import random

# Definimos la funcion generar_numero_aleatorio()
def generar_numero_aleatorio():
    # Pedimos el valor minimo y maximo
    minimo = int(input("Ingresa el valor mínimo: "))
    maximo = int(input("Ingresa el valor máximo: "))
    # Usamos la funcion randint() del modulo random para generar un numero aleatorio entre el valor minimo y maximo
    numero_aleatorio = random.randint(minimo, maximo)
    # Retornamos el numero aleatorio
    return numero_aleatorio

# Llamamos a la funcion y guardamos el resultado en la variable resultado
resultado = generar_numero_aleatorio()
print(f"El número aleatorio es: {resultado}")

# Ejemplo 2: Lanzar un dado y mostrar el resultado:

# Definimos la funcion lanzar_dado()
def lanzar_dado():
    # Usamos la funcion randint() del modulo random para generar un numero aleatorio entre 1 y 6
    resultado = random.randint(1, 6)
    # Retornamos el resultado
    return resultado

# Llamamos a la funcion y guardamos el resultado en la variable valor_dado
valor_dado = lanzar_dado()
print(f"El resultado del lanzamiento del dado es: {valor_dado}")
