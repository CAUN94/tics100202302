# Ahora que ya recordamos como funciona lista vamos a resolver los siguientes ejercicios, tendremos como base la funcion de listas random que hicimos en la clase anterior.

import random

def crear_lista(n, min, max):
    lista = []
    for i in range(n):
        # Append agrega un elemento al final de la lista
        lista.append(random.randint(min, max))
    return lista

# Ejercicio 1, crear una lista con 40 numeros aleatorios entre 1 y 7 que representan las notas finales de un curso y entregar la lista de todos los estudiantes que aprobaron agregando un mensaje que diga aprobado con exelecia si la nota es igual o superior a 6 y aprobado si la nota es menor a 6 y superior o igual a 4. Los estudiantes que reprobaron no se consideran.
# El outpot debe verse así
# Estudiante 1: 5.0 - Aprobado
# Estudiante 2: 6.2 - Aprobado con exelencia
# Estudiante 3: 4.5 - Aprobado

# hint: el numero de estudiante se puede obtener con el indice de la lista + 1

def aprobar_curso(lista):
    for i in range(len(lista)):
        if lista[i] >= 6:
            print(f"Estudiante {i+1}: {lista[i]} - Aprobado con exelencia")
        elif lista[i] >= 4:
            print(f"Estudiante {i+1}: {lista[i]} - Aprobado")

aprobar_curso(crear_lista(40, 1, 7))

# Ejercicio 2: Crear una funciono que reciba una lista con 100 numeros aleatorios entre 1 y 100 y además se le entreguen 2 numeros, la funcion debe mostrar todos los numeros de la lista e indicar cuales son divisibles por el primer numero y que no sean divisibles por el segundo numero.

def dividir_lista(lista, divisor1, divisor2):
    for i in range(len(lista)):
        if lista[i] % divisor1 == 0 and lista[i] % divisor2 != 0:
            print(f"{lista[i]} es divisible por {divisor1} y no es divisible por {divisor2}")
        else:
            print(lista[i])

dividir_lista(crear_lista(100, 1, 100), 3, 5)

# Ejercicio 3: Crear una funcion que le pida al usuario numeros con la condición de que este debe ser primo, en caso de que se cumpla esta condición el numero se agregara a una lista, en caso contrario se le pedira al usuario que ingrese otro numero. El usuario debe ingresar numeros hasta que la suma de todos los elemntos de la lista llegue a 30. En cada iteración se debe mostrar un print de la lista y cuantos numeros faltan para llegar a 30.

def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
    
def sumar_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def crear_lista_primos():
    lista = []
    while sumar_lista(lista) < 30:
        numero = int(input("Ingrese un numero: "))
        if es_primo(numero):
            lista.append(numero)
            print(lista)
            print(f"Faltan {30 - sumar_lista(lista)} para llegar a 30")
        else:
            print("El numero no es primo")
    return lista

crear_lista_primos()

# Ejercicio 4: Tenemos una lista que representa las notas de un curso, pero por un error de tipeo muchas notas quedaron por sobre 7. Haga una función que arrgle esto, para esto debe recorrer la lista y en caso de que la nota sea mayor a 7 debe cambiarla por 7. La función debe retornar la lista arreglada.

def arreglar_notas(lista):
    print(lista)
    for i in range(len(lista)):
        if lista[i] > 7:
            lista[i] = 7
    return lista

print(arreglar_notas(crear_lista(40, 1, 10)))

# Ejercicio 5: Haga lo mismo que en el problema anterior, pero en vez de cambiar la nota debe remover ese numero de la lista y devolver la lista nueva.

def borra_notas(lista):
    print(lista)
    for i in range(len(lista)):
        if lista[i] > 7:
            lista.remove(lista[i])
    return lista

print(borra_notas(crear_lista(40, 1, 10)))

#  Crea una funciono que entregue una lista con n numeros con numeros flooatt aleatorios entre a y b



