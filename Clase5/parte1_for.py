# Ciclo For

# Un ciclo for es un ciclo que se repite un número determinado de veces, los conceptos principales de este son:
# 1. La variable que va a ir cambiando en cada iteración
# 2. El rango de valores que va a tomar la variable
# 3. El cuerpo del ciclo

# Explicación paso a paso del ciclo for

# Para crear un ciclo for llamamos a la palabra reservada for

# for 

# Despues definimos una variable que va a ir cambiando en cada iteración, por convención se llama i, pero puede tener cualquier nombre

# for i
# for iteration
# for x
# for number
# Todas son validas

# Despues definimos el rango de valores que va a tomar la variable, para esto usamos la palabra reservada in

# for i in 

# Siguiente a esto definimos el rango de valores que usaremos, para esto usamos la función range(), la cual recibe 3 valores, el primero es el valor inicial, el segundo es el valor final y el tercero es el valor de incremento, si no se especifica el valor de incremento, por defecto es 1.

#  Veamos ejemplos de range()

# Si solo damos un valor, me genera este conjunto de numeros
# range(5) -> [0, 1, 2, 3, 4]

# Si entregamos principio y final, me genera este conjunto de numeros
# range(5,12) -> [5, 6, 7, 8, 9, 10, 11]

# Si entregamos principio, final e incremento, me genera este conjunto de numeros
# range(6,41,7) -> [6, 13, 20, 27, 34]

# Mucho ojo, ya que nunca se incluye el valor final, es decir, si le pongo range(5), el valor final es 4, si le pongo range(5,12), el valor final es 11, y si le pongo range(6,41,7), el valor final es 34 (si sumo 7 a 34 llego a 41, y 41 no está incluido)

# Tambien puede ser en reversa
# range(5,0,-1) -> [5, 4, 3, 2, 1]
# range(21,-10,-4) -> [21, 17, 13, 9, 5, 1, -3, -7]

# Ahora que ya tengo el rangon podemos hacer nuestro primero for

# for i in range(5):
#     el codigo que quiero que se repita

# Vamos creando ejemplos de for

# Ejemplo 1: Imprimir hola 5 veces



# Ejemplo 2: Imprimir los numeros del 1 al 10



# Ejemplo 3: Imprimir los numeros del 1 al 10 en reversa


