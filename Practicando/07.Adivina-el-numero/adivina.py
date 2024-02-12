import random

print('¿Puedes adivinar el número que estoy pensando?')

# Variable que almacena el número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Intentos para poder adivinar el número
vidas = 3

while True:
    try:
        # Se pide un número al usuario
        numero = int(input('Ingresa un número entre el 1 y el 10: '))

        # Si el número es menor a 1 y mayor a 10 se le da un aviso y pide nuevamente el número
        if numero < 1 or numero > 10:
            print('\nSolo se permiten números entre el 1 y el 10')

        # Si el número es distinto al que penso la computadora, le da un aviso y resta una vida
        elif numero != numero_aleatorio:
            print('\nNo has acertado!!')
            vidas -= 1
            print(f'vidas: {vidas}')

        # En caso de acertar el número, le da un aviso y termina el juego
        else:
            print(f'\nFelicidades, estaba pensando en el número "{numero_aleatorio}"')
            print(f'Tus vidas restantes: {vidas}')
            break
        
        # Si las vidas llegan a 0, se da un aviso y el juego termina
        if vidas == 0:
            print(f'\nLamentablemente te has quedado sin vidas, estaba pensando en el número "{numero_aleatorio}"')
            break

    # En caso de agregarcualquier cosa que no sea un número
    except ValueError:
        print(f'\nPor favor ingresa un número entre el 1 y el 10')