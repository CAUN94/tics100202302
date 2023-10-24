# Título del Ejercicio: Generación Continua de Círculos en Pygame

# Descripción:
# En este ejercicio, crearemos un programa en Pygame que genere continuamente nuevos círculos en la ventana en lugares aleatorios. Esto ayudará a practicar la generación dinámica de figuras en Pygame.

import pygame
import sys
import random
import time

# Inicializar Pygame
pygame.init()

# Configurar ventana
ancho_ventana = 800
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Generación Continua de Círculos en Pygame")

# Colores
Negro = (0, 0, 0)

# Bucle juego
ejecutando = True

while ejecutando:
    # ventana.fill(Negro)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    x = random.randint(0,ancho_ventana)
    y = random.randint(0,alto_ventana)
    color =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    radio = random.randint(20,50)

    # Dibujar el círculo en la ventana
    pygame.draw.circle(ventana,color,[x,y], radio)
    time.sleep(0.1)
    pygame.display.update()

pygame.quiit()
sys.exit()