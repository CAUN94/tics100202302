# Reverso de una Cadena: Implementa una función que invierta una palabra dada. Por ejemplo, si la palabra es "Python", la función debe retornar "nohtyP".

# Función que recibe una cadena y retorna la cadena invertida
def invertirCadena(cadena):
    # Variable que almacenará la cadena invertida
    invertida = ""
    # Recorremos la cadena de atrás hacia adelante
    for i in range(len(cadena) - 1, -1, -1):
        # Agregamos el caracter a la cadena invertida
        invertida += cadena[i]
    # Retornamos la cadena invertida
    return invertida

# Pedimos al usuario la cadena
cadena = input("Ingrese una cadena: ")
# Mostramos la cadena invertida usando la función invertirCadena
print("Cadena invertida: ", invertirCadena(cadena))