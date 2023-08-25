def clasificar_triangulo():
    lado1 = float(input("Ingresa la longitud del primer lado: "))
    lado2 = float(input("Ingresa la longitud del segundo lado: "))
    lado3 = float(input("Ingresa la longitud del tercer lado: "))
    
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

# Llamada a la función
clasificar_triangulo()
