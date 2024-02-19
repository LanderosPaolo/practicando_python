email = input('Ingresa tu correo electronico: ').strip('')

usuario, dominio = email.split('@')

dominio = dominio.split('.')[0]

print('usuario :'+ usuario)

if dominio == 'gmail':
    print('Saludos, estoy viendo que tu email está registrado con Google. ¡Eso es genial!')

elif dominio == 'hotmail' or dominio == 'outlook':
    print('Saludos, estoy viendo que tu email está registrado con Microsoft. ¡Eso es genial!')

elif dominio == 'yahoo':
    print('Saludos, estoy viendo que tu email está registrado con Yahoo. ¡Eso es genial!')

else:
    print(f"Saludos, estoy viendo que estás utilizando un dominio personalizado de {dominio}. ¡Impresionante!")