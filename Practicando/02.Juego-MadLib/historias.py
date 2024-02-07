# Función que ejecutara la historia llamada "Enciende mi fuego"
def enciende_mi_fuego ():
    # Se le pide al usuario ingresar datos
    parte_del_cuerpo_plural = input('Ingresa una parte del cuerpo en plural: ')
    adjetivo_masculino_plural = input('Ingresa un adjetivo masculino en plural: ')
    adjetivo_masculino = input('Ingresa un adjetivo masculino: ')
    adjetivo_masculino_2 = input('Ingresa un segundo adjetivo masculino: ')
    lugar = input('Ingresa un lugar: ')
    animal = input('Ingresa un animal: ')
    parte_del_cuerpo = input('Ingresa una parte del cuerpo: ')
    adjetivo = input('Ingresa un adjetivo: ')
    adjetivo_femenino_plural = input('Ingresa un adjetivo femenino en plural: ')
    adverbio = input('Ingresa un adverbio: ')
    interjeccion = input('Ingresa una interjección: ')
    adjetivo_femenino_plural_2 = input('Ingresa un segundo adjetivo femenino en plural: ')
    nombre_propio = input('Ingresa un nombre propio: ')
    nombre_femenino = input('Ingresa un nombre femenino: ')

    # Los datos ocuparán el espacio "vacío" en el texto.
    print(f'''
    Antiguamente, el ser humano caminaba a cuatro "{parte_del_cuerpo_plural}",
    se expresaba mediante gruñidos "{adjetivo_masculino_plural}" y no sabía encender un "{adjetivo_masculino}" fuego.
    Esta es la historia del día en que la humanidad cambió para siempre (traducida del "{adjetivo_masculino_2}" idioma de las cavernas):
    -.  Hombre de las cavernas 1: 
        En esta cueva hace más frío que en (el/ella) "{lugar}".
        Incluso con la piel del/de la "{animal}" más caliente no consigo que mi "{parte_del_cuerpo}" deje de tiritar.

    -.  Hombre de las cavernas 2:
        Si al menos pudiésemos encontrar una manera de que el frío fuera más "{adjetivo}".

    -.  Hombre de las cavernas 1:"
        Estoy aburrido. Creo que voy a jugar un rato con estas ramas "{adjetivo_femenino_plural}".

    -.  Hombre de las cavernas 2:
        ¿Por qué no las frotas "{adverbio}" a ver qué pasa?

    -.  Hombre de las cavernas 1:
        ¡"{interjeccion}"! Está saliendo humo de las "{adjetivo_femenino_plural_2}" ramas!

    -.  Hombre de las cavernas 2:
        ¡Ay! ¡Está caliente! ¡Por el amor de "{nombre_propio}", hemos conseguido calor!

    -.  Hombre de las cavernas 1:
        A partir de ahora llamaremos "fuego" a esta "{nombre_femenino}" mágica.
    ''')

# Función que ejecutara la historia llamada "Eureka"
def eureka ():
    # Se le pide al usuario ingresar datos
    sustantivo = input('Ingresa un sustantivo: ')
    profesion_masculina_plural = input('Ingresa una profesión masculina en plural: ')
    sustantivo_masculino_plural = input('Ingresa un sustantivo masculino en plural: ')
    sustantivo_plural = input('Ingresa un sustantivo en plural: ')
    sustantis_plural_2 = input('Ingresa un segundo sustantivo en plural: ')
    sustantivo_femenino_plural = input('Ingresa un sustantivo femenino en plural: ')
    sustantivo_masculino = input('Ingresa un sustantivo masculino: ')
    sustantivo_plural_3 = input('Ingresa un tercer sustantivo plural: ')
    sustantivo_plural_4 = input('Ingresa un cuarto sustantivo plural: ')
    adjetivo_masculino = input('Ingresa un adjetivo masculino: ')
    sustantivo_masculino_2 = input('Ingresa un segundo sustantivo masculino: ')
    sustantivo_femenino = input('Ingresa un sustantivo femenino: ')
    sustantivo_femenino_2 = input('Ingresa un segundo sustantivo femenino: ')

    # Los datos ocuparán el espacio "vacío" en el texto.
    print(f'''
    A lo largo de la historia, los inventores han creado objetos de uso 
    cotidiano como el ordenador, el coche, y el/la {sustantivo}. Estos 
    son algunos de los {profesion_masculina_plural} más conocidos hoy en día:

    -. Benjamin Franklin no solo fue uno de los {sustantivo_masculino_plural} fundadores 
    de los Estados Unidos, si no que también inventó muchas cosas, entre las 
    que se incluyen las lentes bifocales, que permiten ver {sustantivo_plural}
    de lejos y cerca. También creó el pararrayos, que protege los/las
    {sustantis_plural_2} de las {sustantivo_femenino_plural} eléctricas.

    -. Johannes Gutenberg fue un {sustantivo_masculino} alemán que inventó la
    imprenta, una máquina capaz de imprimir palabras y {sustantivo_plural_3}
    para componer libros, periódicos y {sustantivo_plural_4}.

    -. Thomas Edison fue un inventor {adjetivo_masculino} muy conocido
    seguramente por crear una bombilla accesible a todo el {sustantivo_masculino_2}.
    También inventó el fonógrafo, la primera {sustantivo_femenino} con la que se
    pudo grabar la {sustantivo_femenino_2} humana y después reproducirla.
    ''')