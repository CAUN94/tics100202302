import math

# Ejemplo 1: Cálculo del área de un círculo:

# Definimos la funcion calcular_area_circulo()
def calcular_area_circulo():
    # Pedimos el radio del círculo
    radio = float(input("Ingresa el radio del círculo: "))
    # Usamos la funcion pi del modulo math para obtener el valor de pi y lo elevamos al cuadrado
    area = math.pi * radio**2

    # Retornamos el valor del area
    return area

# Llamamos a la funcion y guardamos el resultado en la variable resultado
resultado = calcular_area_circulo()

# Imprimimos el resultado
print(f"El área del círculo es: {resultado}")

# Ejemplo 2: Cálculo de la hipotenusa de un triángulo:

# Definimos la funcion calcular_hipotenusa()
def calcular_hipotenusa():
    # Pedimos los catetos del triangulo
    cateto1 = float(input("Ingresa la longitud del primer cateto: "))
    cateto2 = float(input("Ingresa la longitud del segundo cateto: "))

    # Usamos la funcion sqrt() del modulo math para calcular la raiz cuadrada de la suma de los catetos elevados al cuadrado
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

    # Retornamos el valor de la hipotenusa
    return hipotenusa

# Llamamos a la funcion y guardamos el resultado en la variable resultado   
resultado = calcular_hipotenusa()

# Imprimimos el resultado
print(f"La longitud de la hipotenusa es: {resultado}")

# Ejemplo 3: Conversión de grados a radianes:

# Definimos la funcion grados_a_radianes()
def grados_a_radianes():
    # Pedimos la medida en grados
    grados = float(input("Ingresa la medida en grados: "))
    # Usamos la funcion radians() del modulo math para convertir los grados a radianes
    radianes = math.radians(grados)
    # Retornamos el valor en radianes
    return radianes

# Llamamos a la funcion y guardamos el resultado en la variable resultado
resultado = grados_a_radianes()
# Imprimimos el resultado
print(f"La medida en radianes es: {resultado}")