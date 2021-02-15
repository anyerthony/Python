#Introduccion a la manipulacion de archivos

#leer archivo de texto plano
def main():
    redes = open('parte14/redes_sociales.txt')

    print('Redes sociales')
    for l in redes.readlines():
        print('-> ',l,end='')

if __name__ == '__main__':
    main()
