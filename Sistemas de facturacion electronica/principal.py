from os import name
import interfaz

# Menú principal que da inicio al programa
def menu():
    print("Bienvenido al sistema de facturación.")
    interfaz.realizar_venta()  # Inicia la primera venta
    interfaz.continuar_o_salir()  # Pregunta si desea continuar o salir

# Ejecutar el menú
if name == "_main_":
    menu()