# Evidencias y estado

Actualizado: 24 de octubre de 2026 (Guatemala). Se distingue la configuración de la ejecución real. El acuerdo del instructor sobre usar dos cuentas de GitHub ante la falta de Azure fue comunicado por la estudiante.

| Requisito | Estado verificado | Pendiente |
|---|---|---|
| Repositorio | Un repositorio público: [incident-hub](https://github.com/dmazariegoso3-oss/incident-hub). | — |
| Aplicación | API, interfaz, SQLite, historial, indicadores y búsqueda por texto están integrados en main. | Mostrar el flujo completo en la demostración. |
| Dos cuentas y revisión | La segunda cuenta aprobó #1, #2, #33, #34, #35, #37, #38 y #39. #36 fue fusionado con revisión COMMENTED, no aprobación formal. | Mantener la separación autor/revisor en nuevos PR. |
| PR | #1, #2 y #33–#39 están fusionados. El issue #20 quedó cerrado al integrarse #38. | — |
| GitHub Actions | [CI #65](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40165513124) pasó build, sintaxis JavaScript, 10 pruebas, inventario, auditoría y empaquetado. #39 también pasó sus dos checks. | Validar el artefacto durante la demo. |
| Artefacto | [incident-hub-0.1.0.zip](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40165513124/artifacts/12588126951), 25,029 bytes; SHA-256 58d2c3252bcc086dc707fc5cf23c06eaf57a8c91d9beb8f3e83b7927eeb5eb49. | Validar antes de release. |
| Dependencias | pip-audit 2.10.1 no encontró vulnerabilidades conocidas en el inventario de requirements.txt, vacío, durante CI #65. | Revisar runtime, SQLite, acciones y runner por separado. Ver [dependencias](dependencias.md). |
| Backlog | 30 issues #3–#32 organizados como 2 Epics, 4 Features, 8 historias y 16 Tasks en “IT Incident Hub - Backlog”. El tablero existe pero es privado. | Compartir el tablero con el evaluador si debe revisarlo. |
| Sustitución de Azure | La estudiante informó que el instructor permitió trabajar con dos cuentas de GitHub por falta de Azure. Se usa GitHub Issues/Projects para backlog, Actions para CI y la segunda cuenta para revisión. | Explicar el acuerdo y mostrar evidencias de ambas cuentas. |
| Fallo controlado | No hay secuencia documentada de run fallido, diagnóstico, fix y run verde posterior. | Hacer el ensayo en una rama separada y conservar ambos runs. |
| Runner autohospedado | Existe workflow manual; no hay evidencia de un runner real registrado y usado. | Confirmar si aplica con el sustituto aprobado; si aplica, registrar runner Windows y guardar URL/logs. |
| Deuda técnica | Hay siete deudas identificadas. Las correcciones iniciales están en el producto, pero dos necesitan trazabilidad explícita. | Relacionar issue, commit, PR y prueba para dos correcciones. |
| Versiones y release | Versión actual 0.1.0; no hay tag ni release publicados hasta v1.0.0. | Crear la secuencia SemVer y validar la release final. |
| Demostración | Hay guion escrito; no se ha conservado demo final. | Recorrer creación, filtros, estados, comentarios, indicadores y release; guardar evidencia. |

## Hechos remotos

- #38 fue aprobado por crismazariegosovan-star, fusionado en main, y cerró el issue #20.
- #39 fue aprobado por crismazariegosovan-star y fusionado en main; sus dos checks pasaron.
- Al actualizar este documento no hay PR abiertos.
- El tablero Projects es privado; compartirlo con el evaluador por el mecanismo acordado.

## Próximos pasos

1. Realizar el ensayo de fallo controlado en GitHub Actions y enlazar el run fallido con su corrección y run verde.
2. Registrar y ejecutar un runner autohospedado si el acuerdo del instructor no lo exime.
3. Dar trazabilidad a dos correcciones de deuda técnica mediante issues, commits, PR y pruebas.
4. Revisar dependencias y artefacto, crear tags/releases SemVer y completar v1.0.0.
5. Hacer la demostración final. Compartir el tablero con el evaluador según la necesidad.

No afirmar ejecuciones que no aparecen en el historial de Actions. No se agregan comentarios al código.
