# Release y agente autohospedado

## Versionado

La versión publicada en VERSION, health y el paquete es 0.1.0. Todavía no hay tags ni releases de GitHub. Para cumplir el requisito SemVer, cada publicación debe acompañar una versión real validada; no se crean etiquetas retroactivas para simular hitos. La release v1.0.0 se publicará después de que el PR final se apruebe, la CI valide el artefacto y el evaluador acepte los criterios académicos.

## Ambientes y controles

1. Desarrollo: aplicación local y pruebas automatizadas con base aislada.
2. Validación: descargar el artefacto de Actions en una carpeta aparte, usar una base SQLite separada mediante INCIDENT_DB y recorrer el guion de demostración.
3. Release académica: revisar checks verdes, resultado y alcance de la auditoría, historial de PR y paquete; aprobar la validación antes de crear el tag y la release.

Rollback: detener el servidor, conservar la base, restaurar el artefacto previo y verificar /api/health. Antes de cambios de esquema, crear respaldo consistente de SQLite y ensayar la restauración; copiar una base activa sin considerar WAL no garantiza consistencia.

## Runner Windows

Ejecución confirmada: [Self-hosted validation #1](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40214793475), en main, commit 8b3a250bc0dd052d459dea77f53d20e06834ca16. El runner Windows x64, versión 2.338.0, completó local-validation con resultado Succeeded; pasaron 10 pruebas y se generó incident-hub-0.1.0.zip.

El artefacto self-hosted-incident-hub tiene ID 12606818345, tamaño 27,334 bytes y SHA-256 d76351ad95362929e98b9662af662c437d51ac9c73bf95bfdac4113bca685276. GitHub Actions es la evidencia canónica del job; se conserva una copia local del log y una captura de consola.

El workflow Self-hosted validation se ejecuta manualmente y no escucha eventos pull_request; esta ejecución prueba el runner, la suite y el empaquetado, pero no sustituye los checks del CI hospedado para cada PR. El runner debe estar activo para repetir el job.

## Fallo controlado

La secuencia ya quedó ejecutada y documentada en el [PR #41](https://github.com/dmazariegoso3-oss/incident-hub/pull/41), fusionado en main. En la rama aislada codex/controlled-ci-failure, [CI #80 falló](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40166947909) porque la prueba esperaba cuatro coincidencias cuando se habían creado tres. El commit 6ca9465 corrigió la expectativa; [CI #81 pasó](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40167208606), incluyendo las 10 pruebas, auditoría y empaquetado. main no se modificó para provocar el fallo.

## Pendiente antes de v1.0.0

- Fusionar la actualización del informe y la documentación después de la revisión de la segunda cuenta.
- Validar el artefacto y la versión final en CI.
- Confirmar acceso del evaluador al tablero privado o acordar otra forma de presentarlo.
- Crear el tag y la release v1.0.0 después de la aprobación académica y adjuntar el artefacto validado.
