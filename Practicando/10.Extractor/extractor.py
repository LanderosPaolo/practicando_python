# Se solicita el correo al usuario
email = input('Ingresa tu correo electronico: ').strip('')

# Se divide la cadena en dos separando desde el @
usuario, dominio = email.split('@')

# se separa el dominio en dos partes separando desde el .
dominio = dominio.split('.')[0]

# Se imprime el usuario
print('usuario :'+ usuario)

# Segun el dominio utilizado se da un mensaje "personalizado"
if dominio == 'gmail':
    print('Saludos, estoy viendo que tu email está registrado con Google. ¡Eso es genial!')

elif dominio == 'hotmail' or dominio == 'outlook':
    print('Saludos, estoy viendo que tu email está registrado con Microsoft. ¡Eso es genial!')

elif dominio == 'yahoo':
    print('Saludos, estoy viendo que tu email está registrado con Yahoo. ¡Eso es genial!')

else:
    print(f"Saludos, estoy viendo que estás utilizando un dominio personalizado de {dominio}. ¡Impresionante!")