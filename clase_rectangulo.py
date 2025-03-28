############################################################## EXAMEN SORPRESA 28 MARZO ##############################################################


# DEFINIMOS LA CLASE RECTANGULO CON SUS ATRIBUTOS Y MÉTODOS
# La clase Rectangulo representa un rectángulo definido por dos puntos opuestos en un plano cartesiano.
# La clase Punto tiene los siguientes métodos: __init__(self, punto1=Punto(), punto2=Punto()), base(self), altura(self), area(self).

from clase_punto import Punto

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2
    
    def base(self):
        return abs(self.punto2.x - self.punto1.x)
    
    def altura(self):
        return abs(self.punto2.y - self.punto1.y)
    
    def area(self):
        return self.base() * self.altura()
    
# Uso de la clase Rectangulo
p1 = Punto(2, 3)
p2 = Punto(5, 5)
rect = Rectangulo(p1, p2)
print(f"Base del rectángulo: {rect.base()}")
print(f"Altura del rectángulo: {rect.altura()}")
print(f"Área del rectángulo: {rect.area()}")

