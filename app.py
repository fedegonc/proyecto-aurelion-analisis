# Análisis de Ventas - Proyecto Aurelion

# =======================
# 📦 IMPORTS Y CONFIG
# =======================

import pandas as pd
from pathlib import Path

# =======================
# 🔧 FUNCIONES AUXILIARES
# =======================

def cargar_datos():
    """Carga y prepara los datos"""
    print("\n🔄 Cargando datos...")
    clientes = pd.read_excel("data/raw/clientes.xlsx")
    ventas = pd.read_excel("data/raw/ventas.xlsx")
    detalle_ventas = pd.read_excel("data/raw/detalle_ventas.xlsx")
    productos = pd.read_excel("data/raw/productos.xlsx")
    
    clientes['fecha_alta'] = pd.to_datetime(clientes['fecha_alta'])
    ventas['fecha'] = pd.to_datetime(ventas['fecha'])
    
    df = (detalle_ventas
          .merge(productos[['id_producto', 'categoria']], on='id_producto')
          .merge(ventas[['id_venta', 'fecha', 'id_cliente', 'medio_pago']], on='id_venta')
          .merge(clientes[['id_cliente', 'nombre_cliente', 'ciudad']], on='id_cliente'))
    
    print("✅ Datos cargados correctamente\n")
    return df, clientes

def calcular_metricas_cliente(df, clientes):
    """Calcula métricas por cliente"""
    metricas = df.groupby('id_cliente').agg({
        'id_venta': 'nunique',
        'importe': 'sum',
        'fecha': ['min', 'max'],
        'categoria': 'nunique'
    }).reset_index()
    
    metricas.columns = ['id_cliente', 'num_compras', 'importe_total', 
                        'primera_compra', 'ultima_compra', 'categorias']
    
    metricas['tipo'] = metricas['num_compras'].apply(
        lambda x: 'recurrente' if x > 1 else 'unica_compra'
    )
    
    metricas = metricas.merge(
        clientes[['id_cliente', 'nombre_cliente', 'ciudad']], on='id_cliente'
    )
    
    return metricas

# =======================
# 📊 FUNCIONES DE ANÁLISIS
# =======================

def mostrar_resumen_general(df, metricas_cliente):
    """Opción 1: Resumen general"""
    print("\n" + "="*60)
    print("📊 RESUMEN GENERAL")
    print("="*60)
    
    total_clientes = metricas_cliente['id_cliente'].nunique()
    recurrentes = (metricas_cliente['tipo'] == 'recurrente').sum()
    unicos = (metricas_cliente['tipo'] == 'unica_compra').sum()
    
    print(f"\n👥 Total de clientes: {total_clientes}")
    print(f"   ├─ Recurrentes: {recurrentes} ({recurrentes/total_clientes*100:.1f}%)")
    print(f"   └─ Única compra: {unicos} ({unicos/total_clientes*100:.1f}%)")
    
    print(f"\n💰 Ventas totales: {df['id_venta'].nunique()}")
    print(f"💵 Importe total: ${df['importe'].sum():,.0f}")
    print(f"🎯 Ticket promedio: ${df.groupby('id_venta')['importe'].sum().mean():,.0f}")
    
    print(f"\n📦 Total productos: {df['id_producto'].nunique()}")
    print(f"🏷️ Categorías: {df['categoria'].nunique()}")
    print(f"🏙️ Ciudades: {df['ciudad'].nunique()}")

def mostrar_clientes_recurrentes(metricas_cliente):
    """Opción 2: Análisis de clientes recurrentes"""
    print("\n" + "="*60)
    print("👥 ANÁLISIS DE CLIENTES RECURRENTES")
    print("="*60)
    
    recurrentes = metricas_cliente[metricas_cliente['tipo'] == 'recurrente'].sort_values('importe_total', ascending=False)
    
    print(f"\n🔝 Top 10 clientes recurrentes por importe:")
    print(recurrentes[['nombre_cliente', 'ciudad', 'num_compras', 'importe_total']].head(10).to_string(index=False))
    
    print(f"\n📈 Estadísticas de recurrentes:")
    print(f"   ├─ Compras promedio: {recurrentes['num_compras'].mean():.1f}")
    print(f"   ├─ Importe promedio: ${recurrentes['importe_total'].mean():,.0f}")
    print(f"   └─ Categorías promedio: {recurrentes['categorias'].mean():.1f}")

def mostrar_productos(df):
    """Opción 3: Análisis de productos"""
    print("\n" + "="*60)
    print("📦 ANÁLISIS DE PRODUCTOS")
    print("="*60)
    
    productos = df.groupby(['nombre_producto', 'categoria']).agg({
        'cantidad': 'sum',
        'id_cliente': 'nunique',
        'importe': 'sum'
    }).reset_index()
    
    productos.columns = ['producto', 'categoria', 'total_vendido', 'clientes_unicos', 'importe_total']
    productos = productos.sort_values('total_vendido', ascending=False)
    
    print(f"\n🏆 Top 10 productos más vendidos:")
    print(productos[['producto', 'categoria', 'total_vendido', 'clientes_unicos']].head(10).to_string(index=False))
    
    print(f"\n📊 Por categoría:")
    por_categoria = df.groupby('categoria').agg({
        'cantidad': 'sum',
        'importe': 'sum'
    }).sort_values('cantidad', ascending=False)
    print(por_categoria.to_string())

