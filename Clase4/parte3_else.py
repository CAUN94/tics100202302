# Parte 3: Uso de if, elif y else con funciones

# La declaración else se utiliza para definir un bloque de código que se ejecutará cuando ninguna de las condiciones previas (if o elif) sea verdadera. En otras palabras, el bloque de código dentro de else se ejecutará si ninguna de las condiciones anteriores se cumple.

# En este caso evaluaremos posibles respuestas de un usuario

# Definimos la función con el parametro respuesta
def evaluar_respuesta(respuesta):
    # Primero usaremos == para comparar texto, en este caso si la respuesta es si
    if respuesta == "si":
        print("¡Bien hecho!")
    
    # En caso de que la respuesta no sea si, evaluamos si es no

    elif respuesta == "no":
        print("Quizás la próxima vez.")

    # Si nuevamente la respuesta no es correcta probamos con otro elif

    elif respuesta == "tal vez":
        print("¡Casi!")

    # Finalmente si ninguna de las condiciones anteriores es verdadera, se ejecuta el bloque de código dentro de else que no tiene condición

    else:
        print("No es una respuesta válida.")

# Llamada a la función
evaluar_respuesta("si")     # Salida: ¡Bien hecho!
evaluar_respuesta("no")     # Salida: Quizás la próxima vez.
evaluar_respuesta("tal vez")# Salida: ¡Casi!
evaluar_respuesta("ok")     # Salida: No es una respuesta válida.