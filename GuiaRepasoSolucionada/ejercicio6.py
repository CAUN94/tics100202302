# Aprendiendo a Sumar: Crea una funcion que le pida la suma de 2 numeros aleatorios a una persona, si hace bien la suma sigue jugando en caso contrario se termina el juego. Además el juego tiene un maximo de 5 segundos para responder, si no responde en ese tiempo se termina el juego.

import random
import time

# Función que recibe dos números y retorna la suma de ambos
def suma(a, b):
    return a + b

# Función que recibe tres números y retorna True si la suma de los dos primeros es igual al tercero, False en caso contrario
def verificarSuma(a, b, c):
    return suma(a, b) == c

while True:
    # Generamos dos números aleatorios entre 1 y 100
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    
    # Mostramos la suma de los números
    print("Suma: ", a, "+", b)
    
    # Variable que almacenará la respuesta del usuario
    respuesta = int(input("Ingrese la respuesta: "))
    
    # Variable que almacenará el tiempo actual
    tiempo = time.time()
    
    # Si la respuesta es correcta y el tiempo es menor a 5 segundos, el usuario sigue jugando
    if verificarSuma(a, b, respuesta) and time.time() - tiempo < 5:
        print("Correcto!")
    # Si la respuesta es incorrecta o el tiempo es mayor a 5 segundos, el usuario pierde
    else:
        print("Perdiste!")
        break