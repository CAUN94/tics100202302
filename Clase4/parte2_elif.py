# Parte 2: if y elif con funciones

# La declaración elif es una abreviatura de "else if", lo que significa que permite agregar condiciones adicionales después de un if para evaluar diferentes casos en secuencia. Si la condición en el if no es verdadera, se verifica la siguiente condición en el bloque elif. Si esa condición es verdadera, el bloque de código dentro del elif se ejecutará. 

# Ejemplo: Clasificación de Edades

# Supongamos que queremos crear una función que clasifique edades en diferentes grupos. Utilizaremos la declaración elif para establecer diferentes rangos de edades y proporcionar una clasificación para cada rango. Aquí está el ejemplo:

# Definimos la función con el parametro edad
def clasificar_edad(edad):

    # Si la edad es menor que 13, imprime un mensaje que indica que la persona es un niño.
    if edad < 13:
        print("Eres un niño.")

    # En caso de que la edad sea mayor o igual a 13, se evalúa la siguiente condición, en este caso vemos si la edad es menor que 20.
    elif edad < 20:
        print("Eres un adolescente.")

    # Igual que antets, si la edad es mayor o igual a 20, se evalúa la siguiente condición, en este caso vemos si la edad es menor que 60.
    elif edad < 60:
        print("Eres un adulto.")

    # Como ultima condición, si la edad es mayor o igual a 60, se imprime un mensaje que indica que la persona es un adulto mayor.

    elif edad >= 60:
        print("Eres un adulto mayor.")

    # Si ninguna de las condiciones anteriores es verdadera se llega al final de la función y no se imprime nada

# Llamada a la función
clasificar_edad(8)    # Salida: Eres un niño.
clasificar_edad(16)   # Salida: Eres un adolescente.
clasificar_edad(45)   # Salida: Eres un adulto.
