# Seguridad y dependencias

## Implementado

- Escucha local 127.0.0.1 por defecto.
- SQL parametrizado y enumeraciones de dominio.
- Longitudes máximas y cuerpo JSON máximo de 16 KiB.
- Frontend utiliza textContent para mostrar datos ingresados por usuarios.
- CSP limita scripts/estilos al origen; cabecera nosniff.
- Archivos servidos desde frontend y lista explícita de rutas.
- Base, .env y archivos temporales excluidos de Git y ZIP.
- CI solicita permiso contents:read.

## Inventario

Runtime: biblioteca estándar de Python (sqlite3, http.server, json y utilidades); frontend sin paquetes npm. `requirements.txt` no declara dependencias externas. Esto reduce dependencias directas, pero no significa ausencia de vulnerabilidades: Python, SQLite integrado, Node de validación y acciones externas también requieren seguimiento.

| Componente | Severidad conocida en este trabajo | Decisión |
|---|---|---|
| Paquetes Python de runtime | No aplicable: no hay externos | Mantener inventario vacío y auditar requirements en CI |
| Python / SQLite | No evaluada contra avisos vigentes | Actualizar runtime y consultar avisos antes de release |
| Acciones checkout/setup/upload | No evaluada | Fijar SHA revisado y mantener actualizaciones |
| pip-audit (herramienta CI) | No evaluada; instalación sin lock | Fijar versión tras validación de CI |

No hay un reporte de vulnerabilidades remoto todavía; no interpretar la tabla como un escaneo aprobado. Conservar salida de auditoría, fecha, versión exacta, hallazgos, severidad y decisión en la evidencia de release.

## Secretos

No se requieren credenciales para ejecución local. Registro de runner: usar token temporal generado por GitHub; no incluirlo en scripts, commits, documentos o capturas. En despliegue, utilizar secretos del repositorio o del ambiente. No usar secretos en workflows de PR externos ni ejecutar contribuciones no confiables en un runner local.

Limitaciones: sin identidad autenticada, roles, rate limiting, TLS ni endurecimiento de producción. El alcance entregado es demostración local.
