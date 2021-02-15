# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

contador=1
caracter = "*"

for i in range(9):
    for j in range(contador):
        print(caracter,end=(" "))
    if i <4:
        contador +=1
    else:
        contador -=1
    print()
    
   
