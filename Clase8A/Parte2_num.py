# Numpy tiene muchas herramientas que nos podran ayudar
# encontrar el mayor o menor elemento de un arreglo, 
# multiplicar todos los numeros de un arreglo, calcular promedio, entre otros

# Utilicemos numpy para crear un arreglo y veamos que podemos hacer:

import numpy as np

datos = np.random.randint(0,101,[5])

print(datos)
# Minimo
print(np.min(datos))
# Maximo
print(np.max(datos))
# Suma
print(np.sum(datos))
# Promedio
print(np.mean(datos))
# Productoria
print(np.prod(datos))

def obtener_notas():
    cantidad_estudiantes = int(input("Ingrese cantidad de estudiantes: "))
    notas = np.zeros(cantidad_estudiantes)
    print(notas)
    for i in range(cantidad_estudiantes):
        nota = float(input("Ingrese nota: "))
        notas[i] = nota
    print(notas)
    return notas

def calcular_estadisticas(notas):
    promedio_general = np.mean(notas)
    promedio_mas_alto = np.max(notas)
    promedio_mas_bajo = np.min(notas)
    print("Promedio general: ", promedio_general)
    print("Promedio mas alto: ", promedio_mas_alto)
    print("Promedio mas bajo: ", promedio_mas_bajo)

notas = obtener_notas()
calcular_estadisticas(notas)