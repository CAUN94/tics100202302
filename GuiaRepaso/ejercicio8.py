# Cifrado Cesar: El cifrado cesar en una tecnica de criptofria que consiste en reemplazar cada letra de un texto por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto. Por ejemplo, si el número de posiciones es 3, la letra A se reemplaza por la D, la B por la E, la C por la F, etc. La letra Z se reemplaza por la C. Crear un programa en Python que reciba un texto y un número de posiciones y muestre el texto cifrado.

# Solo ingresan letras mayúsculas y minúsculas
# En caso de que ingrese un número, mostrar un mensaje de error
# En caso de pillar un espacio, dejarlo igual
# Se le pide al usuario que ingrese una cadena
# Se le pide al usuario que ingrese un número de posiciones a moverse
# Hint: Usar la función lower() para convertir una letra a minúscula
# Ejemplo: Si damos la palabra "Python" y el número 3, el programa debe retornar "sbwkrq"
# Hint: Dejamos un variable abc con todas las letras del alfabeto en orden

# Función que recibe una cadena y un número de posiciones y retorna la cadena cifrada
def cifradoCesar(palabra,posiciones):
    pass
    # Creamos una variable que almacenará la cadena cifrada 
    

    # Recorremos la palabra
    
        # Si la letra es un espacio, lo agregamos a la cadena cifrada
        
            
        # En caso contrario, llamamos a la función nuevaLetra
        
            # Agregamos la nueva letra a la cadena cifrada
            

    # Retornamos la cadena cifrada
    


    # Variable que almacenará el alfabeto
    

    # Variable que almacenará la nueva letra en minúscula
    

    # Recorremos el alfabeto
    
        # Si la letra es igual a la letra del alfabeto en la posición i
        
            # Si la posición de la letra + las posiciones a moverse es mayor o igual al largo del alfabeto (26) le restamos 26 para que vuelva a empezar
            
                
            # En caso contrario, retornamos la letra del alfabeto en la posición i + posiciones
            
                

# Solicitamos al usuario que ingrese una palabra y un número de posiciones

# Solicitamos al usuario que ingrese un número de posiciones



# Mostramos la cadena cifrada usando la función cifradoCesar



