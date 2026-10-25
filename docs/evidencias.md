# Evidencias y estado

Actualizado: 24 de octubre de 2026 (Guatemala). La evidencia distingue configuración, ejecución y resultado. Un YAML o una captura por sí solos no demuestran que una actividad remota se ejecutó.

| Requisito | Estado verificado | Evidencia que falta |
|---|---|---|
| Repositorio | Repositorio único y público: [incident-hub](https://github.com/dmazariegoso3-oss/incident-hub). | — |
| Aplicación | API, interfaz, SQLite, bitácora, indicadores y búsqueda API están en main. La búsqueda visual se propone en el PR #38, abierto a main. | Revisar y fusionar #38; recorrer el flujo en la demostración. |
| PR y revisión | #1, #2, #33–#35 y #37 están fusionados y aprobados por crismazariegosovan-star. #36 fue fusionado tras revisión COMMENTED. #38 está abierto con revisión solicitada. | Revisar #38 desde la segunda cuenta. #36 tiene revisión registrada, aunque no una aprobación APPROVED. |
| GitHub Actions | Los PR #1, #2 y #33–#38 tienen validaciones exitosas. El run [CI #65](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40165513124) ejecutó build, sintaxis JS, 10 pruebas, inventario, auditoría y paquete. | Conservar el enlace y artefacto en la entrega final. |
| Artefacto | [incident-hub-0.1.0.zip](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40165513124/artifacts/12588126951), 25,029 bytes; SHA-256 58d2c3252bcc086dc707fc5cf23c06eaf57a8c91d9beb8f3e83b7927eeb5eb49. | Validarlo durante la demostración de release. |
| Dependencias | pip-audit 2.10.1 informó “No known vulnerabilities found” al revisar requirements.txt; no hay dependencias Python de runtime declaradas. La auditoría ocurrió el 24 de octubre, Guatemala, en CI #65. | El comando no evalúa Python, SQLite integrado, las acciones de GitHub ni la imagen del runner; revisar esos componentes por separado antes de release. |
| Backlog | 30 issues #3–#32, organizados como 2 Epics, 4 Features, 8 User Stories y 16 Tasks en “IT Incident Hub - Backlog”. El tablero es privado: 28 Todo, 1 In Progress y 1 Done. | Si el evaluador debe verlo, el propietario debe cambiar su visibilidad a pública. Confirmar por escrito si GitHub sustituye Azure Boards. |
| Azure Boards / Pipelines | El archivo azure-pipelines.yml está preparado, pero no hay ejecución de Azure verificada. | Ejecutar Azure o guardar aprobación escrita del ingeniero para sustituirlo por GitHub. |
| Fallo controlado | No hay evidencia de fallo deliberado de pipeline con diagnóstico, corrección y run verde posterior. | Registrar ambos runs en una rama aislada; mantener main estable. |
| Runner autohospedado | Workflow manual configurado; runner real no registrado ni ejecutado. | Registrar un runner Windows y guardar URL, logs y artefacto del job. |
| Secretos | El repositorio excluye datos locales y secretos; CI declara contents:read. | Revisar historial y conservar evidencia de auditoría. |
| Deuda técnica | Siete deudas identificadas. Dos correcciones están descritas como locales, pero aún sin issues/PR remotos que acrediten el flujo exigido. | Trazar al menos dos correcciones con issue, rama, commit, PR y pruebas. |
| Versiones y release | Código 0.1.0; la estrategia está documentada, pero no existen tags/releases hasta v1.0.0. | Crear una secuencia SemVer verificable y demostrar ambientes/controles de aprobación. |
| Demostración | Hay un guion documentado; la demostración final no está registrada. | Recorrer creación, filtros, estados, comentarios, indicadores, auditoría y release; conservar evidencia. |

## Hechos remotos

- #33, #34 y #35 pasaron CI, recibieron aprobación de crismazariegosovan-star y se fusionaron. #34 lleva búsqueda textual a la API.
- #35 se fusionó en codex/search-incidents, no en main. El PR #38 lleva su cambio visual a main; sus checks están verdes y la revisión está solicitada.
- #36 tiene checks exitosos y fue fusionado; su revisión consta como COMMENTED, no APPROVED.
- #37 fue aprobado por la segunda cuenta y fusionado.
- El tablero Projects existe y continúa privado. El issue #19 está completado; el issue #20 sigue abierto hasta integrar la búsqueda visual en main.
- CI #65 terminó correctamente con 10 pruebas. pip-audit no encontró vulnerabilidades conocidas en el inventario declarado y generó el artefacto indicado arriba.

## Próximos pasos

1. Obtener la revisión de crismazariegosovan-star para #38 e integrar la búsqueda visual en main.
2. Confirmar con el ingeniero si GitHub sustituye Azure Boards/Pipelines; si no, conseguir acceso a Azure y ejecutar el pipeline.
3. Registrar el runner Windows y la secuencia de fallo deliberado, diagnóstico, corrección y ejecución verde.
4. Llevar dos deudas a PR trazables, fijar evidencia de dependencias y completar tags/releases hasta v1.0.0.
5. Si se requiere acceso del evaluador, hacer público el tablero Projects; luego realizar la demo final y guardar la evidencia.

No inventar revisiones, ejecuciones ni autorizaciones del ingeniero. Mantener los enlaces hacia evidencia real.
