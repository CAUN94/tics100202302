# Módulo math:
# El módulo math proporciona funciones matemáticas. Vamos a explorar cómo calcular la raíz cuadrada y el seno de un número.

# Importamos el modulo math
import math

# Definimos la funcion calcular_raiz_cuadrada() que recibe un numero como parametro
def calcular_raiz_cuadrada(numero):
    # Usamos la funcion sqrt() del modulo math para calcular la raiz cuadrada del numero
    return math.sqrt(numero)

# Definimos la funcion calcular_seno() que recibe un angulo como parametro
def calcular_seno(angulo):
    # Usamos la funcion sin() del modulo math para calcular el seno del angulo
    return math.sin(angulo)

# Imprimimos los resultados
print("La raíz cuadrada de 16 es:", calcular_raiz_cuadrada(16))
print("El seno de 30 grados es:", calcular_seno(math.radians(30)))
print("La raíz cuadrada de 36 es:", calcular_raiz_cuadrada(36))
print("El seno de 45 grados es:", calcular_seno(math.radians(45)))
print("La raíz cuadrada de 49 es:", calcular_raiz_cuadrada(49))
print("El seno de 15 grados es:", calcular_seno(math.radians(15)))