# Función para generar la factura
def generar_factura(productos_comprados):
    subtotal = sum(p['precio'] * p['cantidad'] for p in productos_comprados)
    iva = subtotal * 0.19
    total = subtotal + iva

    # Mostrar la factura en pantalla
    print("\nFactura:")
    for p in productos_comprados:
        print(f"{p['nombre']} - {p['cantidad']} x ${p['precio']} = ${p['precio'] * p['cantidad']}")
    
    print(f"\nSubtotal: ${subtotal}")
    print(f"IVA (19%): ${iva}")
    print(f"Total: ${total}")