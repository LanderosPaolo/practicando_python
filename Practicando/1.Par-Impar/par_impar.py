print('-.Hola, quieres saber si un número es par o impar?')

# Mientras no se cumpla la condicion, se seguira preguntando
while True:
    try:
        # El input es transformado a integer
        numero = int(input('Ingresa un número entre el 1 y el 1000: '))

        # Si número es mayor o igual a 1 y menor o igual a 1000 se ejecuta.
        # En caso contrario vuelve a preguntar por un número válido
        if 1 <= numero <= 1000:

            if (numero % 2) == 0:
                print(f'El número "{numero}" es par')

            else:
                print(f'El número "{numero}" es impar')

            otro_numero = input('Quieres ingresar otro número? Y/N: ').lower()
            if otro_numero != 'y':
                print('Vuelve pronto!')
                break
    
    except:
        print('Por favor, ingresa un número válido')