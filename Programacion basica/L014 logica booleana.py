# Pedimos dos valores booleanos al usuario
a = input("Ingrese el primer valor booleano (True/False): ")
b = input("Ingrese el segundo valor booleano (True/False): ")

# Convertimos las cadenas a booleanos reales
a = True if a.lower() == "true" else False
b = True if b.lower() == "true" else False

print("\n--- Resultados de la lógica booleana ---")
print("a AND b =", a and b)   # Verdadero solo si ambos son True
print("a OR b  =", a or b)    # Verdadero si al menos uno es True
print("NOT a   =", not a)     # Niega el valor de a
print("NOT b   =", not b)     # Niega el valor de b

# También podemos probar con números y convertirlos a booleanos
print("\n--- Ejemplo con números convertidos a bool ---")
x = 0       # False en booleano
y = 1       # True en booleano (porque no es cero)

print("bool(x) =", bool(x))
print("bool(y) =", bool(y))
print("bool(x) OR bool(y) =", bool(x) or bool(y))
print("bool(x) AND bool(y) =", bool(x) and bool(y))