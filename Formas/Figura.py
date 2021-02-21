from abc import ABC,abstractclassmethod

class Figura(ABC):
    def __init__(self,color,forma):
        self.color = color
        self.forma = forma

    def dibujar(self):
        print('Se esta dibujando la figura de forma', self.forma)

    @abstractclassmethod
    def Colorear(self):
        pass