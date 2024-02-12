palindromo = []
no_palindromo = []

print('Porfavro ingresa 5 palabras que creas que son palindromas')

for palabras in range(5):

    palabra = input(f'Ingresa tu palabra {palabras + 1}: ')
    palabra_reves = palabra[::-1]

    if palabra == palabra_reves:
        palindromo.append(palabra)
    else:
        no_palindromo.append(palabra)


print("\nResultados:")
if len(palindromo) == 0:
    print("No se encontraron palabras palíndromas.")
elif len(palindromo) == 1:
    print("Palabra palíndroma encontrada:")
else:
    print("Palabras palíndromas encontradas:")
for palabra in palindromo:
    print(palabra)


if len(no_palindromo) == 0:
    print("\nNo se encontraron palabras que no sean palíndromas.")
elif len(no_palindromo) == 1:
    print("\nPalabra que no es palíndroma encontrada:")
else:
    print("\nPalabras que no son palíndromas encontradas:")
for palabra in no_palindromo:
    print(palabra)