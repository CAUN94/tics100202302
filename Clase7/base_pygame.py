# Importamos la libreria pygame y sys
import pygame
import sys

# Inicializamos pygame
pygame.init()

# Configuramos la ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mi primer juego")

# Colores
negro = (0,0,0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Figuras
# Creamos un cuadrado con las variables (posición x, posición y, largo y ancho)
cuadrado = pygame.Rect(100,100,50,50)

# Creamos un circulo con las variables, lugar donde aparecera, color, coordenadas, radio
circulo = pygame.draw.circle(ventana,rojo,[300,300],20)

# Creamos un triangulo (poligono) con las variables lugar donde aparecera, color coordenadas de todos sus puntos
triangulo = pygame.draw.polygon(ventana,azul,[(500,500),(550,500),(525,450)])

# Texto
fuente = pygame.font.Font(None, 36)
texto = fuente.render("Hola, Pygame", True, blanco)
ventana.blit(texto, (350, 10))

# Bucle principal del juego
ejecutando = True

while ejecutando:
    # Función para cerrar juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Dibuja las figuras
    pygame.draw.rect(ventana, verde, cuadrado)
    pygame.draw.circle(ventana, azul, (300, 300), 30)
    pygame.draw.polygon(ventana, rojo, [(500, 500), (550, 500), (525, 450)])  

    # Actualiza la ventana
    pygame.display.update()    

# Cerramos el juego
pygame.quit()
sys.exit()