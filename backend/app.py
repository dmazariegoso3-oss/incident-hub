"""IT Incident Hub: API REST y servidor local, sin dependencias externas."""
import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
DB = Path(os.environ.get('INCIDENT_DB', str(ROOT / 'database' / 'incidents.db')))
STATES = ['NUEVO', 'ASIGNADO', 'EN_PROCESO', 'RESUELTO', 'CERRADO']
PRIORITIES = ['BAJA', 'MEDIA', 'ALTA', 'CRITICA']
CATEGORIES = ['Hardware', 'Software', 'Red', 'Accesos', 'Otros']
TRANSITIONS = {'NUEVO': ['ASIGNADO'], 'ASIGNADO': ['EN_PROCESO'], 'EN_PROCESO': ['RESUELTO'], 'RESUELTO': ['CERRADO', 'EN_PROCESO'], 'CERRADO': []}


@contextmanager
def connect():
    connection = sqlite3.connect(DB, timeout=15)
    connection.row_factory = sqlite3.Row
    connection.execute('PRAGMA foreign_keys=ON')
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def initialize():
    DB.parent.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript((ROOT / 'database' / 'schema.sql').read_text(encoding='utf-8'))


def now():
    return datetime.now(timezone.utc).isoformat()


def required(data, name, limit=200):
    value = data.get(name)
    if not isinstance(value, str) or not value.strip() or len(value.strip()) > limit:
        raise ValueError(f'{name}: requerido, máximo {limit} caracteres')
    return value.strip()


def log(conn, incident_id, actor, message):
    conn.execute('INSERT INTO history(incident_id,actor,message,created_at) VALUES(?,?,?,?)', (incident_id, actor, message, now()))


def api(method, path, data=None, query=None):
    data, query = data or {}, query or {}
    with connect() as conn:
        if path == '/api/meta' and method == 'GET':
            return 200, dict(states=STATES, priorities=PRIORITIES, categories=CATEGORIES, transitions=TRANSITIONS)
        if path == '/api/health' and method == 'GET':
            conn.execute('SELECT 1').fetchone()
            return 200, {'status': 'ok', 'version': '0.1.0'}
        if path == '/api/dashboard' and method == 'GET':
            rows = [dict(r) for r in conn.execute('SELECT * FROM incidents')]
            result = {'total': len(rows), 'open': sum(r['status'] != 'CERRADO' for r in rows), 'closed': sum(r['status'] == 'CERRADO' for r in rows), 'critical': sum(r['priority'] == 'CRITICA' and r['status'] != 'CERRADO' for r in rows)}
            for field in ['category', 'technician']:
                counts = {}
                for row in rows:
                    key = row[field] or 'Sin asignar'
                    counts[key] = counts.get(key, 0) + 1
                result[field] = counts
            return 200, result
        if path == '/api/incidents':
            if method == 'GET':
                clauses, values = [], []
                for field in ['status', 'priority', 'category', 'technician']:
                    if query.get(field):
                        clauses.append(f'{field} = ?')
                        values.append(query[field][0])
                search = query.get('q', [''])[0].strip()[:100]
                if search:
                    clauses.append('(instr(lower(title), lower(?)) > 0 OR instr(lower(description), lower(?)) > 0)')
                    values.extend([search, search])
                sql = 'SELECT * FROM incidents' + (' WHERE ' + ' AND '.join(clauses) if clauses else '') + ' ORDER BY id DESC LIMIT 500'
                return 200, [dict(r) for r in conn.execute(sql, values)]
            if method == 'POST':
                title, description, user = required(data, 'title', 150), required(data, 'description', 5000), required(data, 'user', 100)
                if data.get('category') not in CATEGORIES or data.get('priority') not in PRIORITIES:
                    raise ValueError('Categoría o prioridad inválida')
                stamp = now()
                cursor = conn.execute('INSERT INTO incidents(title,description,category,priority,user,status,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)', (title, description, data['category'], data['priority'], user, 'NUEVO', stamp, stamp))
                log(conn, cursor.lastrowid, user, 'Incidente creado')
                return 201, dict(conn.execute('SELECT * FROM incidents WHERE id=?', (cursor.lastrowid,)).fetchone())
        parts = path.strip('/').split('/')
        if len(parts) in (3, 4) and parts[:2] == ['api', 'incidents'] and parts[2].isdigit():
            incident_id = int(parts[2])
            row = conn.execute('SELECT * FROM incidents WHERE id=?', (incident_id,)).fetchone()
            if not row:
                return 404, {'error': 'Incidente no encontrado'}
            if len(parts) == 3 and method == 'GET':
                result = dict(row)
                result['history'] = [dict(r) for r in conn.execute('SELECT * FROM history WHERE incident_id=? ORDER BY id', (incident_id,))]
                return 200, result
            if len(parts) == 4 and parts[3] == 'comments' and method == 'POST':
                actor, message = required(data, 'actor', 100), required(data, 'message', 2000)
                log(conn, incident_id, actor, message)
                return 201, {'ok': True}
            if len(parts) == 3 and method == 'PATCH':
                actor = required(data, 'actor', 100)
                status = data.get('status', row['status'])
                technician = data.get('technician', row['technician'])
                if not isinstance(technician, str) or len(technician.strip()) > 100:
                    raise ValueError('Técnico inválido')
                technician = technician.strip()
                if status != row['status'] and status not in TRANSITIONS[row['status']]:
                    raise ValueError('Transición de estado no permitida')
                if row['status'] == 'CERRADO':
                    raise ValueError('El incidente cerrado es de solo lectura')
                if status != 'NUEVO' and not technician:
                    raise ValueError('Debe asignar un técnico')
                conn.execute('UPDATE incidents SET technician=?,status=?,updated_at=? WHERE id=?', (technician, status, now(), incident_id))
                log(conn, incident_id, actor, f"Estado: {row['status']} → {status}; técnico: {technician or 'Sin asignar'}")
                return 200, {'ok': True}
        return 404, {'error': 'Ruta no encontrada'}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / 'frontend'), **kwargs)

    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('Permissions-Policy', 'camera=(), microphone=(), geolocation=()')
        self.send_header('Content-Security-Policy', "default-src 'self'; style-src 'self'; script-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        super().end_headers()

    def handle_api(self):
        parsed = urlparse(self.path)
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length < 0 or length > 16384:
                self.respond(413, {'error': 'Solicitud demasiado grande'})
                return
            if self.command in ('POST', 'PATCH') and self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                self.respond(415, {'error': 'Se requiere application/json'})
                return
            data = json.loads(self.rfile.read(length)) if length else {}
            if not isinstance(data, dict):
                raise ValueError('Se requiere un objeto JSON')
            code, body = api(self.command, parsed.path, data, parse_qs(parsed.query))
        except (ValueError, UnicodeDecodeError) as exc:
            code, body = 400, {'error': str(exc)}
        except sqlite3.Error:
            code, body = 503, {'error': 'Base de datos no disponible'}
        self.respond(code, body)

    def respond(self, code, body):
        payload = json.dumps(body, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if urlparse(self.path).path.startswith('/api/'):
            self.handle_api()
        elif urlparse(self.path).path in ('/', '/index.html', '/app.js', '/styles.css'):
            super().do_GET()
        else:
            self.send_error(404)

    do_POST = handle_api
    do_PATCH = handle_api


if __name__ == '__main__':
    initialize()
    host, port = os.environ.get('HOST', '127.0.0.1'), int(os.environ.get('PORT', '8000'))
    print(f'Incident Hub: http://{host}:{port}', flush=True)
    ThreadingHTTPServer((host, port), Handler).serve_forever()
