# Catálogo de productos por categorías
catalogo = {
    "Línea Blanca": [
        {"codigo": 1, "nombre": "Refrigerador", "precio": 1000},
        {"codigo": 2, "nombre": "Lavadora", "precio": 800},
        {"codigo": 3, "nombre": "Secadora", "precio": 600},
    ],
    "Pequeños Electrodomésticos": [
        {"codigo": 4, "nombre": "Licuadora", "precio": 100},
        {"codigo": 5, "nombre": "Cafetera", "precio": 150},
        {"codigo": 6, "nombre": "Tostadora", "precio": 50},
    ],
    "Entretenimiento": [
        {"codigo": 7, "nombre": "Televisor", "precio": 500},
        {"codigo": 8, "nombre": "Sistema de sonido", "precio": 300},
    ],
    "Aires Acondicionados": [
        {"codigo": 9, "nombre": "Aire acondicionado", "precio": 1200},
    ]
}

# Función para obtener el producto por código
def obtener_producto(codigo, categoria):
    for prod in catalogo[categoria]:
        if prod['codigo'] == codigo:
            return prod
    return None  # Producto no encontrado