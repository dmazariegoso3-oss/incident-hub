# Evidencias y estado

Actualizado: 24 de octubre de 2026 (Guatemala). Esta tabla diferencia configuración, ejecución y evidencia pública. Un archivo de configuración por sí solo no demuestra que una actividad remota se ejecutó.

| Requisito | Estado verificado | Evidencia que falta |
|---|---|---|
| Repositorio | Público; se decidió usar un único repo: [incident-hub](https://github.com/dmazariegoso3-oss/incident-hub) | — |
| Aplicación y persistencia | API, frontend, SQLite, bitácora e indicadores están publicados en `main` | Completar la demostración final grabada o en vivo |
| PR y revisión | [PR #1 fusionado](https://github.com/dmazariegoso3-oss/incident-hub/pull/1); revisión aprobada por `crismazariegosovan-star`; dos checks pasaron | La rúbrica pide seis PR reales; solo 1 está comprobado |
| GitHub Actions | CI ejecutó en el PR y los checks asociados terminaron exitosamente | Conservar/verificar enlace de ejecución y salida de auditoría como evidencia detallada |
| Backlog | `docs/backlog.csv` contiene la propuesta 2/4/8/16 | Publicar y relacionar los work items en el tablero que el ingeniero acepte |
| Azure Boards / Pipelines | `azure-pipelines.yml` está en el repo; no se ha verificado ejecución de Azure | Ejecutar Azure o guardar aprobación escrita del ingeniero para sustituirlo por GitHub |
| Fallo controlado de pipeline | No hay evidencia documentada de un fallo deliberado con diagnóstico y corrección enlazados | Registrar run fallido, causa, fix y run exitoso; mantener `main` estable |
| Runner autohospedado | Workflow manual configurado | Registrar y ejecutar un runner real; guardar URL del job, logs y artefacto |
| Seguridad y secretos | Se documentan controles de aplicación y exclusiones; PR CI pasó | Guardar resultado fechado de auditoría, severidad y decisión; revisar historial publicado |
| Deuda técnica | Se identifican siete puntos y se describen dos correcciones en código local/publicado | Trazar las dos correcciones con issues, commits, PR separados y pruebas vinculadas |
| Versiones y release | Código en `0.1.0`; existe estrategia documentada | Crear tags/releases verificables hasta `v1.0.0` y validar el artefacto |

## Hechos remotos

- PR #1 fue fusionado en `main` el 24 de octubre de 2026; el evento de GitHub muestra el commit de merge `44d6a11` y dos checks exitosos.
- La segunda cuenta dejó una aprobación visible. Esto prueba una revisión para PR #1, no seis revisiones ni una serie completa de pruebas por PR.
- La búsqueda actual del repo no muestra issues; no se ve un tablero publicado.

## Validación local registrada

El historial local documenta nueve pruebas de `unittest` aprobadas y `node --check frontend/app.js` aprobado. Un fallo local de SQLite ocurrió por conexiones no cerradas y se corrigió con cierre explícito; ese incidente local no sustituye el requisito de fallo de pipeline de Azure.

## Próximo orden

1. Actualizar README y evidencias en este PR documental.
2. Acordar con el ingeniero si GitHub puede reemplazar Azure Boards/Pipelines y registrar la respuesta.
3. Materializar el backlog en el tablero autorizado y vincular issues, ramas, commits y PR.
4. Completar cinco cambios adicionales mediante PR con pruebas/revisión auténticas; no retrofechar ni inventar historial.
5. Capturar la secuencia de fallo controlado y corrección, y ejecutar el runner si el acceso local está disponible.
6. Auditar dependencias, validar artefacto, publicar versiones y completar la demo.
