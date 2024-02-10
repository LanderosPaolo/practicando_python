# Pedimos al usuario que ingrese un significado completo
palabras = input('Ingresa el significado completo: ')

# separamos las palabras
palabras_separadas = palabras.split()

# Creamos la variable acronimo con un string vacío
acronimo = ''

# Con el bucle for tomamos la primera letra de cada palabra
for letra in palabras_separadas:
    acronimo = acronimo + letra[0]

# Se imprime el acronimo
print(f'El acronimo es: "{acronimo.upper()}"')