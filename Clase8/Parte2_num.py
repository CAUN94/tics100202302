# Numpy tiene muchas herramientas que nos podran ayudar
# encontrar el mayor o menor elemento de un arreglo, 
# multiplicar todos los numeros de un arreglo, calcular promedio, entre otros

# Utilicemos numpy para crear un arreglo y veamos que podemos hacer:
import numpy

datos = numpy.random.randint(0,100,5) #creamos un arreglo de 5 elementos con numeros entre 0 y 99
print(datos)
print(datos.min()) #imprime el menor valor
print(datos.max()) #imprime el mayor valor
print(datos.sum()) #imprime la suma de todos los valores
print(datos.mean()) #imprime el promedio del arreglo
print(datos.prod()) #imprime la multiplicacion de todos los elementos del arreglo

# Entonces estamos listos para hacer algunos ejercicios.
import numpy as np

# Función para obtener las notas de los estudiantes
def obtener_notas():
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    notas = np.zeros(cantidad_estudiantes)
    for i in range(0,cantidad_estudiantes):
        nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
        notas[i] = nota
    return notas

# Función para calcular estadísticas
def calcular_estadisticas(notas):
    promedio_general = np.mean(notas)
    promedio_mas_alto = np.max(notas)
    promedio_mas_bajo = np.min(notas)
    print("Promedio general del curso:", promedio_general)
    print("Promedio más alto:", promedio_mas_alto)
    print("Promedio más bajo:", promedio_mas_bajo)
 
print("Bienvenidos al calculador de promedios!")
notas = obtener_notas()





