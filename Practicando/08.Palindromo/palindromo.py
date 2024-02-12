# Creamos las listas donde se guardaran las palabras
palindromo = []
no_palindromo = []

print('Por favor ingresa 5 palabras que creas que son palíndromas')

# Creamos un bucle for para pedir las 5 palabras al usuario
for palabras in range(5):

    palabra = input(f'Ingresa tu palabra {palabras + 1}: ')
    # Damos vuelta las palabras ingresadas
    palabra_reves = palabra[::-1]

    # Si la palabra de derecha a izquierda es igual, se agrega a la lista de palíndromas
    if palabra == palabra_reves:
        palindromo.append(palabra)
    # En caso contrario se agrega a la lista de no_palindromas
    else:
        no_palindromo.append(palabra)

# Se imprime el resultado
print("\nResultados:")
if len(palindromo) == 0:
    print("No se encontraron palabras palíndromas.")
    # En caso de que solo sea una palabra, el texto mostrado es en singular
elif len(palindromo) == 1:
    print("Palabra palíndroma encontrada:")
    # Si hay más de una palabra palíndroma, el texto mostrado es en plural
else:
    print("Palabras palíndromas encontradas:")
# Imprime cada palabra que se encuentra en la lista
for palabra in palindromo:
    print(palabra)


if len(no_palindromo) == 0:
    print("\nNo se encontraron palabras que no sean palíndromas.")
# En caso de tener solo una palabra, el texto es singular
elif len(no_palindromo) == 1:
    print("\nPalabra que no es palíndroma encontrada:")
# Si hay más de 1 palabra, el texto es plural
else:
    print("\nPalabras que no son palíndromas encontradas:")
# Se recorre la lista por cada palabra en ella y se muestra al usuario
for palabra in no_palindromo:
    print(palabra)