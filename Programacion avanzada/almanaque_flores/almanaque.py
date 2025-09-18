"""
Módulo almanaque.py
Define la clase AlmanaqueFlores, encargada de gestionar un conjunto de flores.
"""

from .normalizador import normalizar_texto

class AlmanaqueFlores:
    """
    Clase que representa un almanaque de flores.

    Métodos:
        agregar_flor(flor): Agrega una flor al almanaque.
        mostrar_flores(): Lista todas las flores guardadas.
        buscar_flor(nombre): Busca y muestra información de una flor por nombre.
        eliminar_flor(nombre): Elimina una flor del almanaque.
    """

    def __init__(self):
        self.flores = {}

    def agregar_flor(self, flor):
        """Agrega una nueva flor al almanaque, validando duplicados."""
        clave = normalizar_texto(flor.nombre)
        if clave in self.flores:
            print("Esa flor ya existe en el almanaque.")
        else:
            self.flores[clave] = flor
            print(f"{flor.nombre} ha sido agregada al almanaque.")

    def mostrar_flores(self):
        """Muestra el listado de todas las flores registradas."""
        if not self.flores:
            print("No hay flores en el almanaque.")
        else:
            print("\nListado de flores en el almanaque:")
            for flor in self.flores.values():
                print("-", flor.nombre)

    def buscar_flor(self, nombre):
        """Busca una flor por nombre (ignora mayúsculas y acentos)."""
        clave = normalizar_texto(nombre)
        if clave in self.flores:
            self.flores[clave].mostrar_info()
        else:
            print("Esa flor no está en el almanaque.")

    def eliminar_flor(self, nombre):
        """Elimina una flor del almanaque si existe."""
        clave = normalizar_texto(nombre)
        if clave in self.flores:
            nombre_real = self.flores[clave].nombre
            del self.flores[clave]
            print(f"{nombre_real} ha sido eliminada.")
        else:
            print("Esa flor no existe en el almanaque.")