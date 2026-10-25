# Cierre del proyecto: estado actual y plan




Actualizado: 24 de octubre de 2026 (Guatemala). El repositorio único está público. El producto base y documentación están publicados; la entrega académica todavía tiene verificaciones y aprobaciones pendientes.




## Estado de aceptación




| Requisito | Estado verificado | Para cerrar |
|---|---|---|
| Aplicación | API REST, frontend, SQLite, filtros, historial, indicadores y búsqueda publicados en `main`. | Recorrer el flujo completo en la demostración. |
| Repo único | Público en dmazariegoso3-oss/incident-hub. | Mantener todo en ese repo. |
| Backlog 2/4/8/16 | 30 Issues publicados como #3–#32 y vinculados al tablero “IT Incident Hub - Backlog”. Es privado: 28 Todo, 2 In Progress, 0 Done. | Si el evaluador necesita verlo, el propietario debe hacer público el tablero. Confirmar si GitHub sustituye Azure Boards. |
| Seis PR | #1, #2 y #33–#35 fusionados con aprobación de crismazariegosovan-star. #36 está fusionado y sus 2/2 checks pasaron, pero recibió COMMENTED, no APPROVED. | Si se exige una aprobación en cada PR, #36 no tiene aprobación formal; dejar constancia sin falsificar una. |
| Dos cuentas | crismazariegosovan-star aprobó #1, #2 y #33–#35. En #36 dejó un comentario de revisión, no una aprobación formal. | Confirmar si la rúbrica exige aprobación para los seis PR. |
| CI y artefacto | Los checks de #1, #2 y #33–#36 terminaron correctamente. | Conservar enlaces a los runs, auditoría y artefacto. |
| Azure | No hay cuenta ni ejecuciones de Azure confirmadas. | El ingeniero debe aceptar por escrito GitHub como sustituto o dar acceso al Azure del curso. |
| Fallo controlado | No hay evidencia de run fallido deliberado y posterior corrección. | Hacerlo en rama aislada, enlazar diagnóstico, fix y run verde; nunca en main. |
| Runner Windows | Workflow preparado, runner real no registrado ni ejecutado. | Registrar runner y guardar URL, logs y artefacto del job. |
| Deuda/seguridad | Deudas documentadas; PR #33 mejora encabezados HTTP. | Vincular dos correcciones a issues, PR y pruebas; guardar reporte de auditoría. |
| Versionado | Código 0.1.0; sin release v1.0.0 publicada. | Validar artefacto y criterios, luego crear tag y release SemVer. |
| Demo | Guion documentado; demo final aún no registrada. | Ejecutar con datos de muestra y guardar evidencia. |




## Siguiente secuencia




1. #33–#36 ya están fusionados. La segunda cuenta aprobó #33–#35; #36 tiene solo una revisión COMMENTED. Confirmar si la rúbrica exige aprobación formal para ese PR ya fusionado.
2. La funcionalidad de búsqueda API y UI está integrada; validarla durante la demostración.
3. Confirmar con el ingeniero la sustitución de Azure Boards/Pipelines por GitHub. Si el evaluador debe consultar el tablero Projects privado, el propietario debe cambiar su visibilidad a pública.
4. Obtener evidencia fechada de auditoría y artefacto, y completar dos correcciones de deuda con trazabilidad.
5. Ejecutar el fallo controlado y la corrección en una rama segura.
6. Registrar y ejecutar el runner de Windows; completar la prueba del artefacto.
7. Publicar la release solo al satisfacer criterios y terminar con la demo del guion.




No inventar revisiones, ejecuciones ni autorizaciones del ingeniero. Los enlaces de PR, Actions, Projects, runner y release deben apuntar a evidencia real.
