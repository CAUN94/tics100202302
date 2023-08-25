# En esta clase, exploraremos los conceptos fundamentales de control de flujo en Python, incluyendo el uso de las declaraciones if, elif y else, así como los operadores de comparación. También abordaremos el uso de los módulos random, time y math para realizar diversas operaciones y toma de decisiones basadas en condiciones.

# Parte 1: if

# Paso a Paso: Uso de if con funciones

# Definir la Función: Comienza definiendo una función en Python. Puedes darle un nombre relevante que describa la tarea que realizará la función.

def ejemploif(nr):
    # Definir las Condiciones: Dentro de la función, usa la declaración if seguida de una expresión condicional. Esta expresión se evalúa para determinar si es verdadera o falsa. Si es verdadera, el bloque de código indentado debajo del if se ejecutará.

    # Ejemplo: Si el número es mayor que 0, imprime un mensaje que indica que el número es positivo.

    if nr > 0:
        print("El número es positivo")

    # Ejemplo: Si el número es menor que 0, imprime un mensaje que indica que el número es negativo.

    if nr < 0:
        print("El número es negativo")

    # Ejemplo: Si el número es igual a 0, imprime un mensaje que indica que el número es cero.

    if nr == 0:
        print("El número es cero")

ejemploif(5)
ejemploif(-15)
ejemploif(0)