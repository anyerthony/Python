#50 primeros digitos de la serie Fibonnaci

numero_1 = 1
numero_2 = -1

interuptor = True

for i in range(0,50):
    print(str(i+1) + ") " + str(numero_1+numero_2))
    
    if interuptor:
        numero_2 = numero_1+numero_2
        interuptor = False
    else:
        numero_1= numero_2+numero_1
        interuptor = True
