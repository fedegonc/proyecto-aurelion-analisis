# Documentación del Proyecto Aurelion

## 🎯 Problema

¿Qué factores están asociados a que un cliente vuelva a comprar, y cómo
podemos aumentar su frecuencia de compra?


## ✅ Solución

Pipeline de análisis descriptivo con **pandas** que integra 4 tablas (clientes, productos, ventas, detalle_ventas) para visualizar:


● Detectar clientes que compraron una sola vez vs recurrentes.
● Identificar patrones de recurrencia por producto, categoría, medio de pago, ciudad.
● Permite definir campañas de retención o cross-selling.

Datos involucrados:
● Clientes (fecha de alta, ciudad)
● Ventas (fecha, id_cliente, medio de pago)
● Detalle de ventas (productos adquiridos)

## 💻 Pseudocódigo

```
INICIO
   ↓
CARGAR datos desde Excel (clientes, ventas, detalle_ventas, productos)
CALCULAR métricas por cliente (num_compras, importe_total, tipo)
   ↓
MIENTRAS verdadero:
   ↓
   MOSTRAR menú principal con opciones 1-6 y 0
   ↓
   LEER opción del usuario
   ↓
   SI opción == 1:
      MOSTRAR resumen general (total clientes, ventas, importe)
   SI NO, SI opción == 2:
      MOSTRAR top 10 clientes recurrentes ordenados por importe
   SI NO, SI opción == 3:
      MOSTRAR top 10 productos más vendidos y resumen por categoría
   SI NO, SI opción == 4:
      MOSTRAR ranking de ciudades por % de recurrencia
   SI NO, SI opción == 5:
      MOSTRAR distribución de ventas por medio de pago
   SI NO, SI opción == 6:
      EXPORTAR métricas a archivos CSV en carpeta output/
   SI NO, SI opción == 0:
      MOSTRAR mensaje de despedida
      SALIR del bucle
   SI NO:
      MOSTRAR mensaje de error "Opción inválida"
   ↓
   ESPERAR que usuario presione ENTER
   ↓
FIN MIENTRAS
   ↓
FIN
```

**Datos:** 100 clientes, 100 productos, 120 transacciones, 343 líneas de detalle en 4 ciudades de Córdoba.

---

## 📝 Instrucciones y Prompts

Para ver las instrucciones dadas a Copilot durante el desarrollo, consultar: **`Instrucciones.md`**
