# Diccionario inicial de flores
flores = {
    "Rosa": {
        "nombre_cientifico": "Rosa spp.",
        "familia": "Rosaceae",
        "distribucion": ["Europa", "Asia", "América del Norte"],
        "estado_conservacion": "Cultivada ampliamente",
        "colores": ["rojo", "blanco", "rosado", "amarillo"]
    },
    "Tulipán": {
        "nombre_cientifico": "Tulipa spp.",
        "familia": "Liliaceae",
        "distribucion": ["Turquía", "Países Bajos", "Asia Central"],
        "estado_conservacion": "Cultivada",
        "colores": ["rojo", "amarillo", "morado", "blanco"]
    },
    "Loto": {
        "nombre_cientifico": "Nelumbo nucifera",
        "familia": "Nelumbonaceae",
        "distribucion": ["India", "China", "Sudeste Asiático"],
        "estado_conservacion": "No amenazada",
        "colores": ["rosa", "blanco"]
    }
}

# funciones
def mostrar_flores():
    print("\nListado de flores en el almanaque:")
    for flor in flores:
        print("-", flor)

def buscar_flor():
    flor_buscar = input("Ingrese el nombre de la flor: ")
    if flor_buscar in flores:
        print(f"\nInformación de {flor_buscar}:")
        print("Nombre científico:", flores[flor_buscar]["nombre_cientifico"])
        print("Familia:", flores[flor_buscar]["familia"])
        print("Distribución:", ", ".join(flores[flor_buscar]["distribucion"]))
        print("Estado de conservación:", flores[flor_buscar]["estado_conservacion"])
        print("Colores:", ", ".join(flores[flor_buscar]["colores"]))
    else:
        print("Esa flor no está en el almanaque.")

def agregar_flor():
    nueva_flor = input("Ingrese el nombre de la nueva flor: ")
    if nueva_flor in flores:
        print("Esa flor ya existe en el almanaque.")
    else:
        flores[nueva_flor] = {
            "nombre_cientifico": input("Nombre científico: "),
            "familia": input("Familia: "),
            "distribucion": input("Distribución (separada por comas): ").split(","),
            "estado_conservacion": input("Estado de conservación: "),
            "colores": input("Colores (separados por comas): ").split(",")
        }
        print(f"{nueva_flor} ha sido agregada al almanaque.")

def eliminar_flor():
    flor_eliminar = input("Ingrese el nombre de la flor a eliminar: ")
    if flor_eliminar in flores:
        del flores[flor_eliminar]
        print(f"{flor_eliminar} ha sido eliminada.")
    else:
        print("Esa flor no existe en el almanaque.")

# programa principal
def menu():
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
                mostrar_flores()
            case "2":
                buscar_flor()
            case "3":
                agregar_flor()
            case "4":
                eliminar_flor()
            case "5":
                print("Saliendo del almanaque... ¡Hasta luego! 🌸")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
menu()