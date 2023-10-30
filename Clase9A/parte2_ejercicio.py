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

lista = ['Cris', 'Javier', 'Carlos', 'Juan', 'Pedro', 'Maria', 'Jose', 'Luis', 'Ana', 'Luisa']
matriz = np.random.randint(1, 7, size=(10, 7))

for i in range(0,len(lista)):
    nombre = lista[i]
    notas = matriz[i]
    notas_rojas = matriz[i] < 4
    print(f"{nombre} Mean: {notas.mean()} Rojos: {notas_rojas.sum()}")