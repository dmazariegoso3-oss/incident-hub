# IT Incident Hub




Mesa de servicio académica para registrar incidentes de TI, asignarlos, darles seguimiento y consultar indicadores. Es una demostración universitaria; no está preparada para uso comercial ni para exposición directa a Internet.




## Estado publicado




- Repositorio único y público: https://github.com/dmazariegoso3-oss/incident-hub.
- Hay seis PR reales: #1, #2 y #33–#35 están fusionados con aprobación de crismazariegosovan-star. #36 también está fusionado y su CI pasó, pero la revisión registrada fue comentario (`COMMENTED`), no aprobación (`APPROVED`).
- Los PR #33 (encabezados de seguridad), #34 (búsqueda API), #35 (búsqueda en interfaz) y #36 (evidencias) tienen CI habilitada; consulta la pestaña Checks de cada PR para el resultado vigente.
- La segunda cuenta aprobó #1, #2 y #33–#35. #36 se fusionó tras un comentario; si la rúbrica exige aprobación formal en todos los PR, esa evidencia no está registrada. #34 y #35 ya están integrados en orden.
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
