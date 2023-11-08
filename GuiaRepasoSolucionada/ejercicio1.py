# Suma de Números Impares: Escriba un programa que cree una lista con N numeros aleatorios entre 1 y 1000 y que calcule la suma de todos los numeros impares de la lista.

import random

# Función que recibe una lista y retorna la suma de los números impares
def sumaImpares(lista):
    # Variable que almacena la suma de los números impares
    suma = 0
    # Recorremos la lista
    for i in lista:
        # Si el número es impar, lo sumamos
        if i % 2 != 0:
            # Sumamos el número a la variable suma
            suma += i
    # Retornamos la suma
    return suma

# Función que recibe un número n y retorna una lista de n números aleatorios entre 1 y 1000
def crearLista(n):
    # Lista que almacenará los números aleatorios
    lista = []
    # Recorremos n veces
    for i in range(n):
        # Agregamos un número aleatorio entre 1 y 1000 a la lista
        lista.append(random.randint(1, 1000))
    # Retornamos la lista
    return lista

# Pedimos al usuario la cantidad de números a generar
n = int(input("Ingrese la cantidad de números a generar: "))
# Creamos la lista usando la función crearLista
lista = crearLista(n)
# Mostramos la lista generada
print("Lista generada: ", lista)

# Mostramos la suma de los números impares usando la función sumaImpares
print("La suma de los números impares es: ", sumaImpares(lista))