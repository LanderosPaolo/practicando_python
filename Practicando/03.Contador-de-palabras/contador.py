# Creamos las funciones para los distintos casos

# Funcion para contar cantidad de palabras en el texto
def contador_palabras(texto):
    # Separamos el texto en palabras
    texto = texto.split()
    # imprimimos la cantidad de de palabras en el texto
    cantidad_palabras = len(texto)
    if cantidad_palabras == 1:
        print(f'\nEl texto contiene "{cantidad_palabras}" palabra')
    else:
        print(f'\nEl texto contiene "{cantidad_palabras}" palabras')

# Funcion para contar cantidad de letras en el texto
def contador_letras(texto):
    cantidad_letras = sum(c.isalpha() for c in texto)
    if cantidad_letras == 1:
        print(f'\nEl texto contiene "{cantidad_letras}" letra')
    else:
        print(f'\nEl texto contiene "{cantidad_letras}" letras')

while True:
    try:
        while True:
            try:
                eleccion = int(input('''
Que deseas hacer?
[1]: Contar cantidad de palabras.
[2]: Contar cantidad de letras.
[3]: Salir.
-->: '''))
                break
                
            except ValueError:
                print('\n--> Has ingresado algo que no es un número, por favor, intenta de nuevo. <--')

        if eleccion == 1:
            texto = input('\nQue texto quieres analizar?: ')
            contador_palabras(texto)

        elif eleccion == 2:
            texto = input('\nQue texto quieres analizar?: ')
            contador_letras(texto)

        elif eleccion == 3:
            print('\n¡Vuelve pronto!')
            break

        else:
            print('''\n---> Has ingresado un numero no valido, intenta de nuevo. <-- ''')
            continue

    except Exception as e:
        print('Ha ocurrido un error:', e)
        
    otra_accion = input('\n¿Quieres realizar otra accion? Y/N: ').lower()

    # Si el usuario no quiere jugar otra historia, imprimimos un mensaje y salimos del bucle
    if otra_accion != 'y':
        print('\n¡Vuelve pronto!')
        break