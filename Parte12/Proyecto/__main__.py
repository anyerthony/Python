
from .Funciones_aridmeticas import sumar,restar,multiplicar,dividir

def menu():
    print('Seleccione una opcon:')
    print('1) Sumar')
    print('2) Restar')
    print('3) Multiplicar')
    print('4) Dividir')
    print('0) Salir')
    print()

def main():
    
    while True:
        
        menu()
        while True:
            try:
                opcion = int(input('Indique la operacion que desea realizar: '))
                break
            except:
                print('Error, ninguna opcion seleccionada')
                print()

        print()
        if 0 < opcion <= 4:
            while True:
                try:
                    a = int(input('Primer valor: '))
                    b = int(input('Segundo valor: '))
                    break
                except:
                    print('Indique valores validos')
                    print()
            print()
            
            if opcion == 1:
                suma = sumar(a,b)
                print('El resultado de la suma es: ',suma)
            elif opcion == 2:
                resta = restar(a,b)
                print('El resultado de la resta es: ',resta)
            elif opcion == 3:
                multiplicacion = multiplicar(a,b)
                print('El resultao de la multiplicacion es: ',multiplicacion)
            elif opcion == 4:
                try:
                    division = dividir(a,b)
                    print('El resultado de la division es: ',division)
                except ValueError as e:
                    print('Error: ',e)
                    
            print()

        else:
            print('Ha salido del programa')
            break

if __name__ == '__main__':
    main()
