# Release y agente autohospedado

## Versionado

Versión actual de código: 0.1.0. Secuencia propuesta: v0.1.0 (base funcional), v0.2.0 (automatización validada), v0.3.0 (estabilización), v1.0.0 (criterios completos). Son hitos futuros hasta que existan tags y releases remotos. Mantener VERSION, health y etiqueta visual sincronizados.

## Ambientes y controles

1. Desarrollo: base local; pruebas automáticas aisladas.
2. Validación: extraer artefacto CI en carpeta aparte; usar base distinta mediante INCIDENT_DB; recorrer el guion de demostración.
3. Release académica: responsable revisa CI verde, auditoría, historial de PR y runner. Crear tag y release solo tras aprobación de validación documentada.

Rollback: detener servidor, conservar base, restaurar artefacto anterior y ejecutar health. Antes de cambios de esquema generar respaldo consistente de SQLite y ensayar restauración; copiar una base activa sin considerar WAL no garantiza consistencia.

## Runner Windows

Configuración preparada, **no instalado ni ejecutado todavía**. En repositorio GitHub: Settings → Actions → Runners → New self-hosted runner. Descargar el paquete oficial indicado, verificar instrucciones y registrarlo con el token temporal mostrado. Usar una carpeta dedicada fuera del repositorio. Tener Python en PATH. Iniciar el runner solo durante la práctica; detenerlo al finalizar.

El workflow `Self-hosted validation` se ejecuta manualmente. No escucha eventos pull_request. Tras una ejecución exitosa conservar URL de run, nombre del runner, logs de pruebas y artefacto. Un YAML con runs-on self-hosted no demuestra uso real.

## Fallo controlado

Abrir un issue para un ensayo en rama aislada. Introducir una aserción deliberadamente incorrecta en una prueba con explicación visible y ejecutar CI. Conservar URL fallida, diagnóstico y log; corregir con un commit enlazado, esperar ejecución exitosa, revisar y fusionar mediante PR. Nunca introducir el fallo en main ni borrar la ejecución fallida. La secuencia aún no se ha realizado en GitHub.
