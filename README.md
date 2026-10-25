# IT Incident Hub


Mesa de servicio académica para registrar incidentes de TI, asignarlos, darles seguimiento y consultar indicadores. Es una demostración universitaria; no está preparada para uso comercial ni para exposición directa a Internet.


## Estado publicado


- Repositorio único y público: https://github.com/dmazariegoso3-oss/incident-hub.
- Hay seis PR reales: #1 y #2 están fusionados y aprobados por la segunda cuenta; #33–#36 tienen cambios concretos y siguen abiertos/en revisión.
- Los PR #33 (encabezados de seguridad), #34 (búsqueda API), #35 (búsqueda en interfaz) y #36 (evidencias) tienen CI habilitada; consulta la pestaña Checks de cada PR para el resultado vigente.
- crismazariegosovan-star tiene solicitudes de revisión en #33–#36. Una solicitud no equivale a aprobación. #35 depende de #34 y debe integrarse después.
- Los 30 elementos del backlog están publicados como Issues #3–#32 y asociados al tablero GitHub Projects “IT Incident Hub - Backlog”. El tablero es privado y actualmente muestra 28 elementos en Todo, 2 en In Progress y 0 en Done. Si el evaluador debe consultarlo, el propietario tendrá que cambiar su visibilidad a pública.
- La versión sigue en 0.1.0. No hay release v1.0.0, ejecución de Azure, runner autohospedado ni secuencia de fallo controlado acreditados.
- El curso pide Azure Boards/Pipelines. Confirmar con el ingeniero si acepta GitHub como sustituto; no presentar la alternativa como aprobada sin evidencia.


## Funciones


- Crear y filtrar incidentes por estado, prioridad, categoría, técnico y texto.
- Asignar técnicos y mover incidentes por NUEVO, ASIGNADO, EN_PROCESO, RESUELTO y CERRADO.
- Agregar comentarios y consultar la bitácora.
- Consultar indicadores por estado, prioridad, categoría y técnico.
- Guardar datos persistentemente en SQLite.


## Tecnologías


Python 3.13+, http.server, SQLite, HTML, CSS y JavaScript sin dependencias externas de runtime. API REST e interfaz se sirven desde el mismo origen.


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
