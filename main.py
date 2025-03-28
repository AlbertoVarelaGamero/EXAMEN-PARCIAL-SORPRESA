# main.py

from clase_punto import Punto
from clase_rectangulo import Rectangulo

# Creación de los puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir puntos
print(A)  
print(B)  
print(C)  
print(D)  

# Cuadrantes de A, C y D
print(A.cuadrante())  
print(C.cuadrante())  
print(D.cuadrante())  

# Vectores AB y BA
vector_ab = A.vector(B)
vector_ba = B.vector(A)
print(f"Vector AB: {vector_ab}")  
print(f"Vector BA: {vector_ba}")  

# Distancias entre puntos
distancia_ab = A.distancia(B)
distancia_ba = B.distancia(A)
print(f"Distancia entre A y B: {distancia_ab:.2f}")
print(f"Distancia entre B y A: {distancia_ba:.2f}")

# Punto más lejano del origen
distancias = {"A": A.distancia(D), "B": B.distancia(D), "C": C.distancia(D)}
punto_mas_lejano = max(distancias, key=distancias.get)
print(f"El punto más lejano del origen es {punto_mas_lejano}")

# Crear rectángulo con A y B
rect = Rectangulo(A, B)
print(f"Base del rectángulo: {rect.base()}")
print(f"Altura del rectángulo: {rect.altura()}")
print(f"Área del rectángulo: {rect.area()}")
