"""
rooms = {
    1: "Habitación individual - $45.000 por noche",
    2: "Habitación doble - $65.000 por noche",
    3: "Habitación matrimonial - $70.000 por noche",
    4: "Habitación suite - $120.000 por noche",
    5: "Habitación familiar - $150.000 por noche",
}
"""

tipo_habitacion = int(input("""
    1. Habitación individual - $45.000 por noche
    2. Habitación doble - $65.000 por noche
    3. Habitación matrimonial - $70.000 por noche
    4. Habitación suite - $120.000 por noche
    5. Habitación familiar - $150.000 por noche
    
Ingrese la opcion de la habitación a reservar: """))

cantidad_noches = int(input("Ingrese la cantidad de noches: "))

try:

    match tipo_habitacion:
        case 1:
            valor = 45000
            print("Habitación individual - $45.000 por noche")
            print(f"Valor por {cantidad_noches} noches: {cantidad_noches * valor}")
        
        case 2:
            valor = 65000
            print("Habitación doble - $65.000 por noche")
            print(f"Valor por {cantidad_noches} noches: {cantidad_noches * valor}")

        case 3:
            valor = 70000
            print("Habitación matrimonial - $70.000 por noche")
            print(f"Valor por {cantidad_noches} noches: {cantidad_noches * valor}")

        case 4:
            valor = 120000
            print("Habitación suite - $120.000 por noche")
            print(f"Valor por {cantidad_noches} noches: {cantidad_noches * valor}")

        case 5:
            valor = 150000
            print("Habitación familiar - $150.000 por noche")
            print(f"Valor por {cantidad_noches} noches: {cantidad_noches * valor}")

        case _:
            print("Opción no valida")
    
except:

    print('Opción no valida')
