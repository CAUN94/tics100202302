# Creen una matriiz con valores aleatorios entre 1 y 7
# Creemos una lista con 10 valores equivalentes a la cantidad de files, estas contaran con nombres
# El promedio final con nomnbre de cada alumno y las cantidad de pruebas en las que tuvo un rojo

# [6,7]
# [3,3]
# [3,5]

# ['Cris','Javier','Carlos']

# Cris Mean: 6.5 Rojos: 0
# Javier Mean: 3 Rojos: 2
# Carlos Mean: 4 Rojos: 1

import numpy as np

# Crear matriz con valores aleatorios entre 1 y 7

matriz = np.random.randint(1, 7, size=(10, 10))

# Lista con 10 nombres
lista = ['Cris', 'Javier', 'Carlos', 'Juan', 'Pedro', 'Maria', 'Jose', 'Luis', 'Ana', 'Luisa']

# Promedio final con nombre de cada alumno y cantidad de pruebas en las que tuvo un rojo

print(matriz)

# numpy coount values in array
a = np.array([2,3,4])

for i in range(0, 10):
    promedio = matriz[i].mean()
    lista_rojos = (matriz[i] < 4)
    rojos = np.sum(lista_rojos)
    print(lista[i], 'Mean:', promedio, 'Rojos:', rojos)