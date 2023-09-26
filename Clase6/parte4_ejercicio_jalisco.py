import random, time
from os import system
def generar_numero_secreto():
    return random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100

def adivinar_numero_secreto(numero_secreto):
    intentos = 0
    final = 0
    while final == 0:
        system("cls")
        numero = int(input("Adivina el número secreto (entre 1 y 100): "))
        intentos += 1
        if numero == numero_secreto:
            print(f"¡Correcto! ¡Adivinaste el número secreto {numero_secreto} en {intentos} intentos!")
            break
        elif numero < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
        time.sleep(2)
        
            


# Llamamos a la función principal para iniciar el juego
print("Bienvenido al juego 'Adivina el Número Secreto'")
print("Estoy pensando en un número entre 1 y 100.")
time.sleep(2)
numero_secreto = generar_numero_secreto()
adivinar_numero_secreto(numero_secreto)