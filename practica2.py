'''
    Crear un programa que permita realizar las operaciones basicas +, -, *, /
    Utilizando un funciones para cada operacion y un menu principal para 
    desplegar y elegir que operacion realizar
'''

def suma():
    a = int(input('Dame el primer numero: '))
    b = int(input('Dame el segundo numero: '))
    print (a + b)

def resta():
    a = int(input('Dame el primer numero: '))
    b = int(input('Dame el segundo numero: '))
    print (a - b)

def multiplicacion():
    a = int(input('Dame el primer numero: '))
    b = int(input('Dame el segundo numero: '))
    print (a * b)

def division():
    a = int(input('Dame el primer numero: '))
    b = int(input('Dame el segundo numero: '))
    print (a / b)

def main():
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    opcion = int(input('Elige una opcion: '))

    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    else:
        print('Opcion no valida')

main()