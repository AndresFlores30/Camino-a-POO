var1 = "String con comillas dobles" #declaramos variables con comillas dobles
var2 = 'String con comillas simples'#declaramos variables con comillas simples

print(var1); print(var2) #imprimimos las dos variables en una sola linea

frase = '"print()" se utiliza para imprimir valores en la consola' #almacenamos una frase que contenga comillas
print(frase) #imprimimos la frase

nombre = input("Escribe tu nombre: ")
linea = "Tu nombre es: " + nombre

nombre_convertido = nombre.capitalize()
frase_convertida = linea.upper()
frase_final = frase_convertida.lower()

print("Hola", nombre_convertido)
print(frase_convertida)
print(frase_final)