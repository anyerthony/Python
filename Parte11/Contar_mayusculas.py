def contar(texto):
    mayus = 0
    minus = 0
    oter = 0

    for l in texto:
        if l.isalpha():
            minus +=1


        if l >= 'a' and l <='z':
            minus += 1
        elif l >= 'A' and l <= 'Z':
            mayus += 1
        else:
            oter +=1
    return [mayus,minus,oter]

frase = 'No pinches mames! Wey'

print('cantidad de mayusculas y minisculas en HOLAaa:')
print('Mayusculas: ',contar(frase)[0])
print('Minusculas: ',contar(frase)[1])
print('Otros: ',contar(frase)[2])
