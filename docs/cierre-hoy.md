# Cierre del proyecto: estado actual y plan

Actualizado: 24 de octubre de 2026 (Guatemala). El repositorio único está público. El producto base y documentación están publicados; la entrega académica todavía tiene verificaciones y aprobaciones pendientes.

## Estado de aceptación

| Requisito | Estado verificado | Para cerrar |
|---|---|---|
| Aplicación | API REST, frontend, SQLite, filtros, historial e indicadores publicados. PR #34 añade búsqueda API y #35 la expone en el panel. | La segunda cuenta prueba la búsqueda y la demostración recorre el flujo completo. |
| Repo único | Público en dmazariegoso3-oss/incident-hub. | Mantener todo en ese repo. |
| Backlog 2/4/8/16 | 30 Issues publicados como #3–#32. | Organizar y relacionar en GitHub Projects; el tablero todavía no existe. |
| Seis PR | #1 y #2 fusionados y aprobados; #33–#36 son cambios reales y siguen abiertos con revisiones solicitadas. #33, #34 y #35 tienen 2/2 checks exitosos. | La segunda cuenta debe dejar aprobaciones reales en #33–#36. Integrar #34 antes de #35, cuya rama base es codex/search-incidents. Confirmar CI de #36. |
| Dos cuentas | crismazariegosovan-star aprobó #1 y #2. | Revisar cambios de #33–#36; una solicitud no cuenta como aprobación. |
| CI y artefacto | Actions pasa en #1, #2, #33, #34 y #35. | Conservar enlaces a runs, auditoría y artefacto; comprobar resultados de #36. |
| Azure | No hay cuenta ni ejecuciones de Azure confirmadas. | El ingeniero debe aceptar por escrito GitHub como sustituto o dar acceso al Azure del curso. |
| Fallo controlado | No hay evidencia de run fallido deliberado y posterior corrección. | Hacerlo en rama aislada, enlazar diagnóstico, fix y run verde; nunca en main. |
| Runner Windows | Workflow preparado, runner real no registrado ni ejecutado. | Registrar runner y guardar URL, logs y artefacto del job. |
| Deuda/seguridad | Deudas documentadas; PR #33 mejora encabezados HTTP. | Vincular dos correcciones a issues, PR y pruebas; guardar reporte de auditoría. |
| Versionado | Código 0.1.0; sin release v1.0.0 publicada. | Validar artefacto y criterios, luego crear tag y release SemVer. |
| Demo | Guion documentado; demo final aún no registrada. | Ejecutar con datos de muestra y guardar evidencia. |

## Siguiente secuencia

1. La segunda cuenta revisa #33 y #34, y deja comentarios o aprobaciones auténticas. Revisa #35 y #36 también; no se fusionan PR sin la aprobación solicitada.
2. Después de aprobarse, integrar #34 antes de #35. Luego integrar #33 y #36 según su revisión.
3. Organizar los Issues #3–#32 en un tablero Projects. Confirmar con el ingeniero la sustitución de Azure Boards/Pipelines por GitHub.
4. Obtener evidencia fechada de auditoría y artefacto, y completar dos correcciones de deuda con trazabilidad.
5. Ejecutar el fallo controlado y la corrección en una rama segura.
6. Registrar y ejecutar el runner de Windows; completar la prueba del artefacto.
7. Publicar la release solo al satisfacer criterios y terminar con la demo del guion.

No inventar revisiones, ejecuciones ni autorizaciones del ingeniero. Los enlaces de PR, Actions, Projects, runner y release deben apuntar a evidencia real.
