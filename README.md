# IT Incident Hub

Mesa de servicio académica para registrar incidentes de TI, asignarlos, darles seguimiento y consultar indicadores. Es una demostración universitaria; no está preparada para uso comercial ni para exposición directa a Internet.

## Responsable y revisión

Proyecto individual. Responsable del repositorio: dmazariegoso3-oss. La revisión de cambios se realiza desde la segunda cuenta crismazariegosovan-star.

## Estado verificado al 25 de octubre de 2026

- Repositorio único y público: https://github.com/dmazariegoso3-oss/incident-hub.
- La segunda cuenta aprobó los PR #1, #2, #33, #34, #35 y #37–#40. El PR #36 recibió una revisión COMMENTED, no una aprobación formal. Los PR #1, #2 y #33–#41 constan fusionados.
- Los runs #80 y #81 documentan una falla controlada en rama aislada y su corrección exitosa. El PR #41 conserva la secuencia.
- El CI #65 ejecutó build, sintaxis JavaScript, 10 pruebas, auditoría de dependencias y empaquetado.
- El runner Windows autohospedado completó Self-hosted validation #1: 10 pruebas y artefacto ZIP publicado. Ver https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40214793475.
- Hay 30 elementos del backlog en Issues #3–#32 y en el tablero IT Incident Hub - Backlog. El tablero es privado; comparte acceso con el evaluador si necesita revisarlo.
- La estudiante informó que el instructor permitió usar dos cuentas de GitHub ante la falta de Azure; el acuerdo está documentado en PR #40.
- La demostración local, sus capturas y las pruebas locales están en el [informe de pruebas](docs/Informe_Pruebas_Incident_Hub.pdf). Las 9 pruebas locales y las 10 del runner corresponden a ejecuciones diferentes.

## Pendiente de cierre

- Publicar una secuencia coherente de tags y releases SemVer hasta v1.0.0, después de validar el artefacto final.
- Confirmar que el evaluador tenga acceso al tablero privado o acordar una alternativa visible.
- La auditoría pip-audit no encontró vulnerabilidades conocidas en requirements.txt, que no declara dependencias externas de runtime. El análisis de Python, SQLite, sistema operativo y acciones de GitHub tiene alcance separado; ver docs/dependencias.md.

## Funciones

- Registrar, consultar y filtrar incidentes por estado, prioridad, categoría y técnico; buscar por título o descripción.
- Asignar técnicos y recorrer NUEVO, ASIGNADO, EN_PROCESO, RESUELTO y CERRADO.
- Añadir comentarios y consultar bitácora por incidente.
- Consultar indicadores y guardar los datos persistentemente en SQLite.

## Tecnologías y requisitos

Python 3.13+, http.server, SQLite, HTML, CSS y JavaScript sin dependencias externas de runtime. Requiere Python 3.13 o superior y Node.js solo para revisar sintaxis JavaScript. La API y la interfaz se sirven desde el mismo origen.

## Ejecutar en Windows

Desde la raíz: python backend/app.py. Abre http://127.0.0.1:8000. La base se crea en database/incidents.db y se conserva al reiniciar. Detén con Ctrl+C.

## Validación y paquete

Comandos: python -m unittest discover -s tests -v; node --check frontend/app.js; python devops/package.py. El paquete es dist/incident-hub-0.1.0.zip y excluye la base local, secretos e historial Git.

## Documentación

## Informe de pruebas

La carpeta `docs` contiene únicamente el informe final: [Informe de pruebas](docs/Informe_Pruebas_Incident_Hub.pdf).

## Límites

La aplicación no autentica usuarios; el actor escrito en el formulario no verifica identidad. No desplegarla en Internet. Un entorno compartido requeriría autenticación, roles, TLS, límites de solicitudes, servidor de producción y respaldos.
