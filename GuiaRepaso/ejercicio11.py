# Suma de columnas: Crea una matriz de 5x5 con numeros aleatorios entre 1 y 10 y muestra la suma de cada columna en un vector. Por ejemplo, si tenemos la matriz:
# 1, 2, 3, 4, 5
# 6, 7, 8, 9, 10
# 11, 12, 13, 14, 15
# 16, 17, 18, 19, 20
# 21, 22, 23, 24, 25
# La suma de cada columna es:
# 55, 60, 65, 70, 75

import numpy as np

# Creamos la funcion de crear Matriz
def crearMatriz(n):
    matriz = np.random.randint(1, 10, (n,n))
    return matriz

# Funcion que suma las columnas
def sumaColumnas(matriz):
    suma = np.zeros(len(matriz))
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            suma[j] += matriz[i][j]
    return suma

matriz = crearMatriz(5)
print("Matriz: \n", matriz)
print("Suma de columnas: ", sumaColumnas(matriz))