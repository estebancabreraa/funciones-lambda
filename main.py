from lambda_func import *

exit = False
header = '''
###################################################
#                   Proyecto 2 TC                 # 
###################################################
                Por: Esteban Cabrera A.
                Carnet: 17781.
'''

menu = '''
####################################################
Menu:
    1. Cero(f, x).
    2. Uno(f, x).
    3. Dos(f, x).
    4. Tres(f, x).
'''

functions = '''
Funciones:
    1. Alpha.
    2. Beta.
'''

print(header)

while not exit:
    print(menu)
    option = input('Seleccione una opcion: ')
    try:
        if option == '1':
            print('Cero(f, x)')
            print(functions)
            second_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if second_option == '1':
                res = cero(alpha, x)
                print('\nResultado: ' + str(res))
            elif second_option == '2':
                res = cero(beta, x)
                print('\nResultado: ' + str(res))
        if option == '2':
            print('Uno(f, x)')
            print(functions)
            second_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if second_option == '1':
                res = uno(alpha, x)
                print('\nResultado: ' + str(res))
            elif second_option == '2':
                res = uno(beta, x)
                print('\nResultado: ' + str(res))
        if option == '3':
            print('Dos(f, x)')
            print(functions)
            second_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if second_option == '1':
                res = dos(alpha, x)
                print('\nResultado: ' + str(res))
            elif second_option == '2':
                res = dos(beta, x)
                print('\nResultado: ' + str(res))
        if option == '4':
            print('Tres(f, x)')
            print(functions)
            second_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if second_option == '1':
                res = tres(alpha, x)
                print('\nResultado: ' + str(res))
            elif second_option == '2':
                res = tres(beta, x)
                print('\nResultado: ' + str(res))
    except:
        print('Revise los valores ingresados.')

