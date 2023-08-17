# En esta segunda parte de la clase, exploraremos el módulo Pygame, que nos permitirá crear una interfaz gráfica y realizar acciones visuales en una ventana separada. A lo largo de esta hora, aprenderemos a:

# Importar el módulo Pygame y configurar el entorno.
# Crear una ventana gráfica utilizando Pygame.
# Dibujar formas geométricas básicas en la ventana.
# Controlar el cierre de la ventana y la finalización del programa.
# Mostrar texto en la ventana.

# Importar el módulo Pygame y configurar el entorno.
import pygame

# Inicialización de Pygame, este comando debe ejecutarse antes de cualquier otro comando de Pygame, ya que es el que inicializa el entorno de Pygame.
pygame.init()

# Dimensiones de la ventana
ventana_ancho = 400
ventana_alto = 300

# Creación de la ventana usando la funcion display y dentro de esta la funcion set_mode que recibe como parametro una parentesis con las dimensiones de la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))

# Pongamos un título a la ventana
pygame.display.set_caption("Ventana Pygame")

# Definamos un color para el cuadrado usanfo rgb, en este caso rojo
color_cuadrado = (255, 0, 0)  # Rojo

# Aun no aprendemos a usar el bucle while, pero lo usaremos para que la ventana se mantenga abierta por un tiempo indefinido (por eso usamos True), lo unico que importa es saber que todo lo que este dentro del while se ejecutara una y otra vez hasta que se cierre la ventana, actualmente no sabemos como cerrar la ventana, pero lo veremos mas adelante, por ahora si quiere cerrar entre a la consola y presione Ctrl + C.

# Bucle principal del juego
while True:
    # Llenar la ventana con un color de fondo, en este caso el rgb de blanco
    ventana.fill((255, 255, 255))  

    # Dibujar un cuadrado en la ventana
    # Debemos definir la ventana, el color y un parentesis con la posicion x, y y el ancho y alto del cuadrado
    pygame.draw.rect(ventana, color_cuadrado, (150, 100, 100, 100))

    # Actualizar la ventana, es decir, mostrarla en pantalla, algun día haremos que esto se mueva.
    pygame.display.update()
