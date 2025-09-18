"""
Módulo modelos.py
Contiene las clases Planta y Flor, que representan la jerarquía principal
del almanaque de flores.
"""

class Planta:
    """
    Clase base que representa una planta genérica.

    Atributos:
        nombre (str): Nombre común de la planta (público).
        _familia (str): Familia botánica de la planta (protegido).
        _distribucion (list): Lugares donde se distribuye (protegido).
        __estado_conservacion (str): Estado de conservación (privado).
    """

    def __init__(self, nombre, familia, distribucion, estado_conservacion):
        self.nombre = nombre
        self._familia = familia
        self._distribucion = distribucion
        self.__estado_conservacion = estado_conservacion

    def get_estado_conservacion(self):
        """Devuelve el estado de conservación de la planta."""
        return self.__estado_conservacion

    def set_estado_conservacion(self, nuevo_estado):
        """Actualiza el estado de conservación de la planta."""
        self.__estado_conservacion = nuevo_estado

    def mostrar_info(self):
        """Muestra toda la información disponible de la planta."""
        print(f"Nombre: {self.nombre}")
        print(f"Familia: {self._familia}")
        print(f"Distribución: {', '.join(self._distribucion)}")
        print(f"Estado de conservación: {self.__estado_conservacion}")


class Flor(Planta):
    """
    Clase que representa una flor, heredando de Planta.

    Atributos adicionales:
        nombre_cientifico (str): Nombre científico de la flor (público).
        __colores (list): Colores característicos de la flor (privado).
    """

    def __init__(self, nombre, nombre_cientifico, familia, distribucion, estado_conservacion, colores):
        super().__init__(nombre, familia, distribucion, estado_conservacion)
        self.nombre_cientifico = nombre_cientifico
        self.__colores = colores

    def get_colores(self):
        """Devuelve los colores de la flor."""
        return self.__colores

    def set_colores(self, nuevos_colores):
        """Actualiza los colores de la flor."""
        self.__colores = nuevos_colores

    def mostrar_info(self):
        """Muestra la información completa de la flor, incluyendo colores y nombre científico."""
        super().mostrar_info()
        print(f"Nombre científico: {self.nombre_cientifico}")
        print(f"Colores: {', '.join(self.__colores)}")