def sumar(lista):
    lista.append(2)
    return lista[0]
lista=[1,2,3]

sumar(lista)
r = sumar(lista)

print(lista)
print(r)