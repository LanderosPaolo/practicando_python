# Importamos las funciones enciende_mi_fuego y eureka del módulo historias
from historias import enciende_mi_fuego, eureka

# Creamos un bucle infinito para permitir al usuario seleccionar y jugar historias repetidamente
while True:
    try:
        # Solicitamos al usuario que elija una historia
        while True:
            try:
                eleccion = int(input('''¿Qué historia quieres?
                [1]: Enciende mi fuego
                [2]: ¡Eureka!
                [3]: Salir
                -->: '''))
                break  # Salimos del bucle interno si la conversión a int es exitosa

            except ValueError:  # Manejamos la excepción si el usuario no ingresa un número
                print('Has ingresado algo que no es un número, por favor, intenta de nuevo.')
        
        if eleccion == 1:
            enciende_mi_fuego()
    
        elif eleccion == 2:
            eureka()
        
        elif eleccion == 3:
            print('¡Vuelve luego!')
            break

        else:
            print('Has ingresado un número inválido, por favor, elige entre 1, 2 o 3')

    except Exception as e:  # Manejamos cualquier otra excepción no esperada
        print('Ha ocurrido un error:', e)

    # Preguntamos al usuario si quiere jugar otra historia
    otra_historia = input('¿Quieres probar otra historia? Y/N: ').lower()

    # Si el usuario no quiere jugar otra historia, imprimimos un mensaje y salimos del bucle
    if otra_historia != 'y':
        print('¡Vuelve pronto!')
        break
