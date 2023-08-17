# Los módulos en Python son archivos que contienen definiciones de funciones y clases.
# Ayudan a organizar y reutilizar el código de manera eficiente. Los módulos son esenciales para acceder a funcionalidades que no están disponibles en python.
# Basicamente es una forma de re utilizar codigo creado por otros en forma rapida.
# Más o menos lo mismo que cuando a Neo le enseñan Kung Fu en la Matrix insetandole un chip, que en este caso llamamos modulo.

# Para importar un modulo se usa la palabra reservada import seguida del nombre del modulo.

# Por ejemplo si necesiamos saber la hora podemos llamar al modulo time

# Importamos el modulo time
import time

# Para ordenar nuestro codigo crearemos una funcion llamada obtener_hora_actual()

# Definimos la funcion
def obtener_hora_actual():
    # Usamos la variable time y llamamos a la funcion localtime() que nos devuelve la hora actual
    # Esta la almacenamos en la variable hora_actual
    hora_actual = time.localtime()

    # localtime() nos entrega la hora actual, pero en un formato que no es muy legible
    print("La hora actual sin formao es:", hora_actual)

    # Para darle un formato mas legible usamos la funcion strftime() que nos permite darle un formato a la hora, en este caso en formatto hora, minutos y segundos

    hora_formateada = time.strftime("%H:%M:%S", hora_actual)

    # Retornamos la hora actual
    return hora_formateada

# Imprimimos la hora actual
print("La hora actual es:", obtener_hora_actual())


