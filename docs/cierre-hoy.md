# Cierre del proyecto: estado y próximos pasos

Actualizado: 24 de octubre de 2026 (Guatemala). La aplicación y el flujo de revisión por dos cuentas están publicados en un repositorio único.

## Estado de aceptación

| Requisito | Estado | Para cerrar |
|---|---|---|
| Aplicación | API REST, interfaz, SQLite, bitácora, filtros, indicadores y búsqueda visual están en main. | Mostrar el flujo en la demostración. |
| Repositorio | Único y público: dmazariegoso3-oss/incident-hub. | — |
| Backlog | 30 issues #3–#32: 2 Epics, 4 Features, 8 User Stories y 16 Tasks, vinculados al tablero privado “IT Incident Hub - Backlog”. | Compartir el tablero con el evaluador si lo necesita. |
| PR y revisión | #1, #2 y #33–#39 están fusionados; la segunda cuenta aprobó #1, #2, #33–#35 y #37–#39. #36 tiene revisión COMMENTED. | — |
| CI y artefacto | CI #65 pasó 10 pruebas y produjo el artefacto 0.1.0. #39 pasó sus dos checks. | Validar artefacto final en la demo. |
| Sustitución de Azure | El instructor permitió, según informó la estudiante, usar dos cuentas de GitHub ante la falta de Azure. Issues/Projects, Actions y la aprobación separada documentan el proceso acordado. | Presentar el acuerdo y mostrar la evidencia de ambas cuentas. |
| Fallo controlado | Falta secuencia verificable de fallo, diagnóstico, corrección y CI verde. | Hacerla en rama aislada y enlazar ambos runs. |
| Runner | El workflow self-hosted existe; falta ejecución en runner real. | Confirmar si aplica al sustituto acordado; si aplica, registrar y usar runner Windows. |
| Deuda técnica | Siete puntos identificados; faltan vínculos explícitos para dos correcciones. | Crear trazabilidad issue → commit → PR → prueba para dos deudas. |
| Release | Código 0.1.0; todavía no hay tags/releases hasta v1.0.0. | Publicar versiones SemVer al cumplir criterios y validar el artefacto. |
| Demo | Guion disponible; demo final pendiente. | Ejecutar y conservar evidencia. |

## Secuencia de cierre

1. Registrar un run controladamente fallido y su diagnóstico; corregir la causa en la misma rama y conservar el run verde posterior.
2. Dar trazabilidad a dos correcciones de deuda técnica con issues, commits, PR y pruebas.
3. Ejecutar el runner autohospedado si el instructor no lo eximió al autorizar la alternativa.
4. Validar el paquete y publicar tags/releases SemVer hasta v1.0.0 al satisfacer los criterios.
5. Recorrer la demostración final con ambas cuentas y compartir el tablero con el evaluador si lo solicita.

No confundir configuración YAML con ejecución, revisión comentada con aprobación, ni versión local con release publicada.
