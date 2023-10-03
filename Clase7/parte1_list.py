# Ahora que ya vimos un base simple de lo que son listas hoy entraremos a profundizar y ver más ejercicios sobre esta herramienta.

# Una lista es una estructura de datos que nos permite almacenar una colección de datos. Estos datos pueden ser de cualquier tipo, y cada uno de ellos se denomina elemento de la lista. Las listas se definen entre corchetes y los elementos se separan por comas. Por ejemplo, la siguiente lista contiene 3 elementos: 1, 2 y 3.

lista = [1, 2, 3]

# Los indices de las listas comienzan en 0 y terminan en n-1, donde n es el largo de la lista. Para acceder a los elementos de una lista se utiliza el indice. Para saber el largo de una lista se utiliza la funcion len().

print(lista[0]) # Imprime el primer elemento de la lista (1)
print(lista[1]) # Imprime el segundo elemento de la lista (2)
print(lista[2]) # Imprime el tercer elemento de la lista (3)

print(len(lista)) # Imprime 3

largo = len(lista)

print(lista[largo-1]) # Imprime el ultimo elemento de la lista (3)

# Para modificar un valor funciona como cualquier variable

print(lista[0]) # Imprime el primer elemento de la lista (1)

lista[0] = 4

print(lista[0]) # Imprime el primer elemento de la lista (4)

# También podemos crear listas vacias

lista_vacia = []

# Para agregar un elemento a una lista se utiliza el metodo append()

lista_vacia.append(1) # Agrega el numero 1 al final de la lista

# Las listas pueden contener distintos tipos de datos

lista = [1, 2, 3, "Hola", "Mundo", True, False]

# Incluso una segunda lista

lista = [1, 2, 3, [4, 5, 6]]

# Ahora depende de nosotros como utilizarlas, por ejemplo podemos crear una serie de listas que sean un alumno de su curso y sus notas (nombre, apellido, curso, notas)

alumno1 = ["Juan", "Perez", "4to", [5.5, 6.0, 4.5, 7.0]]
alumno2 = ["Maria", "Gonzalez", "4to", [4.5, 6.0, 4.5, 7.0]]
alumno3 = ["Pedro", "Gonzalez", "4to", [5.5, 6.0, 4.5, 7.0]]

# Y eso incluso lo podemos poner en otra lista, pero eso ya es más avanzado en cuanto a su uso en algoritmos.

alumnos = [alumno1, alumno2, alumno3]

# Ahora que ya entendemos listas y como utilizarlas, veamos algunos ejercicios.

# Ejercicio 0: Crear una función que devuelva una lista con n numeros entre min y max. Los numeros deben ser aleatorios.

import random

def crear_lista(n, min, max):
    lista = []
    for i in range(n):
        # Append agrega un elemento al final de la lista
        lista.append(random.randint(min, max))
    return lista

lista = crear_lista(10, 1, 100)

# Existen 3 formas de recorrer la lista, la primera es con un ciclo for y range, la segunda es solo con ciclo for y la tercera es con un ciclo while.

# for y range

def recorrer_lista_for_y_range(lista):
    print("Recorrido con for y range")
    for i in range(len(lista)):
        print(lista[i])

def recorrer_lista_for(lista):
    print("Recorrido con for")
    for elemento in lista:
        print(elemento)

def recoorer_lista_while(lista):
    print("Recorrido con while")
    i = 0
    while i < len(lista):
        print(lista[i])
        i += 1


# Algunos comandos utiles para la utilizacion de listas son: append(), insert(),remove(), pop(), index(), len(), reverse(), copy()

# Append()

lista = [1, 2, 3]

lista.append(4) # Agrega el numero 4 al final de la lista

print(lista)

# Insert()

lista.insert(0, 0) # Agrega el numero 0 en la posicion 0 de la lista
lista.insert(2, 3) # Agrega el numero 1.5 en la posicion 2 de la lista

# Al usar insert el resto de los elementos se corren hacia la derecha

print(lista)

# Remove()

lista.remove(3) # Elimina el primer elemento que sea igual a 3

print(lista)

# Pop()

lista.pop() # Elimina el ultimo elemento de la lista

print(lista)

lista.pop(1) # Elimina el elemento en la posicion 1 de la lista

print(lista) 
# Los elementos a la derecha de la posicion eliminada se corren hacia la izquierda

# Index()

print(lista.index(2)) # Imprime el indice del primer elemento que sea igual a 2

# Len()

print(len(lista)) # Imprime el largo de la lista

# Reverse()

lista.reverse() # Invierte el orden de los elementos de la lista

print(lista)

# El reverse es permanente, si queremos volver a invertir la lista debemos volver a utilizar el comando

# Copy()

lista2 = lista.copy() # Copia todos los elementos de la lista en una nueva lista


