from almanaque_flores.modelos import Flor
# Lo mas cambiado esta en almanaque_flores/modelos.py (Ahi se visualiza mas el uso de funciones)
# Crear una flor
rosa = Flor(
    "Rosa", "Rosa spp.", "Rosaceae",
    ["Europa", "Asia"], "Cultivada ampliamente",
    ["rojo", "blanco"]
)

# Acceso a atributos públicos
print(rosa.nombre)
print(rosa.nombre_cientifico)

# Acceso a protegidos (no recomendado, pero posible)
print(rosa._familia)

# Acceso a privados (solo con getters)
print(rosa.get_estado_conservacion())
print(rosa.get_colores())

# Modificar privados con setters
rosa.set_estado_conservacion("En peligro")
rosa.set_colores(["amarillo", "rosado"])

# Mostrar la info actualizada
rosa.mostrar_info()