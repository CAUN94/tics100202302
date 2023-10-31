# Producto Escalar: Crea un programa que permita calcular el producto escalar de dos vectores de n elementos. Los vectores se deben crear de forma aleatoria usando numpy y su funcion de crear vectores. El producto escalar se calcula sumando la multiplicacion de los elementos que ocupan la misma posicion en los vectores. Por ejemplo, si tenemos los vectores [1,2,3] y [4,5,6] el producto escalar es 1*4 + 2*5 + 3*6 = 32.

import numpy as np

# Creamos la funcion de crear vectores
def crearVector(n):
    vector = np.random.randint(0, 10, n)
    return vector

# Funcion que calcula el escalar
def productoEscalar(vec1,vec2):
    escalar = 0
    for i in range(len(vec1)):
        escalar += vec1[i] * vec2[i]
    return escalar

vec1 = crearVector(20)
vec2 = crearVector(20)
print("Vector 1: ", vec1)
print("Vector 2: ", vec2)
print("Escalar: ", productoEscalar(vec1,vec2))
