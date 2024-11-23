
import productos
import factura

# Función para realizar la venta
def realizar_venta():
    productos_comprados = []
    
    while True:
        # Selección de categoría
        while True:
            categoria = input("\nSelecciona una categoría (Línea Blanca, Pequeños Electrodomésticos, Entretenimiento, Aires Acondicionados): ").title()
            if categoria in productos.catalogo:
                break  # Si la categoría es válida, salimos del bucle
            else:
                print("Categoría no válida. Intenta de nuevo.")
        
        while True:
            # Mostrar los productos disponibles en la categoría seleccionada
            print("\nProductos disponibles:")
            for p in productos.catalogo[categoria]:
                print(f"Código: {p['codigo']} - {p['nombre']} - Precio: ${p['precio']}")
            
            # Selección de código de producto
            try:
                codigo = int(input("Ingresa el código del producto (0 para finalizar): "))
                if codigo == 0:
                    break  # Si el código es 0, finaliza la compra
                producto = productos.obtener_producto(codigo, categoria)
                if producto:
                    cantidad = int(input(f"¿Cuántos {producto['nombre']} deseas comprar? "))
                    productos_comprados.append({"nombre": producto['nombre'], "cantidad": cantidad, "precio": producto['precio']})
                else:
                    print("Código no válido. Intenta de nuevo.")
            except ValueError:
                print("Por favor, ingresa un código válido.")
        
        if productos_comprados:
            # Generar la factura
            factura.generar_factura(productos_comprados)
            break  # Sale del bucle de venta
        else:
            print("No se seleccionaron productos. Reiniciando la venta.")
            continue  # Reinicia la venta si no se seleccionaron productos

def continuar_o_salir():
    while True:
        opcion = input("\n¿Deseas hacer una nueva compra (s/n)? ").lower()
        if opcion == 's':
            realizar_venta()  # Inicia una nueva venta
        elif opcion == 'n':
            print("Gracias por tu compra. ¡Hasta pronto!")
            break  # Sale del programa
        else:
            print("Opción no válida. Ingresa 's' para sí o 'n' para no.")