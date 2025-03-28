#############################  EXAMEN SORPRESA 28 MARZO #####################################



# EJERCICIO


# DEFINIMOS LA CLASE PUNTO CON SUS ATRIBUTOS Y MÉTODOS
# La clase Punto representa un punto en un plano cartesiano con coordenadas (x, y).
# Tiene métodos para determinar en qué cuadrante se encuentra, calcular el vector entre dos puntos y calcular la distancia entre ellos.
# La clase Punto tiene los siguientes métodos:   __init__(self, x=0, y=0), __str__(self), cuadrante(self), vector(self, otro_punto), distancia(self, otro_punto).

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        elif self.x == 0:
            return "El punto está sobre el eje Y."
        elif self.y == 0:
            return "El punto está sobre el eje X."
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        else:
            return "El punto está en el cuarto cuadrante."
    
    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
    
    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

# Ejemplo de uso
p1 = Punto(2, 3)
p2 = Punto(5, 5)
print(p1)  # (2, 3)
print(p2)  # (5, 5)
print(p1.cuadrante()) 
print(p2.cuadrante())  

vector_ab = p1.vector(p2)
print(f"Vector AB: {vector_ab}")  

distancia_ab = p1.distancia(p2)
print(f"Distancia entre A y B: {distancia_ab:.2f}")


# DEFINIMOS LA CLASE RECTANGULO CON SUS ATRIBUTOS Y MÉTODOS
# La clase Rectangulo representa un rectángulo definido por dos puntos opuestos en un plano cartesiano.
# La clase Punto tiene los siguientes métodos: __init__(self, punto1=Punto(), punto2=Punto()), base(self), altura(self), area(self).


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
rect = Rectangulo(p1, p2)
print(f"Base del rectángulo: {rect.base()}")
print(f"Altura del rectángulo: {rect.altura()}")
print(f"Área del rectángulo: {rect.area()}")



