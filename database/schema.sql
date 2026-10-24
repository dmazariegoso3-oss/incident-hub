PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS incidents (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL, description TEXT NOT NULL,
 category TEXT NOT NULL CHECK(category IN ('Hardware','Software','Red','Accesos','Otros')),
 priority TEXT NOT NULL CHECK(priority IN ('BAJA','MEDIA','ALTA','CRITICA')),
 user TEXT NOT NULL, technician TEXT NOT NULL DEFAULT '',
 status TEXT NOT NULL DEFAULT 'NUEVO' CHECK(status IN ('NUEVO','ASIGNADO','EN_PROCESO','RESUELTO','CERRADO')),
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS history (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 incident_id INTEGER NOT NULL REFERENCES incidents(id),
 actor TEXT NOT NULL, message TEXT NOT NULL, created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_history_incident ON history(incident_id);
CREATE INDEX IF NOT EXISTS idx_incidents_filters ON incidents(status,priority,category,technician);
