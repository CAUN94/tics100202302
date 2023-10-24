# Algo que vimos de manera superficial fueron los "ciclos for anidados" con los
# cuales podemos, dentro de otras cosas, trabajar con "matrices" o "listas de listas"
# ejemplo:

lista_listas = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(lista_listas)
for i in range(len(lista_listas)):
    print(lista_listas[i])

import numpy as np

matriz = np.ones([4,5])
print(matriz)
# Matriz con numeros aleatorios
matriz = np.random.randint(0,101,[4,4])
print(matriz)
print(matriz[0:2,2:4])