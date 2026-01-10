print("Hello World")

num1 = 10
num2 = 20

sum_result = num1 + num2
print(sum_result)

print('Dame dos numeros para sumarlos')
print('')
num1 = int(input('Dame el primer numero: '))
num2 = int(input('Dame el segundo numero: '))
suma = num1 + int(num2)

#Formateo de cadenas, orden de los valores
print('La suma de {1} mas {2} es: {0}'.format(suma, num1, num2))