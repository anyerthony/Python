#Mostrar la fecha y hora actual

import datetime

Ahora = datetime.datetime.now()

print('Fecha y hora actual: ', Ahora)
print()

Ahora_formato = Ahora.strftime('%H:%M:%S  %d/%m/%Y')

print('Fecha y hora con formato: ', Ahora_formato)