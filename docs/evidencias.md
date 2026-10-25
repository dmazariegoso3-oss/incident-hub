# Evidencias y estado








Actualizado: 24 de octubre de 2026 (Guatemala). Esta tabla diferencia configuración, ejecución y evidencia pública. Un archivo de configuración por sí solo no demuestra que una actividad remota se ejecutó.








| Requisito | Estado verificado | Evidencia que falta |
|---|---|---|
| Repositorio | Público; se decidió usar un único repo: [incident-hub](https://github.com/dmazariegoso3-oss/incident-hub) | — |
| Aplicación y persistencia | API, frontend, SQLite, bitácora e indicadores están publicados en `main` | Completar la demostración final grabada o en vivo |
| PR y revisión | #1, #2 y #33–#35 están fusionados con aprobación de crismazariegosovan-star. #36 está fusionado y tiene 2/2 checks verdes, pero su revisión consta como COMMENTED, no APPROVED. | Si la rúbrica exige aprobación formal para cada PR, falta esa evidencia para #36; un PR fusionado no puede cambiarse retrospectivamente a revisión aprobada. |
| GitHub Actions | Los PR #1, #2, #33, #34, #35 y #36 tienen checks exitosos en su integración. | Conservar los enlaces a ejecuciones y salida de auditoría como evidencia detallada. |
| Backlog | Los 30 elementos de la propuesta 2/4/8/16 están publicados como Issues #3–#32 y asociados al tablero GitHub Projects “IT Incident Hub - Backlog”. El tablero es privado: 28 en Todo, 2 en In Progress y 0 en Done. | Si el evaluador debe consultarlo, el propietario debe hacer público el tablero. Confirmar también si GitHub sustituye Azure Boards. |
| Azure Boards / Pipelines | `azure-pipelines.yml` está en el repo; no se ha verificado ejecución de Azure | Ejecutar Azure o guardar aprobación escrita del ingeniero para sustituirlo por GitHub |
| Fallo controlado de pipeline | No hay evidencia documentada de un fallo deliberado con diagnóstico y corrección enlazados | Registrar run fallido, causa, fix y run exitoso; mantener `main` estable |
| Runner autohospedado | Workflow manual configurado | Registrar y ejecutar un runner real; guardar URL del job, logs y artefacto |
| Seguridad y secretos | Se documentan controles de aplicación y exclusiones; PR CI pasó | Guardar resultado fechado de auditoría, severidad y decisión; revisar historial publicado |
| Deuda técnica | Se identifican siete puntos y se describen dos correcciones en código local/publicado | Trazar las dos correcciones con issues, commits, PR separados y pruebas vinculadas |
| Versiones y release | Código en `0.1.0`; existe estrategia documentada | Crear tags/releases verificables hasta `v1.0.0` y validar el artefacto |








## Hechos remotos




- PR #1, #2, #33, #34 y #35 están fusionados en main y aprobados por crismazariegosovan-star; sus checks pasaron.
- PR #33 protege encabezados HTTP; está fusionado, aprobado por la segunda cuenta y sus 2/2 checks pasaron.
- PR #34 agrega búsqueda textual en API; la suite ejecutó 10 pruebas, sus 2/2 checks pasaron y la segunda cuenta lo aprobó antes de integrarlo.
- PR #35 agrega el campo de búsqueda a la interfaz; sus 2/2 checks pasaron y la segunda cuenta lo aprobó. Se integró después de #34.
- PR #36 actualiza estas evidencias; sus 2/2 checks pasaron y fue fusionado. La segunda cuenta dejó un comentario, no una aprobación formal.
- Los issues #3–#32 están asociados al tablero Projects “IT Incident Hub - Backlog”, que es privado y actualmente tiene 28 elementos en Todo, 2 en In Progress y 0 en Done.
