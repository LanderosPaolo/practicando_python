# Importamos random
import random

# Damos la bienvenida al jugador
print('Bienvenido al juego de piedra, papel o tijeras')

# Creamos los contadores para los puntos
puntos_computadora = 0
puntos_jugador = 0
empates = 0

# Creamos un bucle para seguir jugando o en caso de que ingrese un número no válido
while True:
    # Opciones que tendrá la computadora
    opciones_computadora = ['Piedra', 'Papel', 'Tijeras']
    # Las opciones se eligen de manera aleatoria con random
    opcion_aleatoria = random.choice(opciones_computadora)

    try:
        eleccion = int(input('''
Puedes elegir que vas a usar en el siguiente encuentro
[1]: Piedra
[2]: Papel
[3]: Tijeras
[4]: Salir
--->: '''))
        # Transformamos la opción del jugador
        if eleccion == 1:
            eleccion = 'Piedra'
        
        elif eleccion == 2:
            eleccion = 'Papel'

        elif eleccion == 3:
            eleccion = 'Tijeras'

        elif eleccion == 4:
            # Si quiere salir el juego muestra los resultados de los puntos y se detiene
            print(f'''\nEl resultado es este:
-- Puntos jugador: {puntos_jugador}
-- Puntos computadora: {puntos_computadora}
-- Empates: {empates}''')
            print('\n¡Vuelve pronto!')
            break

        else:
            # En caso de ingresar un número no válido, se vuelve a preguntar
            print('''\n---> Has ingresado un número no válido, intenta de nuevo. <-- ''')
            continue

        # En caso de que la elección del jugador sea la misma de la computadora, es un empate
        if eleccion == opcion_aleatoria:
            # Se suma +1 al contador de empates
            empates += 1
            print('\n--> Es un empate <--')
            print('Jugador: ' + eleccion)
            print('Computadora: ' + opcion_aleatoria)

        # Según las reglas del juego, el jugador es el ganador
        elif (eleccion == 'Piedra' and opcion_aleatoria == 'Tijeras') or \
            (eleccion == 'Papel' and opcion_aleatoria == 'Piedra') or \
            (eleccion == 'Tijeras' and opcion_aleatoria == 'Papel'):
            # Se suma +1 a los puntos del jugador
            puntos_jugador += 1
            print('\n--> Felicidades, has ganado <--')
            print('Jugador: ' + eleccion)
            print('Computadora: ' + opcion_aleatoria)
        
        # Según las reglas si no se cumple la línea 52 ni 60 el jugador pierde
        else:
            # Se suma +1 a los puntos de la computadora
            puntos_computadora += 1
            print('\n--> Has perdido <--')
            print('Jugador: ' + eleccion)
            print('Computadora: ' + opcion_aleatoria)

    except ValueError:
        print('\nHas ingresado algo que no es un número, por favor, intenta de nuevo.')

    # Después de cada juego, tenemos la opción de seguir jugando
    seguir_jugando = input('\n¿Quieres seguir jugando? Y/N: ').lower()

    # Si no queremos seguir jugando, nos informan de los puntos y el juego termina
    if seguir_jugando != 'y':
        print(f'''\nEl resultado es este:
-- Puntos jugador: {puntos_jugador}
-- Puntos computadora: {puntos_computadora}
-- Empates: {empates}''')
        print('\n¡Vuelve pronto!')
        break