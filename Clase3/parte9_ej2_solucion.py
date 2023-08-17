# Ejercicio 2: Crear 2 números aleatorios que son catetos y calcular su hipotenusa:

# Crea un programa que genere dos números aleatorios que representan los catetos de un triángulo rectángulo. Luego, utiliza el módulo math para calcular la hipotenusa de ese triángulo y muestra los catetos generados junto con la hipotenusa calculada.

import math
import random

def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return round(hipotenusa,2)

cateto1 = random.randint(1, 10)
cateto2 = random.randint(1, 10)
print(f"Catetos aleatorios: {cateto1}, {cateto2}")

hipotenusa_calculada = calcular_hipotenusa(cateto1, cateto2)
print(f"La hipotenusa del triángulo es: {hipotenusa_calculada}")