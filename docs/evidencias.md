# Evidencias y estado

Actualizado: 25 de octubre de 2026 (Guatemala). Se distinguen ejecuciones locales, runs remotos, cambios fusionados y requisitos todavía condicionados.

| Requisito | Estado verificado | Pendiente |
|---|---|---|
| Repositorio | Único y público: https://github.com/dmazariegoso3-oss/incident-hub. | — |
| Aplicación | API, frontend, SQLite, bitácora, búsqueda e indicadores están en main. La demostración local con datos sintéticos y capturas está en [Informe_Pruebas_Incident_Hub.pdf](Informe_Pruebas_Incident_Hub.pdf). | Mostrar la demo en la defensa si el evaluador la solicita. |
| Pruebas locales | 9 pruebas unittest aprobadas en el checkout de la demostración; node --check aprobado; GET / devolvió HTTP 200 y /api/health status ok. | No mezclar con los resultados de runs remotos. |
| GitHub Actions hospedado | [CI #65](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40165513124) pasó build, sintaxis JavaScript, 10 pruebas, inventario, pip-audit y empaquetado. | Validar el artefacto asociado antes de la release final. |
| Runner autohospedado | [Self-hosted validation #1](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40214793475) terminó correctamente en Windows x64, runner 2.338.0; pasó 10 pruebas y publicó el artefacto self-hosted-incident-hub. | El runner debe estar encendido si se necesita repetir el job. |
| Fallo controlado | [CI #80](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40166947909) falló en rama aislada; commit 6ca9465 corrigió la aserción y [CI #81](https://github.com/dmazariegoso3-oss/incident-hub/actions/runs/40167208606) pasó. La secuencia está documentada en el [PR #41](https://github.com/dmazariegoso3-oss/incident-hub/pull/41), ya fusionado. | — |
| Pull requests y revisión | #1, #2 y #33–#41 están fusionados. crismazariegosovan-star aprobó #1, #2, #33–#35 y #37–#40; #36 tuvo revisión COMMENTED y #41 se fusionó sin aprobación formal registrada. | Se superó el mínimo de seis PR con aprobación; mantener dos cuentas separadas en nuevos cambios. |
| Backlog / Project | 30 Issues #3–#32 organizados como 2 Epics, 4 Features, 8 User Stories y 16 Tasks en el Project IT Incident Hub - Backlog. | El tablero es privado; compartirlo con el evaluador si necesita acceso. |
| Sustitución de Azure | La estudiante informó que el instructor permitió usar dos cuentas de GitHub por falta de Azure. El acuerdo se registró en el PR #40. | Mostrar el PR #40 si el evaluador solicita la confirmación. |
| Dependencias | CI #65 ejecutó pip-audit 2.10.1 contra requirements.txt vacío y no halló vulnerabilidades conocidas en dependencias Python declaradas. El alcance y las limitaciones están en [docs/dependencias.md](dependencias.md). | El escaneo no evalúa Python, SQLite, el sistema operativo ni acciones externas; revisar esos componentes antes de release. |
| Deuda técnica | Siete puntos documentados. DT-01 y DT-02 se corrigieron en el producto, con commits y pruebas del PR #1. | Si la rúbrica pide work items individuales, enlazar las dos correcciones a Issues explícitos. |
| Versiones y release | Código y paquete actuales: 0.1.0; estrategia de ambientes y rollback documentada en [docs/release.md](release.md). No hay release publicada. | Publicar una secuencia SemVer verificable hasta v1.0.0 cuando se apruebe la entrega. |

## Evidencia remota principal

- PR #1 está fusionado y aprobado por la segunda cuenta; PR #2 también está fusionado y aprobado.
- El run self-hosted #1 usó el commit 8b3a250bc0dd052d459dea77f53d20e06834ca16. El log informa 10 pruebas en 0.821 s y el ZIP incident-hub-0.1.0.zip de 27,334 bytes.
- Artefacto self-hosted-incident-hub: ID 12606818345; SHA-256 d76351ad95362929e98b9662af662c437d51ac9c73bf95bfdac4113bca685276.
- CI #65 produjo incident-hub-0.1.0.zip de 25,029 bytes; su auditoría cubre el inventario de paquetes Python declarado, no todas las capas del sistema.
- La cuenta crismazariegoso3-oss preparó los PR y crismazariegosovan-star registró las aprobaciones indicadas arriba.

## Orden final

1. Compartir el Project privado con el evaluador si requiere revisarlo.
2. Revisar y aprobar este PR documental desde la segunda cuenta.
3. Ejecutar la validación final del artefacto y crear releases/tags SemVer hasta v1.0.0 según aceptación del instructor.
4. Mostrar la aplicación y el flujo de revisión en la defensa.

No afirmar que el informe o la release están en main hasta fusionar el PR y crear los tags. Las capturas complementan los registros de Actions, commits, PR e Issues; no los sustituyen.
