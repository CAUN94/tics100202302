import random

def comparar_numero_aleatorio():
    numero_aleatorio = random.randint(1, 100)
    numero_ingresado = int(input("Ingresa un número: "))
    
    if numero_ingresado > numero_aleatorio:
        print("El número ingresado es mayor que el número aleatorio.")
    elif numero_ingresado < numero_aleatorio:
        print("El número ingresado es menor que el número aleatorio.")
    else:
        print("¡Adivinaste el número aleatorio!")

# Llamada a la función
comparar_numero_aleatorio()
