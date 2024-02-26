import json

# Ruta del archivo JSON
ruta_archivo_json = 'Practicando/11.Generador de letras/letras.json'

# Cargar el contenido del archivo JSON
with open(ruta_archivo_json, 'r') as canciones:
    datos = json.load(canciones)

# Crear una lista para almacenar los nombres de las canciones y las letras de las canciones
nombre_canciones = []
autor_cancion = []
letras_canciones = []
for cancion in datos:
    nombre_cancion = cancion["nombre_cancion"]
    autores = cancion["autor"]
    letra_cancion = cancion["letra"]
    nombre_canciones.append(nombre_cancion)
    letras_canciones.append(letra_cancion)
    if autores not in autor_cancion:
        autor_cancion.append(autores)

# Mostrar las canciones al usuario
while True:
    try:
        eleccion = int(input("""
Que categoria quieres ver?:
[1]: Artistas
[2]: Canciones
[3]: Salir
-->: """))
        
        if eleccion == 1:
            while True:
                print("Esta es la lista de Artistas:")
                for i, autor in enumerate(autor_cancion):
                    print(f"[{i + 1}]: {autor}")
                print("[0]: volver")

                # Pedir al usuario que elija un artista específico
                eleccion_artista = int(input("Elige un artista: "))
                if eleccion_artista == 0:
                    break
                elif 0 < eleccion_artista <= len(autor_cancion):
                    # Imprimir las canciones del artista seleccionado
                    artista_seleccionado = list(autor_cancion)[eleccion_artista - 1]
                    print(f"Canciones de {artista_seleccionado}:")
                    numero_cancion = 1
                    for i, nombre in enumerate(nombre_canciones):
                        if artista_seleccionado in datos[i]["autor"]:
                            print(f"[{numero_cancion}]: {nombre}")
                            numero_cancion += 1
                    print("[0]: Volver")
                    eleccion_cancion = int(input("Elige una opción: "))
                    if eleccion_cancion == 0:
                        continue
                    elif 0 < eleccion_cancion <= len(nombre_canciones):
                        indice_cancion = eleccion_cancion - 1
                        print(f"Esta es la letra de la canción '{nombre_canciones[indice_cancion]}':")
                        print(letras_canciones[indice_cancion])
                        break
                    else:
                        print("Selección no válida. Por favor, elige una opción válida.")

                else:
                    print("Selección no válida. Por favor, elige una opción válida.")

        elif eleccion == 2:
            while True:
                print("Esta es la lista de canciones:")
                for i, nombre in enumerate(nombre_canciones):
                    print(f"[{i + 1}]: {nombre}")
                print("[0]: Volver")

                eleccion_cancion = int(input("Elige una opción: "))
                if eleccion_cancion == 0:
                    break
                elif 0 < eleccion_cancion <= len(nombre_canciones):
                    indice_cancion = eleccion_cancion - 1
                    print(f"Esta es la letra de la canción '{nombre_canciones[indice_cancion]}':")
                    print(letras_canciones[indice_cancion])
                    break
                else:
                    print("Selección no válida. Por favor, elige una opción válida.")

        else:
            print("Hasta luego!")
            break

    except ValueError:
        print("Selección no válida. Por favor, elige una opción válida.")
    
    # Preguntar si el usuario quiere hacer algo más
    respuesta = input("¿Quieres hacer algo más? (y/n): ").lower()
    if respuesta != "y":
        print("Hasta luego!")
        break
