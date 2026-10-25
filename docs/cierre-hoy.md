# Cierre del proyecto: estado y próximos pasos

Actualizado: 25 de octubre de 2026 (Guatemala). La aplicación y el flujo de revisión por dos cuentas están publicados en un repositorio único.

## Estado de aceptación

| Requisito | Estado | Para cerrar |
|---|---|---|
| Aplicación | API REST, interfaz, SQLite, bitácora, filtros, indicadores y búsqueda visual están en main. | Mostrar el flujo en la demostración. |
| Repositorio | Único y público: dmazariegoso3-oss/incident-hub. | — |
| Backlog | 30 issues #3–#32: 2 Epics, 4 Features, 8 User Stories y 16 Tasks, vinculados al tablero privado “IT Incident Hub - Backlog”. | Compartir el tablero con el evaluador si lo necesita. |
| PR y revisión | #1, #2 y #33–#40 están fusionados; la segunda cuenta aprobó #1, #2, #33–#35 y #37–#40. #36 tiene revisión COMMENTED. | Revisar el PR del ensayo controlado desde la segunda cuenta. |
| CI y artefacto | CI #65 pasó 10 pruebas y produjo el artefacto 0.1.0. El ensayo aislado [falló en #80](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40166947909), se corrigió en `6ca9465` y [CI #81 pasó](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40167208606). | Validar artefacto final en la demo. |
| Sustitución de Azure | La estudiante informó que el instructor permitió usar dos cuentas de GitHub ante la falta de Azure. Issues/Projects, Actions y la aprobación separada documentan el proceso acordado. | Presentar el acuerdo y mostrar la evidencia de ambas cuentas. |
| Fallo controlado | Registrado en rama aparte: #80 detectó una aserción incorrecta (`3 != 4`); commit `6ca9465` espera las tres filas creadas y #81 quedó verde. | Revisar el PR de evidencia desde la segunda cuenta. |
| Runner | El workflow self-hosted existe; falta ejecución en runner real. | Confirmar que sigue en los criterios; si aplica, registrar y usar runner Windows. |
| Deuda técnica | Siete puntos identificados; faltan vínculos explícitos para dos correcciones. | Crear trazabilidad issue → commit → PR → prueba para dos deudas. |
| Release | Código 0.1.0; todavía no hay tags/releases hasta v1.0.0. | Publicar versiones SemVer al cumplir criterios y validar el artefacto. |
| Demo | Guion disponible; demo final pendiente. | Ejecutar y conservar evidencia. |

## Secuencia de cierre

1. Obtener la revisión de la segunda cuenta en el PR de evidencia del fallo controlado.
2. Dar trazabilidad a dos correcciones de deuda técnica con issues, commits, PR y pruebas.
3. Ejecutar el runner autohospedado si permanece en los criterios acordados; requiere registrarlo y usarlo en la computadora.
4. Validar el paquete y publicar tags/releases SemVer hasta v1.0.0 al satisfacer los criterios.
5. Recorrer la demostración final con ambas cuentas y compartir el tablero con el evaluador si lo solicita.

No confundir configuración YAML con ejecución, revisión comentada con aprobación, ni versión local con release publicada.
