# Suma de Vectores: Crear 2 vectores de 5 elementos enteros cada uno, sumar el primer elemento del primer vector con el primer elemento del segundo vector y así sucesivamente hasta 5 veces e imprimir el resultado de cada operación. Los vectores deben ser creado con números aleatorios. Se deben mostrar los 2 vectores y el resultado de la suma.

import random
import numpy

# Creamos la funcion de crear vectores
def crearVectores(nr):
    # Creamos el vector con numpy y lo llenamos con ceros
    vector = numpy.zeros(nr)
    # Llenamos el vector con numeros aleatorios
    for i in range(nr):
        # Creamos un numero aleatorio entre 0 y 10 y lo agregamos al vector
        vector[i] = random.randint(0, 10)
    return vector

# Funcion que suma los vectores
def sumaVectores(vec1,vec2):
    # Creamos el vector con numpy y lo llenamos con ceros
    suma = numpy.zeros(5)
    # Sumamos los vectores
    for i in range(5):
        # Sumamos los numeros que comparten la misma posicion en los vectores
        suma[i] = vec1[i] + vec2[i]
    return suma

# Creamos los vectores
vec1 = crearVectores(5)
vec2 = crearVectores(5)
# Sumamos los vectores
suma = sumaVectores(vec1,vec2)
# Mostramos los vectores y la suma
print("Vector 1: ", vec1)
print("Vector 2: ", vec2)
print("Suma: ", suma)