# --- MUTABLES, INMUTABLES Y HASHABLES ---

# INMUTABLE: un string (no se puede cambiar su contenido directamente)
flor = "Rosa"
print("String original:", flor)

# Intentar modificar da error
# flor[0] = "M"  # Esto daría un error porque los strings son inmutables

# MUTABLE: una lista (sí se puede cambiar)
flores = ["Rosa", "Tulipán", "Girasol"]
print("\nLista original:", flores)

# Cambiamos un valor dentro de la lista
flores[1] = "Margarita"
print("Lista modificada:", flores)


# HASHABLE: puede ser clave en un diccionario
# Los strings son hashables
colores = {"Rosa": "Rojo", "Tulipán": "Amarillo"}
print("\nDiccionario con strings (hashables):", colores)

# Una lista NO es hashable → no puede ser clave
# colores[["Margarita", "Blanca"]] = "Blanco"  # Esto daría error

# Una tupla SÍ es hashable → puede ser clave
colores[("Margarita", "Blanca")] = "Blanco"
print("Diccionario con tupla (hashable):", colores)