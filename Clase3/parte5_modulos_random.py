# Módulo random:
# El módulo random se utiliza para generar números aleatorios. Veamos cómo obtener un número entero aleatorio y un número decimal aleatorio.

# Importamos el modulo random
import random

# Definimos la funcion generar_numero_aleatorio()
def generar_numero_aleatorio():
    # Usamos la funcion randint() del modulo random para generar un numero aleatorio entre 1 y 100
    return random.randint(1, 100)

# Definimos la funcion generar_numero_decimal_aleatorio()
def generar_numero_decimal_aleatorio():
    # Usamos la funcion uniform() del modulo random para generar un numero decimal aleatorio entre 0 y 1, estos numeros siempre tienen 16 digitos y siguen la distribucion uniforme
    return random.uniform(0, 1)

print(f"Número aleatorio: {generar_numero_aleatorio()}")
print(f"Número decimal aleatorio: {generar_numero_decimal_aleatorio()}")
