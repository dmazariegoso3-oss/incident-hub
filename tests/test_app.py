import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

spec = importlib.util.spec_from_file_location('app', Path(__file__).resolve().parents[1] / 'backend/app.py')
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class IncidentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.previous = app.DB
        app.DB = Path(self.temp.name) / 'test.db'
        app.initialize()

    def tearDown(self):
        app.DB = self.previous
        self.temp.cleanup()

    def create(self, **changes):
        data = dict(title='Sin conexión', description='No funciona la red', user='Ana', category='Red', priority='CRITICA')
        data.update(changes)
        return app.api('POST', '/api/incidents', data)[1]

    def test_create_and_persist(self):
        row = self.create()
        app.initialize()
        result = app.api('GET', f"/api/incidents/{row['id']}")[1]
        self.assertEqual(result['status'], 'NUEVO')
        self.assertEqual(len(result['history']), 1)
        self.assertEqual(result['user'], 'Ana')

    def test_required_and_enum_validation(self):
        for changes in [dict(title=' '), dict(description='x'*5001), dict(user=12), dict(priority='URGENTE'), dict(category='SQL')]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.create(**changes)

    def test_complete_lifecycle_and_audit(self):
        row = self.create()
        path = f"/api/incidents/{row['id']}"
        for state in app.STATES[1:]:
            app.api('PATCH', path, dict(actor='Operadora', technician='Luis', status=state))
        result = app.api('GET', path)[1]
        self.assertEqual(result['status'], 'CERRADO')
        self.assertEqual(len(result['history']), 5)
        with self.assertRaises(ValueError):
            app.api('PATCH', path, dict(actor='Ana', status='NUEVO'))

    def test_reject_skip_and_require_technician(self):
        row = self.create()
        for data in [dict(actor='Ana', status='CERRADO'), dict(actor='Ana', status='ASIGNADO')]:
            with self.assertRaises(ValueError):
                app.api('PATCH', f"/api/incidents/{row['id']}", data)
        self.assertEqual(app.api('GET', '/api/dashboard')[1]['open'], 1)

    def test_comments(self):
        row = self.create()
        path = f"/api/incidents/{row['id']}"
        app.api('POST', path+'/comments', dict(actor='Luis', message='Revisando router'))
        self.assertEqual(app.api('GET', path)[1]['history'][-1]['message'], 'Revisando router')

    def test_each_filter_and_sql_injection(self):
        self.create()
        self.create(category='Software', priority='BAJA')
        for field, value in [('category','Red'), ('priority','CRITICA'), ('status','NUEVO')]:
            rows = app.api('GET', '/api/incidents', query={field:[value]})[1]
            self.assertTrue(rows)
            self.assertTrue(all(row[field] == value for row in rows))
        rows = app.api('GET', '/api/incidents', query={'category':["' OR 1=1 --"]})[1]
        self.assertEqual(rows, [])

    def test_dashboard(self):
        self.create()
        self.create(category='Hardware', priority='BAJA')
        result = app.api('GET', '/api/dashboard')[1]
        self.assertEqual((result['total'], result['open'], result['critical']), (2,2,1))
        self.assertEqual(result['category'], {'Red':1, 'Hardware':1})
        self.assertEqual(result['technician'], {'Sin asignar':2})

    def test_missing(self):
        self.assertEqual(app.api('GET', '/api/incidents/999')[0], 404)

    def test_http_contract_and_static_isolation(self):
        server = app.ThreadingHTTPServer(('127.0.0.1', 0), app.Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f'http://127.0.0.1:{server.server_port}'
        try:
            with urlopen(base+'/api/health') as response:
                self.assertEqual(json.load(response)['status'], 'ok')
                self.assertIn('nosniff', response.headers['X-Content-Type-Options'])
            for path, method, body, expected in [('/database/incidents.db','GET',None,404),('/api/incidents','POST',b'{',400),('/api/incidents','POST',b'[]',400)]:
                request = Request(base+path, data=body, method=method, headers={'Content-Type':'application/json'})
                with self.assertRaises(HTTPError) as raised:
                    urlopen(request)
                self.assertEqual(raised.exception.code, expected)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


    def test_text_search_matches_title_description_and_combines_with_filters(self):
        title_match = self.create(title='VPN caida', description='No conecta', category='Hardware')
        description_match = self.create(title='Otro incidente', description='Falla de VPN en sede')
        self.create(title='Correo', description='No recibe mensajes')

        rows = app.api('GET', '/api/incidents', query={'q': ['vpn']})[1]
        self.assertEqual({row['id'] for row in rows}, {title_match['id'], description_match['id']})

        rows = app.api('GET', '/api/incidents', query={'q': ['vpn'], 'category': ['Hardware']})[1]
        self.assertEqual([row['id'] for row in rows], [title_match['id']])

        rows = app.api('GET', '/api/incidents', query={'q': ['   ']})[1]
        self.assertEqual(len(rows), 3)

if __name__ == '__main__':
    unittest.main()
