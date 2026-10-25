# Evidencias y estado


Actualizado: 24 de octubre de 2026 (Guatemala). Esta tabla diferencia configuración, ejecución y evidencia pública. Un archivo de configuración por sí solo no demuestra que una actividad remota se ejecutó.


| Requisito | Estado verificado | Evidencia que falta |
|---|---|---|
| Repositorio | Público; se decidió usar un único repo: [incident-hub](https://github.com/dmazariegoso3-oss/incident-hub) | — |
| Aplicación y persistencia | API, frontend, SQLite, bitácora e indicadores están publicados en `main` | Completar la demostración final grabada o en vivo |
| PR y revisión | Seis PR reales: #1 y #2 fusionados con aprobación de la segunda cuenta; #33 seguridad, #34 búsqueda API, #35 búsqueda UI y #36 evidencias están abiertos o en revisión. #33, #34 y #35 tienen 2/2 checks exitosos. | Faltan las revisiones aprobadas de #33–#36; no contar solicitudes como aprobaciones. #35 está apilado sobre #34 y debe integrarse después. |
| GitHub Actions | CI ejecutó en el PR y los checks asociados terminaron exitosamente | Conservar/verificar enlace de ejecución y salida de auditoría como evidencia detallada |
| Backlog | Los 30 elementos de la propuesta 2/4/8/16 están publicados como Issues #3–#32. | No hay un tablero GitHub publicado; falta organizar los issues en Projects o confirmar el sustituto aceptado para Azure Boards. |
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
- PR #36 actualiza estas evidencias; verificar sus checks y conservar el enlace del run.
- Los issues #3–#32 contienen los 30 elementos de backlog. No hay aún un tablero Projects asociado.
- La revisión formal de #33–#36 está pendiente. Una solicitud de revisión no equivale a aprobación.

## Validación local registrada


El historial local documenta nueve pruebas de `unittest` aprobadas y `node --check frontend/app.js` aprobado. Un fallo local de SQLite ocurrió por conexiones no cerradas y se corrigió con cierre explícito; ese incidente local no sustituye el requisito de fallo de pipeline de Azure.


## Próximo orden

1. Obtener las revisiones auténticas de la segunda cuenta para #33–#36; integrar #34 antes de #35.
2. Crear y relacionar el tablero GitHub Projects para los issues #3–#32. Confirmar con el ingeniero si GitHub sustituye Azure Boards y Pipelines.
3. Completar evidencia de auditoría de dependencias, artefacto y dos deudas trazadas mediante PR y pruebas.
4. Ejecutar la secuencia de fallo controlado y corrección en rama aislada, conservando los enlaces de ambos runs.
5. Registrar un runner Windows real y ejecutar su workflow; publicar release SemVer solo al cumplir la aceptación.
6. Cerrar con la demostración en vivo o grabada y guardar sus evidencias.
