# Ahora que ya vimos un base simple de lo que son listas hoy entraremos a profundizar y ver más ejercicios sobre esta herramienta.

# Una lista es una estructura de datos que nos permite almacenar una colección de datos. Estos datos pueden ser de cualquier tipo, y cada uno de ellos se denomina elemento de la lista. Las listas se definen entre corchetes y los elementos se separan por comas. Por ejemplo, la siguiente lista contiene 3 elementos: 1, 2 y 3.

lista = [1,2,3,4]

# Los indices de las listas comienzan en 0 y terminan en n-1, donde n es el largo de la lista. Para acceder a los elementos de una lista se utiliza el indice. Para saber el largo de una lista se utiliza la funcion len().

print(lista[0]) # Imprime 1
print(lista[1]) # Imprime 2
print(lista[2]) # Imprime 3

print(len(lista)) # Imprime 3

largo = len(lista) # Guardamos el largo de la lista en una variable

print(lista[largo-1]) # Imprime 4, porque accedemos al ultimo elemento de la lista

# Para modificar un valor funciona como cualquier variable

print(lista[0]) # Imprime 1
lista[0] = 5
print(lista[0]) # Imprime 5

# También podemos crear listas vacias

lista_vacia = []

# Para agregar un elemento a una lista se utiliza el metodo append()
print(lista_vacia) # Imprime []
lista_vacia.append(1) # Agregamos el numero 1 a la lista y lo agreagamos al final
print(lista_vacia) # Imprime [1]
lista_vacia.append(5) # Agregamos el numero 5 a la lista y lo agreagamos al final
print(lista_vacia) # Imprime [1, 5]
lista_vacia.append(5) # Agregamos el numero 5 a la lista y lo agreagamos al final
lista_vacia.append(6) # Agregamos el numero 6 a la lista y lo agreagamos al final
print(lista_vacia) # Imprime [1, 5, 5, 6]

# Las listas pueden contener distintos tipos de datos

lista = [1, 2, 3, "Hola", "Mundo", True, False]

# Incluso una segunda lista

lista = [1, 2, 3, "Hola", "Mundo", True, False,[2,3,4]]
print(lista)
lista.append([1,2,3])
lista.append('TICS100')
lista.append(False)
print(lista)

# Ahora depende de nosotros como utilizarlas, por ejemplo podemos crear una serie de listas que sean un alumno de su curso y sus notas (nombre, apellido, curso, notas)

alumno1 = ['Juan', 'Perez', '4to', [5.0, 6.0, 7.0, 4.0]]
alumno2 = ['Maria', 'Gonzalez', '4to', [4.0, 6.0, 7.0, 4.0]]
alumno3 = ['Pedro', 'Gonzalez', '4to', [5.0, 6.0, 7.0, 4.0]] 

# Y eso incluso lo podemos poner en otra lista, pero eso ya es más avanzado en cuanto a su uso en algoritmos.

alumnos = [alumno1, alumno2, alumno3]
alumno4 = ['Pedro', 'Gonzalez', '4to', [5.0, 6.0, 7.0, 4.0]]
alumnos.append(alumno4)
print(alumnos)
print(alumnos[0])
print(alumnos[0][0])

# Ejercicio 0: Crear una función que devuelva una lista con n numeros entre min y max. Los numeros deben ser aleatorios.

import random

def crear_lista(n,min,max):
    lista = []
    for i in range(n):
        lista.append(random.randint(min,max))
    return lista

lista = crear_lista(10, 1, 100)
print(lista)

# Existen 3 formas de recorrer la lista, la primera es con un ciclo for y range, la segunda es solo con ciclo for y la tercera es con un ciclo while.

def recorrer_lista_for_y_rangr(lista):
    print('Recorrer lista con for y range')
    for i in range(len(lista)):
        print(f"Indice: {i} - Valor: {lista[i]}")

# recorrer_lista_for_y_rangr(lista)

def recorrer_lista_for(lista):
    print('Recorrer lista con for')
    for elemento in lista:
        print(f"Valor: {elemento}")

# recorrer_lista_for(lista)
# recorrer_lista_for('Esto es una oración')

def recorrer_lista_while(lista):
    print('Recorrer lista con while')
    i = 0
    while i < len(lista):
        print(f"Indice: {i} - Valor: {lista[i]}")
        i += 1

# recorrer_lista_while(lista)

# Algunos comandos utiles para la utilizacion de listas son: append(), insert(),remove(), pop(), index(), len(), reverse(), copy()

# Append() agrega un elemento al final de la lista

lista = [1,2,3,4]
lista.append(5)
print(lista)

# Insert() agrega un elemento en la posicion indicada, este recibe 2 parametros, el primero es la posicion y el segundo el elemento a agregar

lista.insert(0, 6) # Agrega el numero 6 en la posicion 0 y desplaza los demas elementos a la derecha
print(lista)
lista.insert(2, 7) # Agrega el numero 7 en la posicion 2 y desplaza los demas elementos a la derecha
print(lista)

# Remove() elimina el primer elemento de la lista que coincida con el parametro que se le pasa

lista.remove(7) # Elimina el primer elemento que sea igual a 7 y corre los demas elementos a la izquierda
print(lista)

# Pop() elimina el elemento de la posicion indicada, si no se indica ninguna posicion elimina el ultimo elemento de la lista

lista.pop() # Elimina el ultimo elemento de la lista
print(lista)
lista.pop(1) # Elimina el elemento de la posicion 1
print(lista)
lista.pop(1) # Elimina el elemento de la posicion 1
print(lista)

# Index devuelve la posicion del elemento indicado, del primero que encuentre

print(lista.index(4)) # Imprime 2

# Len() devuelve el largo de la lista

print(len(lista)) # Imprime 2

# Reverse() invierte el orden de la lista

lista.append(5)
lista.append(6)
lista.append(7)

print(lista)
lista.reverse()
print(lista)
lista.reverse()
print(lista)

# Para volver al orden original podemos utilizar el metodo reverse() 2 veces

# Copy() copia una lista en otra

lista2 = lista.copy()

# Sort() ordena la lista de menor a mayor

lista2.sort()

print(lista2)






