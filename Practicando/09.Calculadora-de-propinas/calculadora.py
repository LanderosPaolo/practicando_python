def calcular_propina():
    # Según el problema, el valor de ejemplo a ingresar es de 55.87
    factura = float(input('¿Cuál es la factura total de hoy, por favor? $'))

    # Guardamos las propinas en una lista para poder ser usadas en el bucle for
    porcentajes_propina = [0.18, 0.2, 0.25]

    # Por cada porcentaje se realizará una operación mostrando los distintos totales
    for porcentaje in porcentajes_propina:
        propina = factura * porcentaje
        total = factura + propina
        print(f'La propina aplicando el {int(porcentaje * 100)}% es ${round((propina), 2)}, que contabiliza un total de ${round((total), 2)}')

    # Cuantas personas pagarán la cuenta
    cantidad_personas = int(input('¿En cuántas personas quiere dividir la factura?: '))

    # Se divide la factura en la cantidad de personas
    total_por_persona = factura / cantidad_personas

    # Cuanto es lo que pagara cada persona, la cantidad es ingresada en la variable "cantidad_personas"
    for porcentaje in porcentajes_propina:
        propina_porcentaje = factura * porcentaje
        propina_por_persona = propina_porcentaje / cantidad_personas
        total_por_persona_con_propina = total_por_persona + propina_por_persona
        print(f'La propina aplicando el {int(porcentaje * 100)}% es ${round(propina_por_persona, 2)}, que contabiliza un total de ${round(total_por_persona_con_propina, 2)} por persona')

    # En caso de ser 2 personas, se ejecuta este fragmento de código adicional, para completar con la orden del problema
    if cantidad_personas == 2:
        porcentaje_pago_1 = float(input("¿Qué porcentaje paga la primera persona? (por ejemplo, 70 para el 70%) "))
        porcentaje_pago_2 = 100 - porcentaje_pago_1

        pago_1 = round(factura * porcentaje_pago_1 / 100, 2)
        pago_2 = round(factura * porcentaje_pago_2 / 100, 2)

        print(f"La primera persona paga ${pago_1} ({porcentaje_pago_1}%) de la factura.")
        print(f"La segunda persona paga ${pago_2} ({porcentaje_pago_2}%) de la factura.")

calcular_propina()