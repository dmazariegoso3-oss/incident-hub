# Evidencias y estado

Fecha de trabajo: 22 de octubre de 2026 (Guatemala).

| Requisito | Estado comprobado |
|---|---|
| Un repositorio | Privado creado: https://github.com/dmazariegoso3-oss/incident-hub ; código remoto pendiente |
| Backlog 2/4/8/16 | CSV preparado; tablero remoto pendiente |
| Aplicación y persistencia | Implementadas; pruebas locales aprobadas |
| Pruebas | 9 pruebas unittest, resultado OK |
| JavaScript | node --check aprobado |
| 6 PR y revisión | Pendientes; no hay URLs |
| Revisión con segunda cuenta | Plan definido: cuenta principal abre PR; segunda cuenta prueba y revisa. Ejecución pendiente |
| CI | Configuración preparada, ejecución remota pendiente |
| Fallo controlado en pipeline | Pendiente; el fallo local de SQLite no lo sustituye |
| Self-hosted | Workflow preparado; registro y ejecución pendientes |
| Seguridad | Controles locales; auditoría CI pendiente |
| Dos deudas resueltas con trazabilidad | Dos correcciones locales documentadas; issues/PR pendientes |
| SemVer hasta v1.0.0 | Plan preparado; tags/releases pendientes |
| Azure | YAML preparado sin ejecución; sustitución requiere validación académica |

## Incidencia local real

La primera ejecución de unittest produjo 9 errores `PermissionError: WinError 32` al eliminar las bases temporales. SQLite mantuvo conexiones abiertas porque `with connection` gestiona la transacción pero no cierra la conexión. Se incorporó un context manager que confirma/revierte y ejecuta close en finally. La siguiente ejecución terminó con 9 pruebas aprobadas. Este registro describe una validación local, no una ejecución de pipeline.

Añadir enlaces verificables a issues, PR, revisiones, jobs y releases conforme se generen. No marcar completados requisitos solo por tener archivos de configuración.

## Publicación pendiente

El repositorio privado fue creado y verificado en el navegador. Git push no pudo conectar a github.com:443 incluso con permiso de red concedido. La integración conectada devuelve 404 para el repositorio nuevo: falta habilitar su acceso. No hay código, issues ni PR publicados todavía. La interfaz local se comprobó creando un incidente de demostración; el dashboard mostró un abierto y un crítico.
