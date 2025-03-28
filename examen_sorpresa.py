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


# DEFINIMOS LA CLASE 


