# Evidencias y estado




Actualizado: 24 de octubre de 2026 (Guatemala). Esta tabla diferencia configuración, ejecución y evidencia pública. Un archivo de configuración por sí solo no demuestra que una actividad remota se ejecutó.




| Requisito | Estado verificado | Evidencia que falta |
|---|---|---|
| Repositorio | Público; se decidió usar un único repo: [incident-hub](https://github.com/dmazariegoso3-oss/incident-hub) | — |
| Aplicación y persistencia | API, frontend, SQLite, bitácora e indicadores están publicados en `main` | Completar la demostración final grabada o en vivo |
| PR y revisión | #1 y #2 fusionados con aprobación de la segunda cuenta. #33–#36 abiertos con revisión solicitada; CI de #33–#36 habilitada y el estado vigente está en cada PR. | Faltan revisiones aprobadas auténticas de la segunda cuenta. #35 está basado en #34 y se integra después. |
| GitHub Actions | CI ejecutó en el PR y los checks asociados terminaron exitosamente | Conservar/verificar enlace de ejecución y salida de auditoría como evidencia detallada |
| Backlog | Los 30 elementos de la propuesta 2/4/8/16 están publicados como Issues #3–#32 y asociados al tablero GitHub Projects “IT Incident Hub - Backlog”. El tablero es privado: 28 en Todo, 2 en In Progress y 0 en Done. | Si el evaluador debe consultarlo, el propietario debe hacer público el tablero. Confirmar también si GitHub sustituye Azure Boards. |
| Azure Boards / Pipelines | `azure-pipelines.yml` está en el repo; no se ha verificado ejecución de Azure | Ejecutar Azure o guardar aprobación escrita del ingeniero para sustituirlo por GitHub |
| Fallo controlado de pipeline | No hay evidencia documentada de un fallo deliberado con diagnóstico y corrección enlazados | Registrar run fallido, causa, fix y run exitoso; mantener `main` estable |
| Runner autohospedado | Workflow manual configurado | Registrar y ejecutar un runner real; guardar URL del job, logs y artefacto |
| Seguridad y secretos | Se documentan controles de aplicación y exclusiones; PR CI pasó | Guardar resultado fechado de auditoría, severidad y decisión; revisar historial publicado |
| Deuda técnica | Se identifican siete puntos y se describen dos correcciones en código local/publicado | Trazar las dos correcciones con issues, commits, PR separados y pruebas vinculadas |
| Versiones y release | Código en `0.1.0`; existe estrategia documentada | Crear tags/releases verificables hasta `v1.0.0` y validar el artefacto |




## Hechos remotos


- PR #1 y PR #2 están fusionados en main; ambos tienen aprobación de crismazariegosovan-star y dos checks exitosos.
- PR #33 protege encabezados HTTP y tiene 2/2 checks exitosos; revisión de la segunda cuenta solicitada.
- PR #34 agrega búsqueda textual en API; Actions ejecutó 10 pruebas y 2/2 checks pasaron; revisión solicitada.
- PR #35 agrega el campo de búsqueda a la interfaz; 2/2 checks pasaron; revisión solicitada. Su base es codex/search-incidents y depende de integrar primero #34.
- PR #36 actualiza estas evidencias; consultar su pestaña Checks para el resultado vigente.
- Los issues #3–#32 están asociados al tablero Projects “IT Incident Hub - Backlog”, que es privado y actualmente tiene 28 elementos en Todo, 2 en In Progress y 0 en Done.
- La revisión formal de #33–#36 está pendiente. Una solicitud de revisión no equivale a aprobación.


## Validación local registrada




El historial local documenta nueve pruebas de `unittest` aprobadas y `node --check frontend/app.js` aprobado. Un fallo local de SQLite ocurrió por conexiones no cerradas y se corrigió con cierre explícito; ese incidente local no sustituye el requisito de fallo de pipeline de Azure.