def mostrar_ciudades(metricas_cliente):
    """Opción 4: Análisis por ciudad"""
    print("\n" + "="*60)
    print("🏙️ ANÁLISIS POR CIUDAD")
    print("="*60)
    
    ciudades = metricas_cliente.groupby('ciudad').agg({
        'id_cliente': 'count',
        'importe_total': 'mean',
        'tipo': lambda x: (x == 'recurrente').sum()
    }).reset_index()
    
    ciudades.columns = ['ciudad', 'total_clientes', 'ticket_promedio', 'recurrentes']
    ciudades['pct_recurrentes'] = (ciudades['recurrentes'] / ciudades['total_clientes'] * 100)
    ciudades = ciudades.sort_values('pct_recurrentes', ascending=False)
    
    print(f"\n📍 Ranking de ciudades por % de recurrencia:")
    print(ciudades.to_string(index=False))

def mostrar_medios_pago(df):
    """Opción 5: Análisis de medios de pago"""
    print("\n" + "="*60)
    print("💳 ANÁLISIS DE MEDIOS DE PAGO")
    print("="*60)
    
    pagos = df.groupby('medio_pago').agg({
        'id_venta': 'nunique',
        'importe': ['sum', 'mean']
    }).reset_index()
    
    pagos.columns = ['medio_pago', 'num_ventas', 'importe_total', 'ticket_promedio']
    pagos['pct_ventas'] = (pagos['num_ventas'] / pagos['num_ventas'].sum() * 100)
    pagos = pagos.sort_values('num_ventas', ascending=False)
    
    print(f"\n💰 Resumen por medio de pago:")
    print(pagos.to_string(index=False))

def exportar_datos(df, metricas_cliente):
    """Opción 6: Exportar datos"""
    print("\n" + "="*60)
    print("💾 EXPORTAR DATOS")
    print("="*60)
    
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Métricas por producto
    productos = df.groupby(['nombre_producto', 'categoria']).agg({
        'cantidad': 'sum',
        'id_cliente': 'nunique',
        'importe': 'sum'
    }).reset_index()
    productos.columns = ['producto', 'categoria', 'total_vendido', 'clientes_unicos', 'importe_total']
    
    # Métricas por ciudad
    ciudades = metricas_cliente.groupby('ciudad').agg({
        'id_cliente': 'count',
        'importe_total': 'mean',
        'tipo': lambda x: (x == 'recurrente').sum()
    }).reset_index()
    ciudades.columns = ['ciudad', 'total_clientes', 'ticket_promedio', 'recurrentes']
    ciudades['pct_recurrentes'] = (ciudades['recurrentes'] / ciudades['total_clientes'] * 100)
    
    # Exportar
    metricas_cliente.to_csv(output_dir / 'metricas_cliente.csv', index=False)
    productos.to_csv(output_dir / 'metricas_producto.csv', index=False)
    ciudades.to_csv(output_dir / 'metricas_ciudad.csv', index=False)
    
    print("\n✅ Archivos exportados:")
    print("   ├─ metricas_cliente.csv")
    print("   ├─ metricas_producto.csv")
    print("   └─ metricas_ciudad.csv")
    print(f"\n📁 Ubicación: {output_dir.absolute()}")

# =======================
# 🧭 FLUJO PRINCIPAL
# =======================

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🎯 SISTEMA DE ANÁLISIS DE VENTAS - PROYECTO AURELION")
    print("="*60)
    print("\n1. 📊 Resumen General")
    print("2. 👥 Clientes Recurrentes")
    print("3. 📦 Análisis de Productos")
    print("4. 🏙️ Análisis por Ciudad")
    print("5. 💳 Medios de Pago")
    print("6. 💾 Exportar Datos")
    print("0. ❌ Salir")
    print("\n" + "="*60)

def main():
    """Función principal"""
    df, clientes = cargar_datos()
    metricas_cliente = calcular_metricas_cliente(df, clientes)
    
    while True:
        mostrar_menu()
        opcion = input("\n👉 Seleccione una opción: ").strip()
        
        if opcion == '1':
            mostrar_resumen_general(df, metricas_cliente)
        elif opcion == '2':
            mostrar_clientes_recurrentes(metricas_cliente)
        elif opcion == '3':
            mostrar_productos(df)
        elif opcion == '4':
            mostrar_ciudades(metricas_cliente)
        elif opcion == '5':
            mostrar_medios_pago(df)
        elif opcion == '6':
            exportar_datos(df, metricas_cliente)
        elif opcion == '0':
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
        
        input("\n⏸️ Presione ENTER para continuar...")

if __name__ == "__main__":
    main()
