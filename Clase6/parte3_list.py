# Lass listas son un tipo de dato que nos permite almacenar varios valores
# Por Ejemplo
# Nombre de los alumnos de un curso
# Nota de los alumnos de un curso
# Puntos de la prueba de un alumno

# Veamos como estas funciona en Python
# Para crear una lista se utilizan los corchetes [ ]

lista = [] # Esta es una lista vacia

lista = [1,2,3,4,5] # Esta es una lista con 5 elementos

lista = [1,2,3,4,5,"Hola","Mundo"] # Esta es una lista con 7 elementos

# Para acceder a los elementos de una lista se utiliza el indice

print(lista[0]) # Imprime el primer elemento de la lista (1)
print(lista[1]) # Imprime el segundo elemento de la lista (2)
print(lista[2]) # Imprime el tercer elemento de la lista (3)
print(lista[3]) # Imprime el cuarto elemento de la lista (4)
print(lista[4]) # Imprime el quinto elemento de la lista (5)
print(lista[5]) # Imprime el sexto elemento de la lista (Hola)
print(lista[6]) # Imprime el septimo elemento de la lista (Mundo)

# Como podemos ver el indice de una lista comienza en 0 y termina en n-1, donde n es el largo de la lista

# Para saber el largo de una lista se utiliza la funcion len()
print(len(lista)) # Imprime 7

# Para agregar un elemento a una lista se utiliza el metodo append()

lista.append(8) # Agrega el numero 8 al final de la lista

print(lista) # Imprime [1,2,3,4,5,"Hola","Mundo",8]
print(lista[7]) # Imprime el octavo elemento de la lista (8)

# En webc hay un pdf con comandos utiles para trabajar con listas, por ahora estos son los que necesitamos

# Ejemplo 1: Recorrer una lista con un ciclo for

def recorrer_lista(lista):
    for elemento in range(len(lista)):
        # imprime indice y elemento
        print(elemento, lista[elemento]) # Ahora se entiende porque el rangr parte de 0

lista = [1,2,3,4,5,"Hola","Mundo",8]
# recorrer_lista(lista)

# Ejemplo 2: Agregar valores numericos a una lista hasta ingresar -1

def agregar_valores():
    lista = []
    valor = int(input("Ingrese un valor: "))
    while valor != -1:
        lista.append(valor)
        valor = int(input("Ingrese un valor: "))
    print(lista)

# agregar_valores()

# Ejemplo 3: Generar una lista con 10 valores aleatorios entre 1 y 20, despues entregar a esta lista y que el usuario entregue un numero y se verifique si existe en la lista, en caso de que exista entregar la posición, en caso contrario entregar un mensaje que diga que no existe (si hay más de un numero debe indicar la posición de todos)

import random

def generar_lista():
    lista = []
    for i in range(10):
        lista.append(random.randint(1,20))
    return lista

def buscar_numero(lista):
    numero = int(input("Ingrese un numero: "))
    numero_existe = False
    for i in range(len(lista)):
        if lista[i] == numero:
            print(f"El numero {numero} se encuentra en la posicion {i}")
            numero_existe = True

    if numero_existe == False:
        print(f"El numero {numero} no existe en la lista")

lista = generar_lista()
print(lista)
buscar_numero(lista)





