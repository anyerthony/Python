# Invertir una palabra introducida por el usuario

while True:
    print("Invertir palabra o frase (En blanco para salir)")
    frase =  input("Digite la palabra/frase que desa invertir: ")
    if len(frase) <=0:
        break
    frase_invertida = ""

    for i in range(len(frase)-1,-1,-1):
        frase_invertida = frase_invertida+ frase[i]

    tipo = ""
    if " " in frase:
        tipo="frase"
    else:
        tipo="palabra"

    print("Su {} invertida es:".format(tipo),end="\n")
    print(frase_invertida.capitalize())

    #----------------------------------------------------
    frase_invertida = frase[::-1]
    print("Su {} invertida es:".format(tipo),end="\n")
    print(frase_invertida.capitalize())