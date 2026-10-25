# IT Incident Hub

Mesa de servicio académica para registrar incidentes de TI, asignarlos, darles seguimiento y consultar indicadores. El proyecto demuestra el flujo de trabajo DevOps de una aplicación funcional; no está preparado para uso comercial ni para exposición directa a Internet.

## Estado publicado

- Repositorio único y público: [dmazariegoso3-oss/incident-hub](https://github.com/dmazariegoso3-oss/incident-hub).
- El [PR #1](https://github.com/dmazariegoso3-oss/incident-hub/pull/1) está fusionado en `main`; GitHub muestra la aprobación de la segunda cuenta y dos checks exitosos.
- Versión del código: `0.1.0`. La release `v1.0.0` y varios requisitos de la rúbrica todavía están pendientes.
- El PDF del curso sigue pidiendo Azure Boards y Azure Pipelines; GitHub Issues, Projects y Actions no se deben presentar como sustitutos aprobados hasta confirmarlo con el ingeniero.

## Funciones

- Crear, consultar y filtrar incidentes por estado, prioridad, categoría y técnico.
- Asignar técnicos y avanzar incidentes por `NUEVO`, `ASIGNADO`, `EN_PROCESO`, `RESUELTO` y `CERRADO`.
- Agregar comentarios y consultar la bitácora del incidente.
- Consultar indicadores de abiertos, cerrados, críticos y distribución por categoría y técnico.
- Guardar datos de forma persistente en SQLite.

## Tecnologías

Python 3.13+, `http.server`, SQLite, HTML, CSS y JavaScript sin dependencias de runtime externas. La API REST y la interfaz se sirven desde el mismo origen.

## Ejecución en Windows

Desde la raíz del repositorio:

```powershell
python backend/app.py
```

Abre http://127.0.0.1:8000. La base local se crea en `database/incidents.db` y se conserva al reiniciar. Detén el servidor con `Ctrl+C`.

## Validación y paquete

```powershell
python -m unittest discover -s tests -v
node --check frontend/app.js
python devops/package.py
```

El paquete generado es `dist/incident-hub-0.1.0.zip`. No contiene la base de datos local, secretos ni el historial Git.

## Estructura

- `backend/`: API y servidor local.
- `frontend/`: interfaz web.
- `database/`: esquema SQLite.
- `tests/`: pruebas automatizadas.
- `devops/`: empaquetado.
- `docs/`: arquitectura, backlog, branching, seguridad, deuda, evidencias, release y demostración.
- `.github/workflows/`: CI de GitHub Actions y validación manual self-hosted.
- `azure-pipelines.yml`: configuración de Azure Pipelines pendiente de ejecución.

## Documentación y avance de la rúbrica

- [Arquitectura y API](docs/arquitectura.md)
- [Backlog propuesto](docs/backlog.csv)
- [Flujo de ramas y PR](docs/branching.md)
- [Deuda técnica](docs/deuda-tecnica.md)
- [Seguridad y dependencias](docs/seguridad.md)
- [Release y runner](docs/release.md)
- [Evidencias verificadas y pendientes](docs/evidencias.md)
- [Guion de demostración](docs/demostracion.md)

Estado comprobado: hay un PR real fusionado de los seis solicitados. El tablero/work items, cinco PR adicionales, diagnóstico documentado de un fallo controlado, uso del runner, ejecución de Azure (o aprobación escrita de una alternativa), y releases SemVer siguen pendientes. Consulta `docs/evidencias.md` antes de afirmar que un requisito se completó.

## Límites

La aplicación no autentica usuarios; el actor escrito en un formulario no verifica identidad. No desplegarla en Internet. Para un entorno compartido se necesitarían autenticación, roles, TLS, límites de solicitudes, servidor de producción y respaldos.
