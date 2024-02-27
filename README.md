# Practicando Python
En mi camino para mejorar mis habilidades de desarrollo de software, he encontrado la necesidad de trabajar en una variedad de proyectos. Siguiendo el consejo de FreeCodeCamp, he decidido comenzar con proyectos más pequeños para desarrollar mi confianza y dominio de Python. Este enfoque progresivo me permitirá aprender y aplicar conceptos fundamentales de manera práctica. Antes de embarcarme en cualquier proyecto, es esencial tener una comprensión sólida de los conceptos básicos de Python, como la declaración de variables, la entrada del usuario, las estructuras de control, y la creación de funciones.

### **_Página de los ejercicios en freecodecamp_**
    https://www.freecodecamp.org/espanol/news/11-proyectos-de-python-que-los-desarrolladores-junior-pueden-crear-para-practicar/

### Índice

1. [Par o Impar](#1-par-o-impar)
2. [Juego Mad Libs](#2-juego-mad-libs)
3. [Contador de Palabras](#3-contador-de-palabras)
4. [Información de la Biografía](#4-información-de-la-biografía)
5. [¿Cuál es el Acrónimo?](#5-cuál-es-el-acrónimo)
6. [Piedra, Papel y Tijeras](#6-piedra-papel-y-tijeras)
7. [Adivina el Número Oculto](#7-adivina-el-número-oculto)
8. [¿Es Palíndromo?](#8-es-palíndromo)
9. [Calculador de Propinas](#9-calculador-de-propinas)
10. [Extractor de Información del Correo Electrónico](#10-extractor-de-información-del-correo-electrónico)
11. [Generador de Letras](#11-generador-de-letras)

### ----------> *Proyectos para niveles Junior* <----------

## 1. Par o Impar
Este programa solicita al usuario ingresar un número entre 1 y 1000. Luego, determina si el número es par o impar y muestra el resultado. Si el usuario ingresa un número fuera de este rango o un valor no numérico, se le pedirá que ingrese un número válido. Después de cada verificación, se pregunta al usuario si desea ingresar otro número. El programa continúa ejecutándose hasta que el usuario decida no ingresar más números.

El resumen del funcionamiento del código es el siguiente:

    Se solicita al usuario ingresar un número entre 1 y 1000.
    El programa verifica si el número ingresado es válido.
    Se determina si el número es par o impar.
    Se le pregunta al usuario si desea ingresar otro número.
    El programa continúa ejecutándose hasta que el usuario decida no ingresar más números.

## 2. Juego Mad Libs
Este programa consiste en dos partes: un módulo llamado historias.py que contiene dos funciones, enciende_mi_fuego() y eureka(), y un archivo de entrada index.py que permite al usuario seleccionar y jugar una de estas historias.

En el archivo historias.py, las funciones solicitan al usuario que ingrese ciertas palabras o frases, que luego se insertan en una historia predefinida para crear una narrativa personalizada. La función enciende_mi_fuego() genera una historia sobre la invención del fuego, mientras que la función eureka() presenta historias sobre famosos inventores y sus creaciones.

El archivo index.py importa estas funciones y presenta al usuario un menú para seleccionar una de las dos historias o salir del programa. Después de jugar una historia, se le pregunta al usuario si quiere jugar otra historia o salir del programa.

El resumen del funcionamiento del código es el siguiente:

    El usuario elige una historia entre dos opciones disponibles.
    Para cada historia seleccionada, se solicitan ciertas palabras o frases al usuario.
    Estas palabras o frases se insertan en una historia predefinida para crear una narrativa personalizada.
    Después de jugar una historia, se le pregunta al usuario si quiere jugar otra historia o salir del programa.

## 3. Contador de Palabras
Este programa ofrece dos funciones principales: contador_palabras() y contador_letras().

La función contador_palabras(texto) cuenta la cantidad de palabras en un texto dado. Primero, el texto se divide en palabras utilizando el método split(). Luego, se cuenta el número de elementos en la lista resultante, lo que proporciona la cantidad de palabras. El resultado se imprime, indicando si hay una palabra o más de una palabra en el texto.

La función contador_letras(texto) cuenta la cantidad de letras en un texto dado. Utiliza una expresión generadora para iterar sobre cada carácter en el texto y cuenta solo aquellos que son letras utilizando el método isalpha(). Nuevamente, el resultado se imprime, indicando si hay una letra o más de una letra en el texto.

El programa principal solicita al usuario que elija entre contar la cantidad de palabras, contar la cantidad de letras o salir del programa. Dependiendo de la elección del usuario, se solicita un texto de entrada y se llama a la función correspondiente. Después de ejecutar la operación seleccionada, se le pregunta al usuario si desea realizar otra acción. El programa continúa ejecutándose hasta que el usuario elige salir.

## 4. Información de la Biografía
Este programa solicita al usuario su nombre, fecha de nacimiento, dirección y meta personal. Utiliza validación de entrada para asegurarse de que el nombre y la fecha de nacimiento se ingresen correctamente en formatos válidos. Para la fecha de nacimiento, utiliza una expresión regular para verificar que el formato sea día/mes/año. Una vez que se han ingresado todos los detalles, el programa imprime la información personal recopilada en un formato organizado y fácil de leer.

## 5. ¿Cuál es el Acrónimo?
Este programa solicita al usuario que ingrese un significado completo y luego genera un acrónimo basado en las letras iniciales de cada palabra en el significado ingresado. Primero, divide el significado en palabras utilizando el método split(). Luego, itera sobre cada palabra y concatena la primera letra de cada palabra para formar el acrónimo. Finalmente, imprime el acrónimo resultante en mayúsculas.

## 6. Piedra, Papel y Tijeras
Este juego clásico permite al jugador enfrentarse a la computadora en una serie de encuentros de Piedra, Papel o Tijeras. El programa solicita al jugador que elija una opción y luego genera una elección aleatoria para la computadora. Después de cada ronda, muestra quién ganó el encuentro o si fue un empate. Además, lleva un registro de los puntos acumulados por el jugador y la computadora, así como la cantidad de empates.

El jugador puede elegir entre las siguientes opciones:

    Piedra
    Papel
    Tijeras
    Salir del juego

Después de cada ronda, el jugador tiene la opción de continuar jugando o salir del juego. Al salir del juego, se muestran los resultados finales, incluidos los puntos del jugador, los puntos de la computadora y la cantidad de empates.

## 7. Adivina el Número Oculto
En este juego, la computadora elige aleatoriamente un número entre 1 y 10, y el jugador tiene tres intentos para adivinar ese número. Después de cada intento, la computadora proporciona pistas al jugador sobre si el número ingresado es mayor o menor que el número seleccionado aleatoriamente.
Instrucciones:

    La computadora elegirá un número aleatorio entre 1 y 10.
    Tienes tres intentos para adivinar el número.
    Intenta adivinar el número antes de quedarte sin vidas.

Ejemplo de juego:

    La computadora elige el número aleatorio.
    Introduces un número, por ejemplo, 5.
    Continúas hasta que adivines el número o agotes tus tres intentos.

## 8. ¿Es Palíndromo?
Este programa te permite verificar si las palabras que ingreses son palíndromas o no. Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.
Instrucciones:

    Ingresa cinco palabras.
    El programa determinará cuáles de esas palabras son palíndromas y cuáles no lo son.
    Al final, te mostrará las palabras palíndromas y las palabras que no son palíndromas.

Ejemplo de uso:

    Por favor ingresa 5 palabras que creas que son palíndromas
    Ingresa tu palabra 1: radar
    Ingresa tu palabra 2: oso
    Ingresa tu palabra 3: casa
    Ingresa tu palabra 4: nivel
    Ingresa tu palabra 5: perro

Resultados:

    Palabras palíndromas encontradas:
        * radar
        * oso

    Palabras que no son palíndromas encontradas:
        * casa
        * nivel
        * perro

El programa identificará y te mostrará cuáles de las palabras ingresadas son palíndromas y cuáles no.

## 9. Calculador de Propinas
Este programa te ayuda a calcular la propina y dividir la factura entre un grupo de personas.

    1.Ingresar la Factura Total: Se te pedirá que ingreses el total de la factura del día.
    2.Cálculo de Propinas: La calculadora mostrará tres opciones de propina: 18%, 20% y 25%. Mostrará el monto de propina correspondiente y el total que debe pagar, incluyendo la propina, para cada una de estas opciones.
    3.Dividir la Factura: Luego, se te pedirá que ingreses la cantidad de personas que pagarán la factura. El programa calculará cuánto debe pagar cada persona, incluyendo la propina, para cada opción de propina.
    4.Opción Especial (para 2 personas): Si dividen la factura en dos personas, tendrás la opción de especificar qué porcentaje de la factura pagará cada persona. El programa calculará cuánto debe pagar cada persona según el porcentaje especificado.

Ejemplo de Uso:

    ¿Cuál es la factura total de hoy, por favor? $55.87
    La propina aplicando el 18% es $10.06, que contabiliza un total de $65.93
    La propina aplicando el 20% es $11.17, que contabiliza un total de $67.04
    La propina aplicando el 25% es $13.97, que contabiliza un total de $68.84

    ¿En cuántas personas quiere dividir la factura?: 4
    La propina aplicando el 18% es $2.51, que contabiliza un total de $16.48 por persona
    La propina aplicando el 20% es $2.79, que contabiliza un total de $16.76 por persona
    La propina aplicando el 25% es $3.49, que contabiliza un total de $17.46 por persona

En este ejemplo, se calculan las propinas y el total a pagar por persona para una factura de $55.87. Luego, se divide la factura entre 4 personas, mostrando cuánto debe pagar cada una, incluyendo la propina, para las tres opciones de propina.

## 10. Extractor de Información del Correo Electrónico
Este programa extrae información útil de una dirección de correo electrónico ingresada por el usuario.

    1.Ingresar Correo Electrónico: Se solicita al usuario que ingrese su dirección de correo electrónico.
    2.Extracción de Información: El programa divide la dirección de correo electrónico en dos partes: el usuario y el dominio.
    3.Análisis de Dominio: Se identifica el proveedor de servicios de correo electrónico basado en el dominio utilizado.

**_Gmail_: Se muestra un mensaje de saludo indicando que el correo está registrado con Google.**

**_Hotmail/Outlook_: Se muestra un mensaje de saludo indicando que el correo está registrado con Microsoft.**

**_Yahoo_: Se muestra un mensaje de saludo indicando que el correo está registrado con Yahoo.**

**_Otros Dominios_: Se muestra un mensaje de saludo personalizado indicando el dominio utilizado.**

Ejemplo de Uso:

    Ingresa tu correo electrónico: ejemplo@gmail.com
    Usuario: ejemplo
    Saludos, estoy viendo que tu email está registrado con Google. ¡Eso es genial!

En este ejemplo, el usuario ingresa la dirección de correo electrónico "ejemplo@gmailcom".El programa extrae el usuario ("ejemplo") y analiza el dominio ("gmail"). Luego, muestra un mensaje de saludo indicando que el correo está registrado con Google.

## 11. Generador de Letras
Generador de Letras de Canciones

Este programa permite al usuario explorar letras de canciones almacenadas en un archivo JSON. El usuario puede elegir entre ver las canciones por artistas o ver todas las canciones disponibles.
Funcionamiento:

    1.Cargar Datos: El programa carga los datos de las canciones desde un archivo JSON que contiene información sobre el nombre de la canción, el autor y la letra.

    2.Opciones de Visualización:
        * Por Artistas: El usuario puede seleccionar un artista específico y ver todas las canciones asociadas a ese artista junto con sus letras.
        * Por Canciones: El usuario puede ver todas las canciones disponibles y seleccionar una para ver su letra.

    3-Interacción con el Usuario:
        * El programa permite al usuario elegir entre las opciones de visualización mencionadas anteriormente.
        * Después de ver la letra de una canción, el usuario tiene la opción de volver al menú principal o salir del programa.

Archivo JSON de Ejemplo (letras.json):

    json

        [
            {
                "nombre_cancion": "Mockingbird",
                "autor": "Eminem",
                "letra": "Yeah, I know sometimes Things may not always make sense to you right now..."
            },
            {
                "nombre_cancion": "Praise Jah In The Moonlight",
                "autor": "YG Marley",
                "letra": "(They say the Sun)..."
            }
        ]

Ejemplo de Uso:

Que categoria quieres ver?:

    [1]: Artistas
    [2]: Canciones
    [3]: Salir
    -->: 1

Esta es la lista de Artistas:

    [1]: Eminem
    [2]: YG Marley
    ...
    [0]: volver
    Elige un artista: 1

Canciones de Eminem:

    [1]: Mockingbird
    [2]: Lose Yourself
    ...
    [0]: Volver
    Elige una opción: 1

Esta es la letra de la canción 'Mockingbird':

    Yeah, I know sometimes Things may not always make sense to you right now...

¿Quieres hacer algo más? (y/n): n

Hasta luego!

En este ejemplo, el usuario elige ver las canciones por artistas, selecciona "Eminem", luego la canción "Mockingbird", y finalmente decide salir del programa.