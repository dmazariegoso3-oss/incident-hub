# Registro de deuda técnica

| ID | Deuda | Impacto | Prioridad | Estado | Verificación |
|---|---|---|---|---|---|
| DT-01 | SQLite no cerraba conexiones al terminar cada operación | Archivos bloqueados en Windows | Alta | Corregida localmente; trazabilidad remota pendiente | 9 pruebas fallaron al limpiar la base; context manager con finally; 9 pruebas pasan |
| DT-02 | Sin cobertura de entradas inválidas y aislamiento de archivos | Regresiones y exposición accidental | Alta | Corregida localmente; trazabilidad remota pendiente | Pruebas de JSON, SQL injection, estados y ruta de base inaccesible |
| DT-03 | No hay autenticación ni roles | Los actores no están verificados | Alta | Pendiente | Incorporar identidad y permisos antes de uso compartido |
| DT-04 | Lista limitada a 500 sin paginación | Consulta parcial a mayor escala | Media | Pendiente | API paginada con orden estable y pruebas |
| DT-05 | Servidor HTTP de biblioteca estándar | No apto para producción pública | Alta | Pendiente | Migrar a servidor de producción con TLS y límites |
| DT-06 | Cambios simultáneos sin control optimista | Última escritura prevalece | Media | Pendiente | Campo versión y respuesta 409 |
| DT-07 | Sin respaldo automatizado | Riesgo de pérdida del archivo local | Media | Pendiente | Respaldo SQLite verificado y ensayo de restauración |

Para cumplir la rúbrica de resolver dos deudas de forma trazable, abrir sus issues, enlazar commits/PR y registrar resultados verificables. La corrección local sola no satisface la evidencia remota.
