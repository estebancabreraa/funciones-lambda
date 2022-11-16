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
    5. Sucesor(n, f, x).
    6. Suma(a, b, f, x).
    7. Multiplacion(a, b, f, x).
    8. Potencia(a, b, f, x).
    9. Salir.
'''

functions = '''
Funciones:
    1. Alpha.
    2. Beta.
'''

numbers = '''
    1. Cero.
    2. Uno.
    3. Dos.
    4. Tres.
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
        elif option == '2':
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
        elif option == '3':
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
        elif option == '4':
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
        elif option == '5':
            print('Sucesor(n, f, x)')
            print(numbers)
            second_option = input('Escoja n: ')
            if second_option == '1':
                numb1 = cero
            elif second_option == '2':
                numb1 = uno
            elif second_option == '3':
                numb1 = dos
            elif second_option == '4':
                numb1 = tres
            print(functions)
            third_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if third_option == '1':
                res = sucesor(numb1)(alpha)(x)
                print('\nResultado: ' + str(res))
            elif third_option == '2':
                res = sucesor(numb1)(beta)(x)
                print('\nResultado: ' + str(res))
        elif option == '6':
            print('Suma(a, b, f, x)')
            print(numbers)
            second_option = input('Escoja a: ')
            if second_option == '1':
                numb1 = cero
            elif second_option == '2':
                numb1 = uno
            elif second_option == '3':
                numb1 = dos
            elif second_option == '4':
                numb1 = tres
            print(numbers)
            second_option = input('Escoja b: ')
            if second_option == '1':
                numb2 = cero
            elif second_option == '2':
                numb2 = uno
            elif second_option == '3':
                numb2 = dos
            elif second_option == '4':
                numb2 = tres
            print(functions)
            third_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if third_option == '1':
                res = suma(numb1)(numb2)(alpha)(x)
                print('\nResultado: ' + str(res))
            elif third_option == '2':
                res = suma(numb1)(numb2)(beta)(x)
                print('\nResultado: ' + str(res))
        elif option == '7':
            print('Multiplicacion(a, b, f, x)')
            print(numbers)
            second_option = input('Escoja a: ')
            if second_option == '1':
                numb1 = cero
            elif second_option == '2':
                numb1 = uno
            elif second_option == '3':
                numb1 = dos
            elif second_option == '4':
                numb1 = tres
            print(numbers)
            second_option = input('Escoja b: ')
            if second_option == '1':
                numb2 = cero
            elif second_option == '2':
                numb2 = uno
            elif second_option == '3':
                numb2 = dos
            elif second_option == '4':
                numb2 = tres
            print(functions)
            third_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if third_option == '1':
                res = multiplicacion(numb1)(numb2)(alpha)(x)
                print('\nResultado: ' + str(res))
            elif third_option == '2':
                res = multiplicacion(numb1)(numb2)(beta)(x)
                print('\nResultado: ' + str(res))
        elif option == '8':
            print('Potencia(a, b, f, x)')
            print(numbers)
            second_option = input('Escoja a: ')
            if second_option == '1':
                numb1 = cero
            elif second_option == '2':
                numb1 = uno
            elif second_option == '3':
                numb1 = dos
            elif second_option == '4':
                numb1 = tres
            print(numbers)
            second_option = input('Escoja b: ')
            if second_option == '1':
                numb2 = cero
            elif second_option == '2':
                numb2 = uno
            elif second_option == '3':
                numb2 = dos
            elif second_option == '4':
                numb2 = tres
            print(functions)
            third_option = input('Escoja la funcion f: ')
            x = int(input('Ingrese el valor de x: '))
            if third_option == '1':
                res = potencia(dos)(tres)(alpha)(x)
                print('\nResultado: ' + str(res))
            elif third_option == '2':
                res = potencia(dos)(tres)(alpha)(x)
                print('\nResultado: ' + str(res))
        elif option == '9':
            exit = True
        else:
            print('La opcion seleccionada no existe.')
    except:
        print('Revise los valores ingresados.')

