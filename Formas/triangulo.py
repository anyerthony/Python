from Figura import Figura

class Triangulo(Figura):
    def __init__(self,color,forma,lados):
        super().__init__(color,forma)
        self.lados = lados

    def Colorear(self): 
        print('Se esta coloreando un triangulo con', self.lados ,' lados')

    
  
    