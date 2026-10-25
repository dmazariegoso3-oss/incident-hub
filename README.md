# IT Incident Hub

Mesa de servicio académica para registrar incidentes de TI, asignarlos, darles seguimiento y consultar indicadores. Es una demostración universitaria; no está preparada para uso comercial ni para exposición directa a Internet.

## Estado publicado

- Repositorio único y público: https://github.com/dmazariegoso3-oss/incident-hub.
- Los PR #1, #2 y #33–#40 están fusionados en main; la búsqueda por título y descripción ya está disponible en la interfaz.
- La segunda cuenta crismazariegosovan-star aprobó #1, #2, #33, #34, #35, #37, #38, #39 y #40. El PR #36 recibió revisión COMMENTED, no APPROVED.
- El issue #20 se cerró al fusionar #38. El PR del ensayo controlado documenta [el fallo #80](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40166947909) y [la corrección verificada por CI #81](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40167208606); el PR requiere revisión de la segunda cuenta.
- La estudiante informó que el instructor permitió usar dos cuentas de GitHub ante la falta de Azure. La cuenta principal prepara cambios; la segunda cuenta prueba, revisa y aprueba PR. GitHub Issues/Projects y Actions son la plataforma de trabajo acordada.
- Los 30 elementos del backlog están en Issues #3–#32 y en el tablero “IT Incident Hub - Backlog”. El tablero es privado; compártelo con el evaluador si necesita revisarlo.
- El CI #65 ejecutó build, sintaxis JavaScript, 10 pruebas, auditoría de dependencias y paquete 0.1.0. Ver docs/dependencias.md.

## Pendientes para cerrar la entrega

- Revisar y aprobar desde la segunda cuenta el PR del fallo controlado.
- Ejecutar el workflow de validación con un runner autohospedado, si sigue siendo parte de los criterios aceptados por el instructor.
- Trazar dos correcciones de deuda técnica a issues, commits, PR y pruebas.
- Publicar tags/releases SemVer hasta v1.0.0, cuando se cumplan los criterios.
- Hacer y conservar la demostración final.

## Funciones

- Registrar incidentes con título, descripción, categoría, prioridad, usuario, fecha y estado.
- Asignar técnicos y recorrer NUEVO, ASIGNADO, EN_PROCESO, RESUELTO y CERRADO.
- Añadir comentarios y consultar la bitácora por incidente.
- Filtrar por estado, prioridad, categoría y técnico, y buscar por título o descripción.
- Consultar indicadores por estado, prioridad, categoría y técnico.
- Guardar los datos persistentemente en SQLite.

## Tecnologías

Python 3.13+, http.server, SQLite, HTML, CSS y JavaScript sin dependencias externas de runtime. La API y la interfaz se sirven desde el mismo origen.

## Ejecución en Windows

Desde la raíz del repositorio, ejecuta:

    python backend/app.py

Abre http://127.0.0.1:8000. La base local se crea en database/incidents.db y se conserva al reiniciar. Detén el servidor con Ctrl+C.

## Validación y paquete

    python -m unittest discover -s tests -v
    node --check frontend/app.js
    python devops/package.py

El paquete es dist/incident-hub-0.1.0.zip y excluye la base local, secretos e historial Git.

## Documentación

- Arquitectura y API: docs/arquitectura.md
- Backlog: docs/backlog.csv
- Flujo de ramas y PR: docs/branching.md
- Deuda técnica: docs/deuda-tecnica.md
- Seguridad: docs/seguridad.md
- Auditoría de dependencias: docs/dependencias.md
- Release y runner: docs/release.md
- Evidencias verificadas y pendientes: docs/evidencias.md
- Guion de demostración: docs/demostracion.md

## Límites

La aplicación no autentica usuarios: el actor escrito en el formulario no verifica identidad. No desplegarla en Internet. Un entorno compartido requeriría autenticación, roles, TLS, límites de solicitudes, servidor de producción y respaldos.
