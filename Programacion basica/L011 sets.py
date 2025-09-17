# Conjunto de flores americanas
flores_americanas = {"Rosa", "Girasol", "Margarita", "Orquídea"}
# Conjunto de flores asiáticas (un solo elemento)
flores_asiaticas = {"Loto"}

print(flores_americanas)
print(flores_asiaticas)

# Agregamos nuevas flores
flores_americanas.add("Hibisco")
# Intentamos agregar una flor repetida (no se duplica)
flores_americanas.add("Rosa")

# Eliminamos una flor
flores_americanas.remove("Margarita")
print(flores_americanas)

# Intentamos descartar una flor que no está (no da error)
flores_asiaticas.discard("Cerezo Japonés")
print(flores_asiaticas)

# Cantidad de flores en cada set
cant_americanas = len(flores_americanas)
cant_asiaticas = len(flores_asiaticas)
print("La cantidad de flores americanas es:", cant_americanas)
print("La cantidad de flores asiáticas es:", cant_asiaticas)

# Orden alfabético dentro del set
primera_flor = min(flores_americanas)
ultima_flor = max(flores_americanas)
print("La primera flor (alfabéticamente) es:", primera_flor)
print("La última flor (alfabéticamente) es:", ultima_flor)

# frozenset es la versión inmutable y hashable de un set
flores_favoritas = frozenset(["Tulipán", "Rosa"])
print(flores_favoritas)