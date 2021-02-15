#Tipo de dato compuesto String

nombre = 'Anyerson Fuentes'
email = "afuentes@rolda.com.ve"
direccion = '''La matica
Vuelta larga'''

print(nombre)
print(email)
print(direccion)

print('Nombre: ' + nombre + ' email: ' + email)
print(f'Nombre: {nombre} email: {email}')
print('Nombre: {} email: {}'.format(nombre,email))
print('Nombre: %s email: %s'% (nombre,email))

#inmutabilidad

lenguaje = 'Python'
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

lenguaje = 'p' + lenguaje[1:]
print(lenguaje)

lenguaje = 'PYTHON'.lower()
print(lenguaje)

#Split

valores = '5,6,8,9'
numeros = valores.split(',')
print(numeros)

#Find

indice = valores.find('2')

print(indice)


print()

def encontrar(cadena,caracter):
    indice = -1
    for i in range(0,len(cadena)):
        if caracter == cadena[i]:
            indice=i
            break
    return indice

indice = encontrar(valores,'8')
print(indice)
    
