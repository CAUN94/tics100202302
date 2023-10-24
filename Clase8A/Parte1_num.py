# Instalar numpy
# pip install numpy

# Ya conocimos las listas y sus distintos usos. Sabemos que podemos guardar distintos
# datos en la misma lista, independiente de si es un entero, un string, etc. Podemos
# hacer crecer esta lista cuanto necesitemos con ayuda de append, podemos eliminar elementos
# con pop y hacer muchas otras modificaciones segun necesitemos.

# Pero muchas veces tanta libertad puede traer problemas, ya que, por ejemplo, si
# tenemos una lista de numeros enteros y strings y queremos realizar una division
# tendremos un problema solo cuando nos encontremos con el string, ademas de que al ser
# un elemento "infinito", es complejo encontrar un elemento en una posicion especifica.

# Para estos casos y otros es una buena idea utilizar "Numpy", un modulo de python
# altamente utilizado y es el encargado de facilitarnos la vida en el trabajo de matrices
# y en la unificacion de tipos de datos. 

lista = [1,2,3]
print(lista)

import numpy as np
arreglo = np.array([1,2,3])
print(arreglo)

# Ahora veamos a que nos referimos con unificar tipos de datos
arreglo_uno = np.array([1,3,4,5.1,4.2])
print(arreglo_uno)

arreglo_dos = np.array([1,3,4,5.1,4.2,"hola"])
print(arreglo_dos)

# veamos un ejemplo concreto en donde es mejor utilizar numpy que listas.
# Haga un programa que cree una lista con 10 elementos generados al azar
# y muestre en pantalla el mayor de ellos.

import random

def crear_lista(nr):
    for i in range(nr):
        lista.append(random.randint(0,100))
    return lista
lista = crear_lista(10)

def mayor(lista):
    mayor = lista[0]
    for valor in lista:
        if valor > mayor:
            mayor = valor
    print(lista)
    print(mayor)

mayor(lista)

arreglo = np.random.randint(0,101,[10])
mayor = np.max(arreglo)
print(arreglo)
print(mayor)