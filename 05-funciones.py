import os

def funcion1():
    print('Esta es la funcion 1')

def funcion2():
    # print('Esta es la funcion 2')
    # os.system('cls')  Solo funciona en windows 
    os.system('clear') # Funciona en mac y linux

def funcion3():
    print('Esta es la funcion 3')

def main():
    funcion1()
    #funcion2()
    funcion3()

if __name__ == '__main__':
    main()