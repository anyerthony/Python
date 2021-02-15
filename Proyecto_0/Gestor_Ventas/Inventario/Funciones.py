from datetime import datetime
from collections import Counter


def registrar_producto(productos, producto):
    """
    Agrega un producto a la lista de productos

    parameters:
        productos: Lista de productos.
        producto: producto a agregar
    """
    productos.append(producto)
    print('Registrado con exito')


def realizar_venta(ventas, venta):

    venta['fecha'] = datetime.now()
    ventas.append(venta)
    print('Vendido')


def buscar_producto(productos, id_producto):
    for p in productos:
        if p['id_producto'] == id_producto:
            return p['id_producto']
    return None


def cambiar_disponible(productos,producto):
    for p in productos:
        if p['id_producto'] == producto:
            if p['disponible'] == 0:
                p['disponible'] =1
                print('Producto habilitado para la venta')
            else:
                p['disponible']=0
                print('Prodicto inhabilitado para la venta')



def ventas_rango(ventas, fecha_ini, fecha_fin):
    ventas_rango_list = []
    for v in ventas:
        print(v['fecha'])
        if v['fecha'] >= fecha_ini and datetime.date(v['fecha']) <= datetime.date(fecha_fin):
            ventas_rango_list.append(v)
    return ventas_rango_list


def top_5_mas(ventas):
    conteo_ventas = {}

    for v in ventas:
        if v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {k: v for k, v in sorted(
        conteo_ventas.items(), key=lambda item: item[1], reverse=True)}

    contador = Counter(conteo_ventas)
    return contador.most_common(5)


def top_5_menos(ventas):
    conteo_ventas = {}

    for v in ventas:
        if v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {k: v for k, v in sorted(
        conteo_ventas.items(), key=lambda item: item[1])}

    contador = Counter(conteo_ventas)
    return contador.most_common(5)[::-1]


def mostrar_datos_producto(lista_productos,id):
    for e in lista_productos:
        if e['id_producto'] == id:
            print('Nombre: ', e['nombre'])
            dis = ''
            if e['disponible']:
                dis= 'Si'
            else:
                dis = 'No'
            print('Disponible para la venta?: ', dis)
            print('Stock actual: ', e['stock'])
            print('Precio: ', e['precio'])
            
