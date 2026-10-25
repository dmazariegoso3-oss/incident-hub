# IT Incident Hub

Mesa de servicio académica para registrar incidentes de TI, asignarlos, darles seguimiento y consultar indicadores. Es una demostración universitaria; no está preparada para uso comercial ni para exposición directa a Internet.

## Estado publicado

- Repositorio único y público: https://github.com/dmazariegoso3-oss/incident-hub.
- Se abrieron ocho PR con cambios concretos: #1, #2 y #33–#37 están fusionados; #38 está abierto para llevar la búsqueda visual a main.
- crismazariegosovan-star aprobó #1, #2, #33, #34, #35 y #37. #36 se fusionó con una revisión COMMENTED, no APPROVED. #38 tiene revisión solicitada.
- Los checks de #1, #2 y #33–#38 pasaron. El PR #38 añade a main el campo visual que #35 integró en codex/search-incidents.
- Los 30 elementos del backlog están en Issues #3–#32 y vinculados al tablero “IT Incident Hub - Backlog”. El tablero es privado y muestra 28 elementos en Todo, 1 en In Progress y 1 en Done. Si el evaluador debe consultarlo, el propietario tendrá que hacer público el tablero.
- CI #65 ejecutó 10 pruebas, la auditoría de requirements.txt no encontró vulnerabilidades conocidas y produjo el paquete 0.1.0. Ver docs/dependencias.md para alcance y límites.
- Aún no hay release v1.0.0, ejecución confirmada de Azure, runner autohospedado utilizado, ni evidencia del fallo controlado y su corrección.
- La rúbrica pide Azure Boards/Pipelines. Confirmar con el ingeniero por escrito si acepta GitHub como sustituto; no presentar la alternativa como aprobada sin evidencia.

## Funciones

- Registrar incidentes con título, descripción, categoría, prioridad, usuario, fecha y estado.
- Asignar técnicos y recorrer NUEVO, ASIGNADO, EN_PROCESO, RESUELTO y CERRADO.
- Añadir comentarios y consultar la bitácora por incidente.
- Filtrar por estado, prioridad, categoría y técnico. La API también permite buscar por título y descripción; el campo de interfaz está propuesto en el PR #38.
- Consultar indicadores por estado, prioridad, categoría y técnico.
- Guardar los datos persistentemente en SQLite.

## Tecnologías

Python 3.13+, http.server, SQLite, HTML, CSS y JavaScript sin dependencias externas de runtime. La API y la interfaz se sirven desde el mismo origen.

## Ejecución en Windows

Desde la raíz del repositorio, ejecuta:

    python backend/app.py

Abre http://127.0.0.1:8000. La base local se crea en database/incidents.db y se conserva al reiniciar. Detén el servidor con Ctrl+C.

## Validación y paquete

    python -m unittest discover -s tests -v
    node --check frontend/app.js
    python devops/package.py

El paquete es dist/incident-hub-0.1.0.zip y excluye la base local, secretos e historial Git.

## Documentación

- Arquitectura y API: docs/arquitectura.md
- Backlog: docs/backlog.csv
- Flujo de ramas y PR: docs/branching.md
- Deuda técnica: docs/deuda-tecnica.md
- Seguridad: docs/seguridad.md
- Auditoría de dependencias: docs/dependencias.md
- Release y runner: docs/release.md
- Evidencias verificadas y pendientes: docs/evidencias.md
- Guion de demostración: docs/demostracion.md

## Límites

La aplicación no autentica usuarios: el actor escrito en el formulario no verifica identidad. No desplegarla en Internet. Un entorno compartido requeriría autenticación, roles, TLS, límites de solicitudes, servidor de producción y respaldos.
