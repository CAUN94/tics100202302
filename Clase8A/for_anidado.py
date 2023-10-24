# doble lista de 3x3
lista_listas = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(lista_listas)):
    for j in range(len(lista_listas[i])):
        print(lista_listas[i][j])

import numpy as np
#  matriz de 3x3 con numeros aleatorios entre 1 y 9
matriz = np.random.randint(1,10,[3,3])
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        print(matriz[i,j])
