# Crear una torre: Usando 2 ciclos for debe crear la siguiente torre con *:
#    *
#   ***
#  *****
# El alto de la torre debe ser ingresado por el usuario.

# Función que recibe el alto de la torre y la imprime
def crearTorre(alto):
    # Recorremos desde 1 hasta el alto de la torre
    for i in range(1, alto + 1):
        # Imprimimos los espacios en blanco
        for j in range(alto - i):
            print(" ", end="")
        # Imprimimos los asteriscos
        for j in range(2 * i - 1):
            print("*", end="")
        # Imprimimos un salto de línea
        print()

# Pedimos al usuario el alto de la torre
alto = int(input("Ingrese el alto de la torre: "))