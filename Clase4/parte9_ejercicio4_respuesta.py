import math

def verificar_raiz_cuadrada_entera():
    numero = float(input("Ingresa un número: "))
    raiz_cuadrada = math.sqrt(numero)
    
    if raiz_cuadrada == int(raiz_cuadrada):
        print("La raíz cuadrada es un número entero.")
    else:
        print("La raíz cuadrada no es un número entero.")

# Llamada a la función
verificar_raiz_cuadrada_entera()
