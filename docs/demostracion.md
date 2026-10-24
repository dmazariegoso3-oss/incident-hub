# Guion de defensa

1. Ejecutar `python backend/app.py` y abrir localhost:8000.
2. Crear un incidente de red con prioridad CRITICA y usuario de demostración.
3. Abrir detalle: explicar ID, fecha, estado NUEVO e historial.
4. Asignar un técnico y pasar a ASIGNADO; luego EN_PROCESO.
5. Agregar comentario de diagnóstico; mostrar actor y fecha.
6. Filtrar por prioridad, categoría, estado y técnico; limpiar filtros.
7. Resolver y cerrar. Mostrar actualización de indicadores e historial.
8. Reiniciar servidor y comprobar persistencia.
9. Ejecutar pruebas y explicar rechazo de transiciones inválidas.
10. Una vez publicadas las evidencias: recorrer issue → rama → commit → PR → revisión → CI → artefacto → versión. Mostrar fallo/corrección y job del runner real.

Preguntas previsibles: por qué SQLite (simple, persistente, sin servicio adicional); qué protege una consulta parametrizada; por qué main se protege; diferencia entre artefacto y release; SemVer; cómo se evita exponer secretos; qué deuda queda antes de producción.
