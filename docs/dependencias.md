# Auditoría de dependencias

## Resultado de CI

- Fecha local: 24 de octubre de 2026, Guatemala (run UTC: 2026-10-25 05:26).
- Workflow: [CI #65](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40165513124), asociado al PR #38.
- Herramienta: pip-audit 2.10.1.
- Alcance directo: requirements.txt no declara paquetes externos de runtime; el frontend tampoco tiene dependencias npm de runtime.
- Resultado del comando pip-audit -r requirements.txt: “No known vulnerabilities found”. No hubo hallazgos ni severidades/CVE que resolver dentro de ese inventario.
- Decisión: no hay una actualización de paquete runtime que aplicar a partir de este escaneo. Repetir la auditoría antes de publicar una release y registrar los hallazgos nuevos si aparecen.

## Alcance y limitaciones

La comprobación se ejecutó contra el inventario declarado en requirements.txt, que estaba vacío. No equivale a afirmar que el sistema completo está libre de vulnerabilidades. pip-audit no evalúa el intérprete de Python, SQLite incluido con el intérprete, el sistema operativo del runner, las acciones de GitHub ni el paquete pip-audit y sus propias dependencias. La instalación de pip-audit se realiza sin versión fijada en el workflow; esa herramienta es de CI, no una dependencia de runtime de la aplicación.

La interfaz usa JavaScript del navegador y no declara paquetes en package.json. El workflow verifica sintaxis con Node.js, pero esta auditoría no analiza Node ni acciones externas. Antes de una release, revisar avisos del runtime y las acciones; mantener sus versiones actualizadas y repetir este reporte con fecha.

## Artefacto de la ejecución

- Archivo: incident-hub-0.1.0.zip.
- Tamaño: 25,029 bytes.
- SHA-256: 58d2c3252bcc086dc707fc5cf23c06eaf57a8c91d9beb8f3e83b7927eeb5eb49.
- [Descargar artefacto de CI #65](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40165513124/artifacts/12588126951).

El mismo run ejecutó la compilación de Python, la comprobación de sintaxis de frontend/app.js y 10 pruebas de unittest; todas terminaron correctamente. Este artefacto corresponde a la versión 0.1.0 del PR #38, no a una release v1.0.0.
