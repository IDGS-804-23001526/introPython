"""
    Operacion de multiplicacion de a x b utilizando sumas
    a = 3
    b = 4
    salida = 3 + 3 + 3 + 3 = 12
"""

a = 3
b = 4
cont = ''
suma_total = 0

while b > 0:
    suma_total+= a
    cont+= str(a) + '+'
    b-=1

print(cont + ' = ' + str(suma_total))