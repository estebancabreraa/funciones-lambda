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
                c = cero(alpha, x)
                print('\nResultado: ' + str(c(alpha, x)))
            elif second_option == '2':
                c = cero(beta, x)
                print('\nResultado: ' + str(c(beta, x)))
        if option == '2':
            print('Uno(f, x)')
            print(functions)
            second_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if second_option == '1':
                u = uno(alpha, x)
                print('\nResultado: ' + str(u(alpha, x)))
            elif second_option == '2':
                u = uno(beta, x)
                print('\nResultado: ' + str(u(beta, x)))
        if option == '3':
            print('Dos(f, x)')
            print(functions)
            second_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if second_option == '1':
                d = dos(alpha, x)
                print('\nResultado: ' + str(d(alpha, x)))
            elif second_option == '2':
                d = dos(beta, x)
                print('\nResultado: ' + str(d(beta, x)))
        if option == '4':
            print('Tres(f, x)')
            print(functions)
            second_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if second_option == '1':
                t = tres(alpha, x)
                print('\nResultado: ' + str(t(alpha, x)))
            elif second_option == '2':
                t = tres(beta, x)
                print('\nResultado: ' + str(t(beta, x)))
    except:
        print('Revise los valores ingresados.')

