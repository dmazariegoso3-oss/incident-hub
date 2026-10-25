# Cierre del proyecto: estado actual y plan

Actualizado: 24 de octubre de 2026 (Guatemala). La aplicación base está en el único repositorio público. La entrega académica aún tiene evidencia operativa y de release pendiente.

## Estado de aceptación

| Requisito | Estado verificado | Para cerrar |
|---|---|---|
| Aplicación | API REST, frontend, SQLite, bitácora, filtros e indicadores en main. La búsqueda API está integrada; el campo visual se propone en #38. | Revisar y fusionar #38; mostrar el flujo en la demo. |
| Repo único | Público en dmazariegoso3-oss/incident-hub. | — |
| Backlog 2/4/8/16 | 30 issues #3–#32 en el tablero “IT Incident Hub - Backlog”; privado, 28 Todo, 1 In Progress y 1 Done. | Si el evaluador necesita verlo, el propietario debe hacerlo público. Confirmar si GitHub sustituye Azure Boards. |
| Pull requests | #1, #2, #33–#35 y #37 fusionados con aprobación de crismazariegosovan-star. #36 fusionado tras revisión COMMENTED. #38 abierto y revisado aún pendiente. | La segunda cuenta debe revisar #38. #36 sí tiene revisión, pero no aprobación formal. |
| CI, pruebas y paquete | CI #65 pasó build, sintaxis JS, 10 pruebas, inventario, auditoría y empaquetado; artefacto 0.1.0 generado. | Guardar y validar el artefacto en el paso de release. |
| Dependencias | pip-audit 2.10.1 reportó cero vulnerabilidades conocidas al revisar requirements.txt vacío. | Considerar runtime, SQLite, acciones y runner; ver docs/dependencias.md. |
| Azure | No hay ejecución de Azure confirmada. | Obtener aceptación escrita del ingeniero para GitHub o acceso y ejecución real de Azure Boards/Pipelines. |
| Fallo controlado | No se acredita un pipeline fallido deliberado con diagnóstico y corrección. | Hacerlo en rama aislada; enlazar run fallido, causa, fix y run verde. |
| Runner Windows | YAML manual configurado; runner real no registrado ni ejecutado. | Registrar el runner y guardar URL, logs y artefacto. |
| Deuda técnica | Siete puntos identificados; dos correcciones todavía están descritas como locales sin trazabilidad remota. | Resolver dos con issue, rama, commit, PR y prueba. |
| Versionado y release | Código 0.1.0; sin secuencia de tags/release hasta v1.0.0. | Crear versiones SemVer y demostrar controles de validación y aprobación. |
| Demo | Guion escrito; demo final no registrada. | Demostrar el sistema y guardar evidencia. |

## Secuencia

1. La segunda cuenta revisa #38 y confirma que la búsqueda visual funciona en main después de integrarse.
2. Confirmar con el ingeniero el uso de GitHub en lugar de Azure o completar los requisitos en Azure.
3. Ejecutar y documentar auditoría, fallo controlado, runner y dos correcciones trazables.
4. Validar el artefacto, publicar los tags/releases SemVer y preparar la demo final.
5. Si el evaluador necesita el backlog, el propietario cambia la visibilidad del tablero privado a pública.

No presentar archivos de configuración como ejecuciones ni inventar aprobaciones, runs o autorizaciones.
