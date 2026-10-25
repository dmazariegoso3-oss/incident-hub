# Cierre del proyecto: estado actual y plan

Actualizado: 24 de octubre de 2026 (Guatemala). El repositorio único ya es público y el PR #1 con la aplicación está fusionado en `main`. El código y la validación base están disponibles; falta completar las evidencias de proceso que exige la rúbrica.

## Estado de aceptación

| Requisito | Hoy | Para cerrar |
|---|---|---|
| App funcional | API, interfaz, SQLite, filtros, dashboard e historial publicados | Ejecutar el guion completo delante del evaluador |
| Repo único | Público en GitHub | Mantener ahí todo el proyecto |
| Backlog 2 Epics / 4 Features / 8 historias / 16 tareas | CSV de 30 filas listo | Crear work items en el tablero que autorice el ingeniero; el CSV no es tablero |
| Seis PR con validación/revisión | PR #1 fusionado; 2 checks y una aprobación | Crear cinco PR adicionales con cambios reales, pruebas y revisión de la segunda cuenta |
| Dos cuentas | La segunda cuenta aprobó el PR #1 | En los nuevos PR, que la segunda cuenta pruebe y deje revisión auténtica |
| CI y artefacto | GitHub Actions pasó en el PR #1; workflow de build/test/audit/package existe | Guardar enlaces y salida verificable de auditoría y paquete |
| Azure Boards/Pipelines | YAML de Azure preparado; no hay ejecución confirmada | Ejecutar en Azure DevOps o documentar aprobación expresa del ingeniero para el reemplazo |
| Fallo y corrección de pipeline | No está demostrada la secuencia requerida | Un run fallido aislado, diagnóstico visible, corrección real y run verde posterior |
| Runner autohospedado | Workflow manual preparado | Registrar runner Windows y ejecutar job real; conservar enlace/logs/artefacto |
| Deuda técnica | Siete deudas identificadas; dos correcciones están en el código | Vincular al menos dos correcciones a issue, rama, commit, PR y pruebas |
| Secretos y dependencias | Controles documentados; no hay paquetes externos de runtime | Ejecutar/guardar reporte fechado y revisar avisos de runtime y Actions |
| Versiones y release | Versión de código 0.1.0 y estrategia escrita | Crear releases/tags SemVer y llegar a v1.0.0 solo después de aceptar los criterios |
| Documentación | Arquitectura, seguridad, deuda, release y demo existen | Mantener README/evidencias sincronizados con el estado publicado |

## Secuencia recomendada

1. Revisar este PR documental y pedir a la segunda cuenta que valide la información antes de aprobarlo.
2. Obtener la decisión escrita del ingeniero sobre Azure. Esta es la dependencia que define si se prepara Azure real o se acredita GitHub como sustituto.
3. Publicar el tablero/work items autorizados y enlazar cada cambio.
4. Completar cinco cambios reales adicionales mediante PR, con CI, pruebas y revisiones auténticas; no retrofechar ni inventar historial.
5. Ejecutar una falla controlada en una rama aislada; conservar la ejecución fallida y enlazar el commit correctivo y el run exitoso.
6. Registrar y ejecutar el runner autohospedado de Windows. El token temporal debe introducirse solo en la configuración local de GitHub y nunca guardarse en el repo, documento o captura.
7. Guardar auditoría y artefacto, validar la demo, crear tags/releases y completar v1.0.0 al satisfacer criterios.

No crear PR vacíos ni simular pruebas/revisiones. La evidencia de capturas complementa, pero no reemplaza, el historial del repo y las URLs de runs, issues, PR y releases.
