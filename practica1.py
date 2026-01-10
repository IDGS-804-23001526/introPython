"""Operacion de multiplicacion de a x b utilizando sumas
a = 3
b = 4
salida = 3 + 3 + 3 + 3 = 12
"""

a = 3
b = 4
res = ''

while b > 0:
    res+= str(a) + '+'
    b-=1

print(res + ' = ' + str(a))