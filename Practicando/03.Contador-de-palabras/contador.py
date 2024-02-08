# Función para contar cantidad de palabras en el texto
def contador_palabras(texto):
    # Separamos el texto en palabras
    texto = texto.split()
    # Calculamos la cantidad de palabras
    cantidad_palabras = len(texto)
    # Imprimimos el resultado
    if cantidad_palabras == 1:
        print(f'\nEl texto contiene "{cantidad_palabras}" palabra')
    else:
        print(f'\nEl texto contiene "{cantidad_palabras}" palabras')

# Función para contar cantidad de letras en el texto
def contador_letras(texto):
    # Calculamos la cantidad de letras
    cantidad_letras = sum(c.isalpha() for c in texto)
    # Imprimimos el resultado
    if cantidad_letras == 1:
        print(f'\nEl texto contiene "{cantidad_letras}" letra')
    else:
        print(f'\nEl texto contiene "{cantidad_letras}" letras')

# Bucle principal para permitir al usuario seleccionar y ejecutar operaciones
while True:
    try:
        # Bucle para manejar la entrada del usuario
        while True:
            # Solicitamos al usuario que elija una opción
            try:
                eleccion = int(input('''
¿Que deseas hacer?
[1]: Contar cantidad de palabras.
[2]: Contar cantidad de letras.
[3]: Salir.
-->: '''))
                # Salimos del bucle interno si la conversión a número es exitosa
                break
                
            except ValueError:
                print('\n--> Has ingresado algo que no es un número, por favor, intenta de nuevo. <--')

        # Ejecutamos la opción seleccionada por el usuario
        if eleccion == 1:
            texto = input('\n¿Qué texto quieres analizar?: ')
            contador_palabras(texto)

        elif eleccion == 2:
            texto = input('\n¿Qué texto quieres analizar?: ')
            contador_letras(texto)

        elif eleccion == 3:
            print('\n¡Vuelve pronto!')
            break

        else:
            print('''\n---> Has ingresado un número no válido, intenta de nuevo. <-- ''')
            continue

    except Exception as e:
        print('Ha ocurrido un error:', e)
    
    # Preguntamos al usuario si quiere realizar otra acción
    otra_accion = input('\n¿Quieres realizar otra acción? Y/N: ').lower()

    # Salimos del bucle principal si el usuario no quiere realizar otra acción
    if otra_accion != 'y':
        print('\n¡Vuelve pronto!')
        break