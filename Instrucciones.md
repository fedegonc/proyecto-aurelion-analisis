# 📝 Instrucciones Dadas a Copilot

## Proyecto: Sistema de Análisis de Ventas - Aurelion

---

## 💬 Ejemplo de Prompt Didáctico

```
Asume el rol de un analista de datos junior en una empresa de retail. 
Tienes 4 archivos Excel con datos de ventas y necesitas responder:
¿Qué clientes compran más de una vez y por qué?

Crea un script en Python que:
1. Cargue los datos desde data/raw/
2. Calcule cuántas veces compró cada cliente
3. Identifique qué productos, ciudades y medios de pago prefieren los recurrentes
4. Muestre un menú interactivo para explorar los resultados
5. Exporte las métricas a CSV

Usa pandas, mantén el código simple.
```

---

## ✅ Instrucciones Aceptadas

1. **Calcular AOV por cliente** → `calcular_metricas_cliente()`
2. **Identificar clientes VIP (percentil 90)** → Lógica en análisis recurrentes
3. **Análisis por medio de pago** → `mostrar_medios_pago()` - Opción 5
4. **Ranking de ciudades por recurrencia** → `mostrar_ciudades()` - Opción 4
5. **Exportar métricas a CSV** → `exportar_datos()` - Opción 6
6. **Top productos más vendidos** → `mostrar_productos()` - Opción 3
7. **Clientes recurrentes vs únicos** → Columna `tipo` en métricas
8. **Menú interactivo con ciclo** → `main()` con `while True`

---

## ❌ Instrucciones Rechazadas

1. **Machine Learning para predicción** → Dataset pequeño (120 transacciones)
2. **Gráficos con Plotly** → Mantener simplicidad en consola
3. **Base de datos SQL** → Archivos Excel suficientes (< 500 registros)
4. **CRUD de clientes desde menú** → Sistema de análisis, no gestión

---

## 🔄 Instrucciones Modificadas

1. **Tendencia de precios**: Diaria → Mensual (dataset pequeño)
2. **Clientes recurrentes**: Todos → Top 10 (legibilidad)
3. **Formato de salida**: Simple → Con emojis y árbol visual
4. **Carga de datos**: Múltiple → Una sola vez al inicio

---

## 🎯 Lecciones Aprendidas

1. **Definir rol**: "Analista junior" establece nivel de complejidad
2. **Pregunta de negocio**: "¿Por qué vuelven?" > "Haz análisis"
3. **Simplicidad**: Rechazar ML/APIs cuando no agregan valor
4. **Especificar tecnología**: "Usa pandas" evita librerías complejas
