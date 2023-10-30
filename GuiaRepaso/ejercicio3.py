# Verificador de parentesis: Haz una funcion a la que se le entregue una ecuacion y verifique si los parentesis estan bien cerrados, por ejempo (2+3)*5 esta bien, pero (2+3)*5) esta mal.

# Función que recibe una cadena y retorna True si los paréntesis están bien cerrados, False en caso contrario

def verificarParentesis(cadena):
    # Variable que almacenará la cantidad de paréntesis abiertos
    abiertos = 0
    # Recorremos la cadena
    for i in cadena:
        # Si encontramos un paréntesis abierto, aumentamos la variable abiertos en 1
        if i == "(":
            abiertos += 1
        # Si encontramos un paréntesis cerrado, disminuimos la variable abiertos en 1
        elif i == ")":
            abiertos -= 1
        # Si la variable abiertos es negativa, significa que hay más paréntesis cerrados que abiertos, por lo tanto, retornamos False
        if abiertos < 0:
            return False
    # Si la variable abiertos es distinta de 0, significa que hay más paréntesis abiertos que cerrados, por lo tanto, retornamos False
    if abiertos != 0:
        return False
    # Si no se cumple ninguna de las condiciones anteriores, significa que los paréntesis están bien cerrados, por lo tanto, retornamos True
    return True

# Pedimos al usuario la cadena
cadena = input("Ingrese una cadena: ")

# Mostramos el resultado de la función verificarParentesis
print("Los paréntesis están bien cerrados: ", verificarParentesis(cadena))
