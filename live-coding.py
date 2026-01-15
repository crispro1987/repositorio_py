try :

    temperatura = float(input('Cuantos grados :'))

    if temperatura < 10:
        print('Usa abrigo grueso y bufanda')
    elif 10 <= temperatura <= 20:
        print('Usa chaqueta ligera')
    elif 20 <= temperatura <= 30:
        print('Usa ropa cómoda y fresca')
    elif temperatura > 30:
        print('Usa ropa ligera y protector solar.') 
    else:
        print('Temperatura no válida')

except:
    print('Se ha ingresado una temperatura no valida')