from .Funciones import realizar_venta,registrar_producto,buscar_producto,cambiar_disponible,ventas_rango,top_5_mas,top_5_menos,mostrar_datos_producto

import datetime



def menu():
    # 1. Registro de nuevos productos
    # 2. Venta de productos existentes
    # 3. Búsqueda de los datos de un producto por su código
    # 4. Cambiar la disponibilidad de un producto.
    # 5. Generar un reporte de los productos vendidos en un rango de fecha.
    # 6. Ver un top 5 de los productos más vendidos, al igual que los menos vendidos.

    print('Bienvendo al gestor de ventas')
    print('Seleccione una de las siguentes opciones:')
    print()
    print('1.- Registrar un nuevo producto')
    print('2.- Vender productos')
    print('3.- Buscar un producto')
    print('4.- Inhabilitar/habilitar producto')
    print('-' * 10, 'Productos mas vendidos', '-'*10)
    print('5.- Por fecha')
    print('6.- Top 5')
    print('-'*20)
    print('0.- Salir')
    print()

def sub_menu():
    print('Reporte: top 5 de productos...')
    print('1.- Mas vendidos.')
    print('2.- Menos vendidos.')
    print('-'*20)
    print('0.- Volver al menu principal')

def capturar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje + ': '))
            return valor
        except ValueError:
            print('Error: debe ingresar un numero entero')
        except KeyboardInterrupt as e:
            print('Entrada abortada.',e)
        print()

def capturar_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje + ': '))
            return valor
        except ValueError:
            print('Error: debe ingresar un numero entero')
        except KeyboardInterrupt as e:
            print('Entrada abortada.',e)
        print()

def capturar_cadena(mensaje):
    while True:
        try:
            valor = input(mensaje + ': ')

            if len(valor):
                return valor
            else:
                print('Debe ingresar una cadena valida')
        except KeyboardInterrupt as e:
            print('Entrada abortada.',e)
        print()

def continuar():
    print()
    print('Precione enter para continuar...', end='')
    input()
    print()


def escribir(mensaje):
    print()
    print(mensaje)
    print()

def main():
    productos= []
    # registrar_producto(productos,{
    #                 'id_producto': 1,
    #                 'nombre':'Aut01',
    #                 'disponible':1,
    #                 'stock':10,
    #                 'precio':100.2})
    
    # registrar_producto(productos,{
    #                 'id_producto': 2,
    #                 'nombre':'Aut02',
    #                 'disponible':1,
    #                 'stock':10,
    #                 'precio':110.2})

    ventas = []
    # realizar_venta(ventas,{
    #                     'id_producto':1,
    #                     'cantidad': 20
    #                 })
    # realizar_venta(ventas,{
    #                     'id_producto':2,
    #                     'cantidad': 25
    #                 })

    try:
        while True:

            menu()

            while True:
                try:
                    #opcion = int(input('Digite la opcion a seleccionar: '))
                    opcion= capturar_entero('Digite la opcion a seleccionar')
                    print()
                    break
                except ValueError as e:
                    print('Mensaje: Digite una opcion vaida, ',e)
                    print()

            if 0 <= opcion <= 6:
                if opcion == 0:
                    print('Ha salido del programa')
                    break
                elif opcion == 1:
                    id_producto = capturar_entero('Indique el id del producto')
                    validar = buscar_producto(productos,id_producto)
                    #print(validar)
                    if validar == id_producto:
                        escribir('Ya se registro un producto con este codigo')
                    else:
                        nombre = capturar_cadena('Indique el nombre del producto')
                        while True:
                            disponible= capturar_entero('Esta disponible para la venta? SI --> 1     NO --> 0')
                            if disponible == 0 or disponible == 1:
                                break
                            else:
                                escribir('Debe seleccionar una de las opciones indicadas')
                        stock = capturar_entero('Inventario inicial para el producto')
                        precio = capturar_decimal('Precio del producto')

                        registrar_producto(productos,{
                            'id_producto':id_producto,
                            'nombre':nombre,
                            'disponible':disponible,
                            'stock':stock,
                            'precio':precio})

                elif opcion == 3:
                    busqueda = capturar_entero('Indique el codigo del producto')
                    print()

                    resultado_busqueda = buscar_producto(productos,busqueda)
                    #print(resultado_busqueda)
                    if resultado_busqueda is None:
                        print('No se encontro el producto')
                    else:
                        mostrar_datos_producto(productos,resultado_busqueda)
                elif opcion == 2:
                    if len(productos):
                        while True:
                            id_producto = buscar_producto(productos,capturar_entero('Codigo del producto a a vender'))
                            if id_producto is None:
                                escribir('No se encontro el producto')
                            else:
                                break
                        cantidad = capturar_entero('Cantidad vendida')
                        
                        realizar_venta(ventas,{
                            'id_producto':id_producto,
                            'cantidad': cantidad
                        })
                    else:
                        escribir('No hay productos registrados')
                elif opcion ==4 :
                    if len(productos):
                        while True:
                                id_producto = buscar_producto(productos,capturar_entero('Codigo del producto'))
                                if id_producto is None:
                                    escribir('No se encontro el producto')
                                else:
                                    break
                        cambiar_disponible(productos,id_producto)
                    else: 
                        escribir('No hay productos registrados')
                
                elif opcion == 5:
                    while True:
                        try:
                            fecha_ini = capturar_cadena('Fecha de inicio (DD-MM-AAAA)')
                            fecha_ini = datetime.datetime.strptime(fecha_ini, '%d-%m-%Y')
                            break
                        except:
                            escribir('ERROR: formato de fecha invalido')
                    while True:
                        try:
                            fecha_fin = capturar_cadena('Fecha de final (DD-MM-AAAA)')
                            fecha_fin = datetime.datetime.strptime(fecha_fin, '%d-%m-%Y')
                            break
                        except:
                            escribir('ERROR: formato de fecha invalido')
                    ventas_en_rango= ventas_rango(ventas,fecha_ini,fecha_fin)
                    if len(ventas_en_rango):
                        for v in ventas_en_rango:
                            mostrar_datos_producto(productos,v['id_producto'])
                            total_venta =0
                            for p in productos:
                                if p['id_producto']==v['id_producto']:
                                    total_venta=p['precio']
                            total_venta *= v['cantidad']
                            print('Cantidad vendida: ',v['cantidad'])
                            print('Total: ',total_venta)
                    else:
                        escribir('No se encontraron ventas en el rango indicado')
                elif opcion == 6:
                    if len(ventas):
                        while True:
                            sub_menu()
                            while True:
                                print()
                                opcion = capturar_entero('Digite la opcion a seleccionar')
                                print()
                                if opcion in (0,1,2):
                                    break
                                else:
                                    escribir('Debe elegir una de las opciones de menu.')
                            if opcion == 1:
                                resultado = top_5_mas(ventas)
                                #print(resultado)
                                for v in resultado:
                                    mostrar_datos_producto(productos, v[0])
                                    print('Ventas totales: ',v[1])
                                    print()
                            elif opcion == 2:
                                resultado = top_5_menos(ventas)
                                print(resultado)
                                for v in resultado:
                                    mostrar_datos_producto(productos, v[0])
                                    print('Ventas totales: ',v[1])
                                    print()
                            elif opcion == 0:
                                escribir('Saliendo al menu principal')
                                break
                            continuar()

                    else:    
                        escribir('No se ha realizado ninguna venta')
                

            continuar()
    except KeyboardInterrupt as e:
        print('ERROR: Salida forzada del sistema. ',e)
                
    
if __name__ == '__main__':
    main()
