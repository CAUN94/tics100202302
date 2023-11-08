import csv
from faker import Faker

fake = Faker()

# Crear una lista de diccionarios con datos ficticios de estudiantes
data = []
for _ in range(1000):
    estudiante = {
        'Rut': fake.unique.random_number(digits=8),
        'Nombre': fake.first_name(),
        'Apellido': fake.last_name(),
        'Edad': fake.random_int(min=18, max=30),
        'Promedio_final': fake.random_int(min=1, max=7),
        'Carrera': fake.job(),
        
    }
    data.append(estudiante)

# Guardar los datos en un archivo CSV
with open('lista_estudiantes.csv', 'w', newline='') as archivo_csv:
    campos = ['Rut', 'Nombre', 'Apellido', 'Edad', 'Promedio_final', 'Carrera']
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

    # Escribir el encabezado del archivo CSV
    escritor_csv.writeheader()

    # Escribir los datos de los estudiantes
    escritor_csv.writerows(data)