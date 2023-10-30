# Numpy es una libreria de pytthon que noos permite rabajar con vevtores y matricess.

import numpy as np

vector = np.array([1,2,3,4,5,6,7,8,9,10])
# print(vector)

vector2 = np.array([1,1,1,1,1,1,1,1,1,1])
# print(vector2)
# print(vector+vector2)
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matriz)

# Crear un vector con puros ceros
vector_ceros = np.zeros(10)
# print(vector_ceros)

# Crear un vector con puros ceros
vector_unos = np.ones(10)
# print(vector_unos)

matriz_unos = np.ones([7,4])
# print(matriz_unos)

matriz_ceros = np.zeros([4,5])
# print(matriz_ceros)

matriz_aleatoria_enteros = np.random.randint(1,7, size=(6,6))
print(matriz_aleatoria_enteros)

# print(matriz_aleatoria_enteros.max())
# print(matriz_aleatoria_enteros.min())
# print(matriz_aleatoria_enteros.mean())

sum = 0
count = 0
for fila in matriz_aleatoria_enteros:
    for valor in fila:
        sum += valor
        count += 1

# print(sum/count)

print(matriz_aleatoria_enteros >= 4)
# lista = np.array([1,2,3])
# lista_bol = np.array([True,False,True])

# print(lista[lista_bol])

print(matriz_aleatoria_enteros[matriz_aleatoria_enteros >= 4])

matriz_aleatoria_enteros = np.array([1,3,4,5])

for valor in matriz_aleatoria_enteros:
    print(valor)

matriz_aleatoria_enteros1 = np.random.randint(1,7, size=(6,6))
matriz_aleatoria_enteros2 = np.random.randint(1,7, size=(6,6))

print(matriz_aleatoria_enteros1)
print(matriz_aleatoria_enteros2)

print(matriz_aleatoria_enteros1 == matriz_aleatoria_enteros2)