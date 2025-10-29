# Observaciones de Normalización y Transformaciones

Este documento recopila consideraciones y pendientes detectados durante el análisis exploratorio de los datos.

## Ajustes aplicados o sugeridos

- **Fechas**:
  - Asegurar que todas las columnas de fecha (por ejemplo, `ventas.fecha` y `clientes.fecha_alta`) se conviertan a tipo `datetime64[ns]` para facilitar filtros y cálculos por período.
  - Definir un formato estándar ISO-8601 (`YYYY-MM-DD`) cuando se exporten informes.
- **Importes**:
  - Las métricas monetarias provienen de la tabla `detalle_ventas`. Se recomienda sumar el campo `importe` por `id_venta` para obtener el valor total de cada operación antes de agregaciones mensuales.
- **Identificadores**:
  - Validar unicidad en claves primarias (`id_cliente`, `id_producto`, `id_venta`). No se detectaron duplicados en la carga actual.
- **Ciudades**:
  - Se codificará la ciudad de los clientes según el diccionario establecido en el sistema (`Cordoba: 0`, `Carlos Paz: 1`, `Rio Cuarto: 2`, `Santa Fe: 3`, `Villa Maria: 4`). Mantener este mapeo centralizado para evitar inconsistencias.
- **Unificación de tablas**:
  - Para análisis detallados, unir `ventas` + `detalle_ventas` + `clientes` + `productos` mediante `id_venta`, `id_cliente` e `id_producto`.
  - La vista resultante facilita KPIs por cliente, producto, ciudad y fecha.
- **Columnas categóricas**:
  - Revisar `medio_pago` y `categoria` por posibles valores fuera del catálogo esperado.

## Pendientes futuros

- Generar catálogos maestros (ciudades, medios de pago) para validar entradas nuevas.
- Revisar outliers de `importe` y `precio_unitario` tras unificar la base.
- Documentar reglas de negocio adicionales detectadas durante la exploración.
