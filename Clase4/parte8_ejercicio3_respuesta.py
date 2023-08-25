import time

def saludo_según_hora():
    hora_actual = time.localtime().tm_hour
    
    if 5 <= hora_actual < 12:
        print("¡Buenos días!")
    elif 12 <= hora_actual < 18:
        print("¡Buenas tardes!")
    else:
        print("¡Buenas noches!")

# Llamada a la función
saludo_según_hora()
