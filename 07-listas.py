"""
    Una lista es una secuencia de elementos
    se crea con un []
"""

lista1 = ["Dario", 33, 9.5, True, "German", 20.8]

print(lista1)             # Imprime toda la lista
print(lista1[:])          # Imprime toda la lista
print(lista1[2])          # Imprime el elemento en la posicion 2
print(lista1[-1])         # Imprime el elemento en la ultima posicion
print(lista1[0:3])        # Imprime los elementos desde la posicion 0 hasta la 3
print(lista1[3:])         # Imprime los elementos desde la posicion 3 hasta el final

lista1.append("Vargas")
print(lista1)

lista1.insert(2, "Nadia")
print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(33) # Elimina el elemento 33
print(lista1)
lista1.pop() # Elimina el ultimo elemento
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2
print(lista3)

print(lista2*4)
lista4 = [2,1,5,4,3]
print(lista4)
lista4.sort() # Ordena la lista
print(lista4)