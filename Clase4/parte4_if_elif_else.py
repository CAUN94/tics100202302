# Ejemplo 1: Verificación de Mayoría de Edad para Comprar Alcohol

# Definimos la función con el parametro edad
def verificar_edad_alcohol(edad):
    # Si la edad es mayor o igual a 18, imprime un mensaje que indica que la persona es mayor de edad.
    if edad >= 18:
        print("Eres mayor de edad para comprar alcohol.")
    
    # En caso de que la edad sea menor a 18, se imprime un mensaje que indica que la persona es menor de edad.
    elif edad >= 0:
        print("Eres menor de edad. No puedes comprar alcohol.")

    # Si la no cumple ninguna de las condiciones anteriores, se imprime un mensaje que indica que la edad es inválida.
    else:
        print("Edad inválida. Ingresa una edad positiva.")

# Llamada a la función
verificar_edad_alcohol(22)   # Salida: Eres mayor de edad para comprar alcohol.
verificar_edad_alcohol(16)   # Salida: Eres menor de edad. No puedes comprar alcohol.
verificar_edad_alcohol(-5)   # Salida: Edad inválida. Ingresa una edad positiva.

# Ejemplo 2: Verificación de Contraseña

# Definimos la función
def verificar_contrasena():
    # Definimos la contraseña real
    contrasena_real = "secreto123"

    # Solicitamos al usuario que ingrese la contraseña
    contrasena_ingresada = input("Ingresa tu contraseña: ")

    # Si la contraseña ingresada es igual a la contraseña real, se imprime un mensaje que indica que la contraseña es correcta.
    if contrasena_ingresada == contrasena_real:
        print("Contraseña correcta. Bienvenido.")
    else:
        print("Contraseña incorrecta. Acceso denegado.")

# Llamada a la función
verificar_contrasena()

# Ejemplo 3: Verificar divisibilidad y comparación de numeros

# Esta función solicitaremos dos números al usuario, verificamos si el primero es divisible por el segundo y luego compara los números para determinar cuál es mayor, cuál es menor o si son iguales. En caso de que el segundo número sea cero, se imprime un mensaje indicando que la división no es posible.

# Definimos la función
def verificar_divisibilidad_y_comparar():
    # Solicitamos al usuario que ingrese dos números
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    
    # Verificamos si el segundo número es cero
    if numero2 == 0:
        print("El segundo número no puede ser cero. No se puede realizar la división.")
    
    # Si el segundo número no es cero, verificamos si el primer número es divisible por el segundo
    # El comando % nos permite obtener el residuo de una división, si el residuo es cero, el primer número es divisible por el segundo, de lo contrario no es divisible.
    # 4%2 = 0, 4 es divisible por 2
    # 3%2 = 1, 3 no es divisible por 2
    # 7%2 = 1, 7 no es divisible por 2
    # 6%2 = 0, 6 es divisible por 2
    elif numero1 % numero2 == 0:
        print(f"{numero1} es divisible por {numero2}.")
        
        # Si el primer número es divisible por el segundo, comparamos los números para determinar cuál es mayor, cuál es menor o si son iguales.
        if numero1 > numero2:
            print(f"{numero1} es mayor que {numero2}.")
        elif numero1 < numero2:
            print(f"{numero1} es menor que {numero2}.")
        else:
            print("Los números son iguales.")
    else:
        print(f"{numero1} no es divisible por {numero2}.")

# Llamada a la función
verificar_divisibilidad_y_comparar()

