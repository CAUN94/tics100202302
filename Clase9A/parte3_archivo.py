#  Es muy coomun en pythoon el trabajo coon archivos ya sea csv o txt

import csv

# Abrimos el archivo en modo lectura el archiivo estudiantes.csv (que se encuentra en la misma carpeta que este archivo)

# La r es por modo lectura

# Leemos el archivo linea por linea usando while y el metodo readlines(), usaremos el metodo split para separar los valores por comas y los guardaremos en una lista

def leer_archivo(archivo):
    estudiantes = []
    while True:
        linea = archivo.readline()
        if not linea:
            break
        estudiantes.append(linea.split(','))
    
    return estudiantes

# Ahora que tenemos los datos en una lista, podemos trabajar con ellos, en este caso contaremos cuantos estudiantes aprobaron el ramo
def contar_aprobados(estudiantes):
    cont = 0
    for i in range(1,len(estudiantes)):
        nota = int(estudiantes[i][4])
        if nota >= 4:
            cont += 1
    print(cont)
    
archivo = open('estudiantes.csv','r')
estudiantes = leer_archivo(archivo)
contar_aprobados(estudiantes)

with open('estudiantes.csv','a') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['18783422','Nacho','Ugarte','28','2','ING TI'])

