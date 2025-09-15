lista = ["uno","dos","tres","cuatro","cinco"] #creamos lista con posiciones asignadas
print(lista) #imprimimos toda la lista
print(lista[0])#imprimimos el primer dato de la lista

lista.append("seis") #añade al final otro elemento a la lista
print(lista)

lista.insert(0,"cero") #inserta un valor a la lista en el indice que quiera
print(lista)

lista2 = ["siete", "ocho", "nueve"]
lista.extend(lista2) #combina las listas
print(lista)

lista.pop() #elimina el ultimo valor de la lista
print(lista)

lista.pop(3) #elimina el valor de la lista en el indice que quiera
print(lista)

lista.remove("dos") #remueve lo puesto entre parentesis de la lista
print(lista)

numero = lista.index("cuatro") #estrae el valor indicado de la lista
print(lista)