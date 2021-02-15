#Tipo de dato compuesto tupla

punto = (2,5)
print(type(punto))
print(punto)
print(len(punto))
#---------------

print('While')
numeros = (1,2,3,4,5,6,78,9)
i=0
while i < len(numeros):
    print(f'Numero actual: {numeros[i]}')
    i+=1

print('For')

for i in range(len(numeros)):
    print(f'Numero actual: {numeros[i]}')

print('For mejorado')

for i in numeros:
    print('Numero actual: ',i)

print('Enumerate')

for i,v in enumerate(numeros):
    print(f'Numero actual: {v}')

#Crear tuplas
#1

numeros1 = 1,2,3
print(type(numeros1))

print()

#2

impares = tuple([1,6,9])
print(type(impares))

print()

