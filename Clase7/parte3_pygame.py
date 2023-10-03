# Título del Ejercicio: Generación Continua de Círculos en Pygame

# Descripción:
# En este ejercicio, crearemos un programa en Pygame que genere continuamente nuevos círculos en la ventana en lugares aleatorios. Esto ayudará a practicar la generación dinámica de figuras en Pygame.


import pygame
import sys
import random
import time

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ancho_ventana = 800
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Generación Continua de Círculos")

# Colores
NEGRO = (0, 0, 0)

# Bucle principal del juego
ejecutando = True

while ejecutando:
    ventana.fill(NEGRO)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Crear coordenadas aleatorias para el círculo
    x = random.randint(0, ancho_ventana)
    y = random.randint(0, alto_ventana)
    radio = random.randint(20, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Dibujar el círculo en la ventana
    pygame.draw.circle(ventana, color, (x, y), radio)

    time.sleep(1)

    # Actualizar la ventana
    pygame.display.update()

# Salir del juego
pygame.quit()
sys.exit()
