# Es muy comun el trabajo con archivos csv (comma separated values) o txt (texto plano) en python.

# Partiremos trabajando con un archivo csv simple

import csv

# Abrimos el archivo en modo lectura el archiivo estudiantes.csv (que se encuentra en la misma carpeta que este archivo)

# La r es por modo lectura


# Leemos el archivo linea por linea usando while y el metodo readlines(), usaremos el metodo split para separar los valores por comas y los guardaremos en una lista

def revisar_csv(archivo):
    estudiantes = []

    while True:
        linea = archivo.readline()
        if not linea:
            break
        estudiantes.append(linea.split(','))

    return estudiantes


# Ahora que tenemos los datos en una lista, podemos trabajar con ellos, en este caso contaremos cuantos estudiantes aprobaron el ramo
def contar_aprobados(estudiantes):
    aprobados = 0

    if not estudiantes:
        print("No se encontraron datos de estudiantes.")
        return 0

    # Suponemos que la primera fila contiene los nombres de las columnas
    encabezados = estudiantes[0]
    columna_promedio = None

    if "Promedio_final" in encabezados:
        columna_promedio = encabezados.index("Promedio_final")
    else:
        print("No se encontró la columna 'Promedio_final' en el archivo.")
        return 0

    for estudiante in estudiantes[1:]:  # Empezamos desde la segunda fila
        promedio = estudiante[columna_promedio]
        if int(promedio) >= 4.0:  # Asegura que promedio no esté vacío
            aprobados += 1

    return aprobados

# Ahora que ya sabemos como leer un archivo csv, podemos crear uno nuevo con los datos que queramos

def crear_csv(estudiantes):
    # Tomaremos la lista de todos los estudiantes y crearemos un archivo csv con los estudiantes que aprobaron el ramo
    # Y en la ultima linea del archivo pondremos la cantidad de estudiantes aprobados y el promedio de notas de los estudiantes aprobados

    # Abrimos el archivo en modo escritura
    archivo = open('estudiantes_aprobados.csv', 'w')

    # Escribimos el encabezado del archivo
    archivo.write('Rut,Nombre,Apellido,Edad,Promedio_final,Carrera\n')

    # Escribimos los datos de los estudiantes
    aprobados = contar_aprobados(estudiantes)

    # Escribimos los datos de los estudiantes aprobados desde la segunda fila
    for estudiante in estudiantes[1:]:
        if int(estudiante[4]) >= 4.0:
            # Usamos join para unir los datos de cada estudiante con una coma entre ellos (contrario a split) y escribimos la linea en el archivo
            archivo.write(','.join(estudiante))
    
    # Escribimos la cantidad de estudiantes aprobados y el promedio de notas de los estudiantes aprobados

    archivo.write(f'\n{aprobados},{round(aprobados/len(estudiantes), 2)}')


    


archivo = open('estudiantes.csv', 'r')

estudiantes = revisar_csv(archivo)

print(estudiantes[0])

aprobados = contar_aprobados(estudiantes)

print(f"La cantidad de estudiantes aprobados es: {aprobados}")

crear_csv(estudiantes)









