# Branching y trazabilidad

Un repositorio durante las tres semanas. `main` debe contener únicamente integraciones verificadas. Usar `feature/*`, `fix/*`, `refactor/*`; si el entorno de trabajo impone prefijo `codex/`, mantener equivalencia en la descripción.

## Dos cuentas para autoría y validación

La cuenta principal implementa los cambios y abre los PR. La segunda cuenta prueba el cambio en la rama propuesta, verifica el resultado de CI y deja una revisión con comentarios concretos antes de aprobar. La autora incorpora las correcciones y responde a los comentarios desde su cuenta principal. Conservar los dos perfiles de GitHub, la aprobación de revisión, el resultado de pruebas y el enlace del PR como evidencia. La segunda cuenta debe ser controlada por la estudiante y no representar a una persona externa.

Los identificadores E/F/US/T del CSV son locales, no números de issues. Al crear issues registrar sus URLs y referenciarlas con `Closes #n` o `Refs #n`. No usar AB# como si existiera un Work Item Azure cuando no existe.

## Seis PR que deben existir realmente

| PR | Alcance | Validación |
|---|---|---|
| 1 | Arquitectura, backlog y esquema | Revisar criterios y restricciones SQL |
| 2 | API de creación y consulta | Pruebas de creación, persistencia y validación |
| 3 | Asignación, estados y bitácora | Pruebas de ciclo, rechazo y comentarios |
| 4 | Interfaz, filtros e indicadores | Sintaxis JS y demostración en navegador |
| 5 | CI, empaquetado y seguridad | Actions, descarga e inspección de artefacto |
| 6 | Estabilización, runner y release | Regresión, runner real y ensayo de release |

Esta tabla es una propuesta, no evidencia de PR abiertos. La implementación local se preparó antes de publicar; no retrofechar commits. Cada PR debe presentar un cambio real, evidencia de validación y revisión visible de la segunda cuenta. La evidencia debe mostrar actividad real de ambas cuentas y la separación de autoría y prueba.

Activar protección de main y checks obligatorios cuando la disponibilidad de la cuenta lo permita. Revertir mediante PR, sin reescribir historia de main.
