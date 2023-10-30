# Revisión de datos: Cree una lista vacia que pedira al usuario que ingrese datos hasta que se cumplan las siguientetes condiciones: "Tener al menos 3 numeros primos", "Que la suma total de los numeros sea mayor a 100" y "Que 2 numeros consecutivos sean iguales". Al finalizar, muestre la lista.

# Función que recibe un número n y retorna True si es primo, False en caso contrario
def primo(n):
    # Si el número es 1, retornamos False
    if n == 1:
        return False
    # Si el número es 2, retornamos True
    if n == 2:
        return True
    # Recorremos los números desde 2 hasta n - 1
    for i in range(2, n):
        # Si el número es divisible por i, retornamos False
        if n % i == 0:
            return False
    # Si no se cumple ninguna de las condiciones anteriores, retornamos True
    return True

# Funcion que recibe una lista y retorna True si hay al menos 3 números primos, False en caso contrario

def alMenos3Primos(lista):
    # Variable que almacenará la cantidad de números primos
    primos = 0
    # Recorremos la lista
    for i in lista:
        # Si el número es primo, aumentamos la variable primos en 1
        if primo(i):
            primos += 1
    # Si la variable primos es mayor o igual a 3, retornamos True
    if primos >= 3:
        return True
    # Si no se cumple la condición anterior, retornamos False
    return False

# Función que recibe una lista y retorna True si la suma de los números es mayor a 100, False en caso contrario

def sumaMayor100(lista):
    # Variable que almacenará la suma de los números
    suma = 0
    # Recorremos la lista
    for i in lista:
        # Sumamos el número a la variable suma
        suma += i
    # Si la suma es mayor a 100, retornamos True
    if suma > 100:
        return True
    # Si no se cumple la condición anterior, retornamos False
    return False

# Función que recibe una lista y retorna True si hay 2 números consecutivos iguales, False en caso contrario

def consecutivosIguales(lista):
    # Recorremos la lista desde el segundo elemento hasta el último
    for i in range(1, len(lista)):
        # Si el elemento actual es igual al anterior, retornamos True
        if lista[i] == lista[i - 1]:
            return True
    # Si no se cumple la condición anterior, retornamos False
    return False

# Funcion que crea una lista vacia y pide al usuario que ingrese datos hasta que se cumplan las condiciones
def revision():
    lista = []
    while True:
        # Pedimos al usuario un número
        n = int(input("Ingrese un número: "))
        
        lista.append(n)

        # Si la lista tiene al menos 3 números primos, la suma de los números es mayor a 100 y hay 2 números consecutivos iguales, retornamos la lista

        if alMenos3Primos(lista) and sumaMayor100(lista) and consecutivosIguales(lista):
            return lista
        
# Llamamos a la función revision y mostramos la lista
revision()

        
