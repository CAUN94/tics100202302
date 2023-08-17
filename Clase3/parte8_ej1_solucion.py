# Ejercicio 1: Calcular la edad a partir de una fecha aleatoria de nacimiento:

# Diseña un programa que genere de manera aleatoria un día entre 1 y 29, un mes entre 1 y 12, y un año entre 1900 y el año actual, para representar la fecha de nacimiento de una persona. Luego, solicita al usuario ingresar su nombre. Utiliza la función calcular_edad proporcionada en los ejemplos para calcular la edad de la persona en años y muestra la fecha aleatoria generada, el nombre ingresado y la edad calculada.

import math
import time
import random

def calcular_edad(nombre, dia_nacimiento, mes_nacimiento, anio_nacimiento):
    fecha_actual = time.mktime(time.localtime())
    fecha_nacimiento = time.mktime((anio_nacimiento, mes_nacimiento, dia_nacimiento, 0, 0, 0, 0, 0, 0))
    edad = fecha_actual - fecha_nacimiento
    edad_anios = edad / 60 / 60 / 24 / 365
    print(f"La edad de {nombre} es {round(edad_anios, 1)} años")

dia_aleatorio = random.randint(1, 29)
mes_aleatorio = random.randint(1, 12)
anio_aleatorio = random.randint(1900, time.localtime().tm_year)
print(f"Fecha aleatoria de nacimiento: {dia_aleatorio}/{mes_aleatorio}/{anio_aleatorio}")

nombre_persona = input("Ingresa tu nombre: ")
calcular_edad(nombre_persona, dia_aleatorio, mes_aleatorio, anio_aleatorio)
