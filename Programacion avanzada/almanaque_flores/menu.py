"""
Módulo menu.py
Proporciona una interfaz de usuario interactiva para el almanaque de flores.
"""

from .almanaque import AlmanaqueFlores
from .modelos import Flor

def menu():
    """
    Función principal que muestra el menú del almanaque y permite
    gestionar flores de manera interactiva.
    """
    almanaque = AlmanaqueFlores()

    # Flores iniciales
    almanaque.agregar_flor(Flor(
        "Rosa", "Rosa spp.", "Rosaceae",
        ["Europa", "Asia", "América del Norte"],
        "Cultivada ampliamente", ["rojo", "blanco", "rosado", "amarillo"]
    ))
    almanaque.agregar_flor(Flor(
        "Tulipán", "Tulipa spp.", "Liliaceae",
        ["Turquía", "Países Bajos", "Asia Central"],
        "Cultivada", ["rojo", "amarillo", "morado", "blanco"]
    ))
    almanaque.agregar_flor(Flor(
        "Loto", "Nelumbo nucifera", "Nelumbonaceae",
        ["India", "China", "Sudeste Asiático"],
        "No amenazada", ["rosa", "blanco"]
    ))

    while True:
        print("\n--- ALMANAQUE DE FLORES ---")
        print("1. Ver todas las flores")
        print("2. Buscar una flor")
        print("3. Agregar una flor")
        print("4. Eliminar una flor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                almanaque.mostrar_flores()
            case "2":
                flor_buscar = input("Ingrese el nombre de la flor: ")
                almanaque.buscar_flor(flor_buscar)
            case "3":
                nombre = input("Ingrese el nombre de la nueva flor: ")
                nombre_cientifico = input("Nombre científico: ")
                familia = input("Familia: ")
                distribucion = input("Distribución (separada por comas): ").split(",")
                estado_conservacion = input("Estado de conservación: ")
                colores = input("Colores (separados por comas): ").split(",")

                nueva_flor = Flor(nombre, nombre_cientifico, familia, distribucion, estado_conservacion, colores)
                almanaque.agregar_flor(nueva_flor)
            case "4":
                flor_eliminar = input("Ingrese el nombre de la flor a eliminar: ")
                almanaque.eliminar_flor(flor_eliminar)
            case "5":
                print("Saliendo del almanaque... ¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")