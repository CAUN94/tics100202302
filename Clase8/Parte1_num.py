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

# Veamos unos ejemplos.

# Anteriormente si quisieramos crear una lista con los elementos 1, 2, 3 
# hariamos lo siguiente:

lista = [1,2,3]
print(lista) #imprime [1, 2, 3]

# En el caso de numpy podriamos hacer lo siguiente:
import numpy
arreglo = numpy.array([1,2,3])
print(arreglo) #imprime [1 2 3] sin comas!!!!

# Ahora veamos a que nos referiamos anteriormente con "unificacion de tipo de datos":

arreglo_uno = numpy.array([3.2,5,2.1])
print(arreglo_uno) #imprime [3.2 5.  2.1] convirtiendo todo a float!!!

arreglo_dos = numpy.array([1,2,"buenas!"])
print(arreglo_dos) #imprime ['1' '2' 'buenas!'] convirtiendo todo a str

arreglo_tres = numpy.array([1.5,2,"y ahora?"])
print(arreglo_tres) #imprime ['1.5' '2' 'y ahora?'] convirtiendo todo a str

# veamos un ejemplo concreto en donde es mejor utilizar numpy que listas.
# Haga un programa que cree una lista con 10 elementos generados al azar
# y muestre en pantalla el mayor de ellos.

import random
lista = []
for i in range (0,10):
    numero = random.randint(0,100)
    lista.append(numero)

mayor = lista[0]
for dato in lista:
    if dato > mayor:
        mayor = dato
print(lista)
print(f"El numero mas grande es {mayor}")

# ahora veamos como seria con numpy

arreglo = numpy.random.randint(0,100,[10])
mayor = numpy.max(arreglo)
print(arreglo)
print(mayor)

# QUE HERMOSO O NO?!!!