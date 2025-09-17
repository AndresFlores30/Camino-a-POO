# Pedimos un entero
num_entero = int(input("Ingrese un número entero: "))
# Pedimos un decimal (float)
num_float = float(input("Ingrese un número decimal: "))
# Pedimos un booleano (True/False, se convierte a bool)
num_bool = input("Ingrese un valor booleano (True/False): ")
num_bool = True if num_bool.lower() == "true" else False
# Pedimos un número complejo (ej: 3+2j)
num_complex = complex(input("Ingrese un número complejo (ej: 3+2j): "))

print("\n--- Resultados de las sumas ---")
print("Entero + Decimal =", num_entero + num_float)
print("Entero + Booleano =", num_entero + num_bool)
print("Decimal + Booleano =", num_float + num_bool)
print("Entero + Complejo =", num_entero + num_complex)
print("Decimal + Complejo =", num_float + num_complex)