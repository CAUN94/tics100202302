# Crear un archivo csv

import csv

# Para crear un archivo csv debo usar el comando 'a' y csv

# Si el archivo no existe, se creará uno nuevo
# Si el archivo existe, se agregaran lineas al final del archivo

archivo = open('estudiantes_lista.csv', 'a')

# Escribimos una linea en el archivo
linea = '12345678-9,Jose,Jose,20,4,Ingenieria Civil Informatica\n'
archivo.write(linea)

# Otra linea
linea = '12345678-8,Claudio,Claudio,10,4,Ingenieria Civil Civil\n'
archivo.write(linea)

# el \n es para que se escriba la linea en una nueva linea (es un salto de linea)

# Cerrar el archivo
archivo.close()

# Separar los datos de una linea de un archivo csv
datos = linea.split(',')
print(datos)

# Unir datos
linea = ','.join(datos)