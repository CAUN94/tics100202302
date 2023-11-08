# Conjetura de Collatz: La conjetura de Collatz es una hipótesis matemática que aún no ha sido demostrada. Crear un programa en Python que aplique la Conjetura de Collatz a un número ingresado por el usuario y cuente la cantidad de iteraciones necesarias para que ese número llegue a 1.

# Función que recibe un número n y retorna la cantidad de iteraciones necesarias para que llegue a 1
# La conjetura se define como:
# Si el número es par, se divide entre 2
# Si el número es impar, se multiplica por 3 y se le suma 1
# Se repite esto hasta que el número llegue a 1

def collatz(n):
    # Variable que almacenará la cantidad de iteraciones
    iteraciones = 0
    # Mientras el número sea distinto de 1
    while n != 1:
        # Si el número es par, se divide entre 2
        if n % 2 == 0:
            n //= 2
        # Si el número es impar, se multiplica por 3 y se le suma 1
        else:
            n = n * 3 + 1
        # Aumentamos la variable iteraciones en 1
        iteraciones += 1
    # Mostramos la cantidad de iteraciones
    print("Cantidad de iteraciones: ", iteraciones)

n = int(input("Ingrese un número: "))
collatz(n)