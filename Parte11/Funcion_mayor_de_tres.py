def verificar_mayor(a,b,c):
    if a > b and a > c:
        return a 
    elif b > a and b > c:
        return b 
    elif c > a and c > b:
        return c
    else:
        return 0

print('EL mayor es: ', verificar_mayor(5,4,9))

def verificar_mayor_op_2(*numeros):
    return max(numeros)

print('EL mayor es: ', verificar_mayor_op_2(5,4,9,8,48,88))

def verificar_mayor_op_3(a,b,c):
    if isinstance(int,float):
        if a > b and a > c:
            return a
        elif a == b == c:
            return None
        else:
            return verificar_mayor(b,c,a)
    else:
        raise TypeError('Se resivieron parametros incorrectos')

#print('EL mayor es: ', verificar_mayor_op_3(5,4,9))
#print('EL mayor es: ', verificar_mayor_op_3(1,1,2))
try:
    print('EL mayor es: ', verificar_mayor_op_3('a',2,1))
except TypeError as e:
    print("ERROR: ",e)



def verificar_rango(n):
    if isinstance(int,float):
        if n in range(10,101): 
            return True 
        else: 
            return False
    else:
        raise TypeError


    print("N esta en un rango de 10 a 100? ",verificar_rango(100))

try:
    print("N esta en un rango de 10 a 100? ",verificar_rango('100n'))


except TypeError as e:    
    print("Error: Tipo de dato incorrecto")

print('ok')