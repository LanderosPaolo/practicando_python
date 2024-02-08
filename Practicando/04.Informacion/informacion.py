import re

while True:
    nombre = input('Ingrese su nombre: ')
    if not nombre.isalpha():
        print('No has ingresado un nombre válido')
    else:
        break

while True:
    nacimiento = input('Ingrese su fecha de nacimiento (formato día/mes/año): ')
    if re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', nacimiento):
        break
    else:
        print('Formato de fecha incorrecto. Por favor, ingrese la fecha en el formato día/mes/año.')

direccion = input('Ingrese su dirección: ')
meta = input('Ingrese su meta personal: ')

print(f'''
--> Datos Personales <--
-Nombre: {nombre}
-Fecha de nacimiento: {nacimiento}
-Dirección: {direccion}
-Meta personal: {meta}
''')