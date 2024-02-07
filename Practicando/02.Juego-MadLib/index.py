# Importamos las funciones enciende_mi_fuego y eureka del módulo historias
from historias import enciende_mi_fuego, eureka

# Creamos un bucle infinito para permitir al usuario seleccionar y jugar historias repetidamente
while True:
    try:
        # Solicitamos al usuario que elija una historia
        eleccion = int(input('''¿Qué historia quieres?
        [1]: Enciende mi fuego
        [2]: ¡Eureka!
        [3]: Salir
        -->: '''))

        if eleccion == 1:
            enciende_mi_fuego()
    
        elif eleccion == 2:
            eureka()
        
        elif eleccion == 3:
            print('¡Vuelve luego!')
            break
        # Si el usuario ingresa un número no válido, le pedimos que elija entre 1, 2 o 3
        else:
            print('Has ingresado un número inválido, por favor, elige entre 1, 2 o 3')
            continue
    # Manejamos excepciones en caso de que el usuario ingrese algo que no sea un número
    except:
        print('Has ingresado un número invalido, por favor, vuelve a intentar: ')

    # Preguntamos al usuario si quiere jugar otra historia
    otra_historia = input('¿Quieres probar otra historia? Y/N: ').lower()

    # Si el usuario no quiere jugar otra historia, imprimimos un mensaje y salimos del bucle
    if otra_historia != 'y':
        print('¡Vuelve pronto!')
        break