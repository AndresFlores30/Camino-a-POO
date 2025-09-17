flores = {
    "Rosa": {
        "nombre cientifico": "Rosa spp.",
        "familia": "Rosaceae",
        "distribucion": ["Europa", "Asia", "América del Norte"],
        "estado_conservacion": "Cultivada ampliamente",
        "colores": ["rojo", "blanco", "rosado", "amarillo"]
    },
    "Tulipán": {
        "nombre cientifico": "Tulipa spp.",
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

# Buscar una flor
flor_buscar = input("Indique la flor a buscar: ")
print(f"\n Información de la flor: {flor_buscar}")
print(f"Nombre científico: {flores[flor_buscar]['nombre_cientifico']}")
print(f"Estado de conservación: {flores[flor_buscar]['estado_conservacion']}")

# Agregar una nueva flor al almanaque
flores["Girasol"] = {
    "nombre_cientifico": "Helianthus annuus",
    "familia": "Asteraceae",
    "distribucion": ["América del Norte", "América Central"],
    "estado_conservacion": "Cultivada",
    "colores": ["amarillo", "marrón"]
}
print("\n Diccionario actualizado con 'Girasol' ")

# Eliminar una flor
flor_eliminar = input("Indique la flor a eliminar: ")
del flores[flor_eliminar]
print(f"\n--- Diccionario después de eliminar '{flor_eliminar}' ---")
print(flores)