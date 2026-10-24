# Cierre del proyecto: estado y pasos pendientes

Actualizado: 24 de octubre de 2026. Este estado se basa en el código local y en las respuestas disponibles de GitHub; un archivo YAML o un plan escrito no demuestra que una actividad remota ocurrió.

## Estado de aceptación

| Requisito | Preparado localmente | Evidencia aún necesaria |
|---|---:|---|
| Aplicación de incidentes, API, persistencia y dashboard | Sí | Demo y código publicados en el único repo |
| 2 Epics, 4 Features, 8 historias, 16 tareas con responsable, prioridad, estimación y estado | CSV de 30 filas | Publicar en un tablero; confirmar con el ingeniero si acepta GitHub Projects/Issues por Azure Boards |
| Ramas y trazabilidad | Dos ramas y commits locales | Push, issues con IDs reales, commits y PR enlazados |
| 6 PR reales y revisión | Plantilla y plan de seis cambios | Abrir PR individualmente; segunda cuenta prueba y escribe revisión auténtica; resolver comentarios antes de integrar |
| 5 deudas identificadas y 2 resueltas | Seis registradas; dos correcciones implementadas y validadas en local | Issues, commits y PR que conecten corrección, causa y pruebas |
| CI, pruebas, dependencias y artefacto | Workflow de GitHub Actions y YAML de Azure | Confirmar aceptación del reemplazo de Azure; ejecutar el workflow, guardar run, auditoría y ZIP publicado |
| Fallo de pipeline, diagnóstico y corrección | Caso y pasos planeados | Run real fallido en rama de ensayo, run exitoso tras fix y enlaces a ambos; nunca simular con un fallo local |
| Agente autohospedado | Workflow manual preparado | Registrar runner real, ejecutar workflow y guardar URL del job/runner y artefacto |
| Secretos protegidos | Exclusiones y documentación | Inspeccionar los commits publicados; almacenar únicamente secretos necesarios como secretos del ambiente |
| Dependencias, severidad y decisión | Inventario sin paquetes Python de runtime; auditoría prevista | Ejecutar auditoría, guardar fecha y salida; incluir runtime, SQLite y Actions en la revisión |
| SemVer hasta v1.0.0 | Versión local 0.1.0 y secuencia propuesta | Tags y releases verificables para cada versión; promover v1.0.0 solo al cumplir criterios |
| Estrategia de release y ambientes | Flujo de control y rollback documentado | Validar el artefacto, registrar aprobaciones disponibles y publicar la release real |
| Documentación y demostración | README, arquitectura, seguridad, deuda, release y guion | Revisar contenido después de la publicación |

## Bloqueos actuales

1. **Publicación del repositorio:** `incident-hub` fue creado como privado en `dmazariegoso3-oss`. En esta sesión, el conector GitHub identifica el perfil `dmazariegoso3-oss` pero sus instalaciones accesibles muestran una cuenta distinta y no listan ese repositorio. El push local falla porque Windows no tiene credenciales GitHub disponibles. No hay commits ni ramas publicados.
2. **Codespace abierto:** la carpeta remota `incident-hub` no muestra archivos y aparece en modo restringido; no sirve como copia del código local ni como evidencia de ejecución.
3. **Requisito académico:** el PDF original pide Azure Boards y Azure Pipelines. La actualización del usuario confirma un repositorio único, pero no confirma que el ingeniero aceptó sustituir Azure por GitHub. Mantener la configuración de Azure como alternativa documentada hasta obtener esa respuesta.

## Orden de cierre

1. Recuperar publicación autenticada para la cuenta propietaria. Verificar en el repo que estén `main` y la rama de trabajo; conservar el historial local existente.
2. Acordar con el ingeniero qué herramientas sustituyen Azure. Crear el tablero y materializar el CSV con work items reales y vínculos.
3. Separar el historial en seis cambios revisables si la rúbrica exige seis PR independientes; ejecutar CI por PR y dejar la segunda cuenta probar y revisar cada cambio.
4. Registrar al runner Windows y completar una ejecución manual desde Actions.
5. Producir el fallo controlado documentado y su reparación mediante una rama y PR reales.
6. Ejecutar auditoría final, regenerar artefacto, crear tags/releases y completar una demostración reproducible.

Los pasos 2 a 6 dependen de que el punto 1 permita publicar y de la decisión del ingeniero para los requisitos Azure. Las revisiones reales requieren que la segunda cuenta haga sus pruebas y deje su aprobación o comentarios.
