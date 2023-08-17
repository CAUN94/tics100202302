# Importamos el modulo time
import time

# Ejemplo 1: Medir el tiempo que el usuario tarda en responder 3 preguntas:

# Definimos la funcion
def hacer_preguntas():
    # Usamos la funcion time() para obtener el tiempo actual
    start_time = time.time()

    # Hacemos las preguntas
    pregunta1 = input("¿Cuál es tu color favorito? ")
    pregunta2 = input("¿Qué te gusta hacer en tu tiempo libre? ")
    pregunta3 = input("¿Cuál es tu película favorita? ")

    # Usamos la funcion time() para obtener el tiempo actual
    end_time = time.time()

    # Calculamos el tiempo transcurrido
    tiempo_transcurrido = end_time - start_time

    # Imprimimos el tiempo transcurrido y usamos round para redondear el numero a 2 decimales
    print(f"Te tomó {round(tiempo_transcurrido,2)} segundos responder las preguntas")

# Llamamos a la funcion
hacer_preguntas()

# Ejemplo 2: Esperar un tiempo determinado para mostrar una palabra

def esperar_palabras():

    # Pedimos la primera palabra, el tiempo de espera y la segunda palabra
    primera_palabra = input("Ingresa la primera palabra: ")
    tiempo_espera = int(input("Ingresa el tiempo en segundos: "))
    segunda_palabra = input("Ingresa la segunda palabra: ")
    
    print(primera_palabra)

    # Usamos la funcion sleep() para esperar el tiempo ingresado, este tiempo debe ser en segundos.
    time.sleep(tiempo_espera)

    print(segunda_palabra)

esperar_palabras()


# Ejemplo 3: Calcular la edad de una persona a partir de su fecha de nacimiento:

# Definimos la funcion y sus 4 parametros
def calcular_edad(nombre, dia_nacimiento, mes_nacimiento, anio_nacimiento):

    # Usaremos la funcion mktime() que devuelve el valor en segundos de la fecha entregada, en este caso de la fecha actual usando localtime()
    fecha_actual = time.mktime(time.localtime())

    # Usamos la funcion mktime() para convertir los valores entregados en un objeto de tiempo, en este caso la fecha de nacimiento, se agregan ceros a los valores que no se necesitan, que son los de hora, minuto, segundo, dia de la semana, dia del año y horario de verano, 
    fecha_nacimiento = time.mktime((anio_nacimiento, mes_nacimiento, dia_nacimiento, 0, 0, 0, 0, 0, 0))

    # Calculamos la edad en segundos
    edad = fecha_actual - fecha_nacimiento

    # Mostremos la edad en segundos
    print(f"Edad en segundos: {edad}")

    # Para convertir la edad en segundos a años, dividimos por 60 para obtener los minutos, por 60 para obtener las horas, por 24 para obtener los dias y por 365 para obtener los años

    edad_anios = edad / 60 / 60 / 24 / 365

    # Imprimimos la edad en años redondeada a 1 decimal
    print(f"La edad de {nombre} es {round(edad_anios,1)} años")


nombre = input("Ingresa tu nombre: ")
dia = int(input("Ingresa el día de tu nacimiento: "))
mes = int(input("Ingresa el mes de tu nacimiento: "))
anio = int(input("Ingresa el año de tu nacimiento: "))

calcular_edad(nombre, dia, mes, anio)

