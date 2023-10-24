# Numpy es una libreria de python que nos permite trabajar con vectores y matrices

# Importamos la libreria numpy
import numpy as np

# Creamos un vector

vector = np.array([1,2,3,4,5,6,7,8,9,10])
# print(vector)

# Creamos una matriz

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matriz)

# Creamos un vector de ceros

vector_ceros = np.zeros(10)
# print(vector_ceros)

# Creamos una matriz de ceros

matriz_ceros = np.zeros((5,5))
# print(matriz_ceros)

# Creamos un vector de unos

vector_unos = np.ones(10)
# print(vector_unos)

# Creamos una matriz de unos

matriz_unos = np.ones((5,5))
# print(matriz_unos)

# Creamos un vector con valores aleatorios

vector_aleatorio = np.random.rand(10)
# print(vector_aleatorio)

# Creamos una matriz con valores aleatorios

matriz_aleatoria = np.random.rand(5,5)
# print(matriz_aleatoria)

# Creamos un vector con valores aleatorios enteros

vector_aleatorio_enteros = np.random.randint(10)
# print(vector_aleatorio_enteros)

# Creamos una matriz con valores aleatorios enteros

matriz_aleatoria_enteros = np.random.randint(10, size=(5,5))
# print(matriz_aleatoria_enteros)

# Creamos un vector con valores aleatorios enteros entre un rango

vector_aleatorio_enteros_rango = np.random.randint(10,20, size=(10))
# print(vector_aleatorio_enteros_rango)

# Creamos una matriz con valores aleatorios enteros entre un rango

matriz_aleatoria_enteros_rango = np.random.randint(10,20, size=(5,5))

# print(vector_aleatorio_enteros_rango)
# print(matriz_aleatoria_enteros_rango)

# Funcionalidades de numpy

# En el vector puedo:
# Obtener el valor maximo

# print(vector_aleatorio_enteros_rango.max())

# Obtener el valor minimo

# print(vector_aleatorio_enteros_rango.min())

# Obtener el promedio

# print(vector_aleatorio_enteros_rango.mean())

# Comparar valores

# print(vector_aleatorio_enteros_rango < 15)

# Obtener los valores que cumplen la condicion

# print(vector_aleatorio_enteros_rango[vector_aleatorio_enteros_rango < 15])

# Obtener una posicion especifica

# print(vector_aleatorio_enteros_rango[0])
# print(vector_aleatorio_enteros_rango[3])

# Recorrer el vector

# for valor in vector_aleatorio_enteros_rango:
#     print(valor)

# En la matriz puedo:
# Obtener el valor maximo

# print(matriz_aleatoria_enteros_rango.max())

# Obtener el valor minimo

# print(matriz_aleatoria_enteros_rango.min())

# Obtener el promedio

# print(matriz_aleatoria_enteros_rango.mean())

# Obtener el valor maximo de cada fila

# print(matriz_aleatoria_enteros_rango.max(axis=1))

# Obtener el valor maximo de cada columna

# print(matriz_aleatoria_enteros_rango.max(axis=0))

# Comparar valores

# print(matriz_aleatoria_enteros_rango < 15)

# Obtener los valores que cumplen la condicion

# print(matriz_aleatoria_enteros_rango[matriz_aleatoria_enteros_rango < 15])

# Obtener una posicion especifica

# print(matriz_aleatoria_enteros_rango[0])
# print(matriz_aleatoria_enteros_rango[3,1])

# Obtener rango de posiciones

# print(matriz_aleatoria_enteros_rango[0:2])
# print(matriz_aleatoria_enteros_rango[0:2,1:3])
# print(matriz_aleatoria_enteros_rango[:,0:2])

# Recorrer la matriz

# for fila in matriz_aleatoria_enteros_rango:
#     print(fila)

# Recorrer la matriz valor por valor

# for fila in matriz_aleatoria_enteros_rango:
#     for columna in fila:
#         print(columna)

