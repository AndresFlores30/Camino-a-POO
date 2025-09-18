# clases
class Flor:
    def __init__(self, nombre, nombre_cientifico, familia, distribucion, estado_conservacion, colores):
        self.nombre = nombre
        self.nombre_cientifico = nombre_cientifico
        self.familia = familia
        self.distribucion = distribucion
        self.estado_conservacion = estado_conservacion
        self.colores = colores

    def mostrar_info(self):
        print(f"\nInformación de {self.nombre}:")
        print(f"Nombre científico: {self.nombre_cientifico}")
        print(f"Familia: {self.familia}")
        print(f"Distribución: {', '.join(self.distribucion)}")
        print(f"Estado de conservación: {self.estado_conservacion}")
        print(f"Colores: {', '.join(self.colores)}")


class AlmanaqueFlores:
    def __init__(self):
        self.flores = {}

    def agregar_flor(self, flor):
        if flor.nombre in self.flores:
            print("Esa flor ya existe en el almanaque.")
        else:
            self.flores[flor.nombre] = flor
            print(f"{flor.nombre} ha sido agregada al almanaque.")

    def mostrar_flores(self):
        if not self.flores:
            print("No hay flores en el almanaque.")
        else:
            print("\nListado de flores en el almanaque:")
            for nombre in self.flores:
                print("-", nombre)

    def buscar_flor(self, nombre):
        if nombre in self.flores:
            self.flores[nombre].mostrar_info()
        else:
            print("Esa flor no está en el almanaque.")

    def eliminar_flor(self, nombre):
        if nombre in self.flores:
            del self.flores[nombre]
            print(f"{nombre} ha sido eliminada.")
        else:
            print("Esa flor no existe en el almanaque.")

def menu():
    almanaque = AlmanaqueFlores()

    # Agregamos las flores iniciales
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

menu()