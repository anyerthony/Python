def sumar(*numeros):
    return sum(numeros)
    
def restar(a,b):
    return (a-b)

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b == 0:
        raise ValueError('Intenta dividir entre 0')
    else:
        return a/b