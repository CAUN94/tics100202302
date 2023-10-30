import pygame
import csv
import time
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Juego de Hacer Clic")

# Lista para almacenar las coordenadas de los 3 puntos
puntos = []

# Generar 3 puntos aleatorios
for _ in range(3):
    x = random.randint(20, 380)
    y = random.randint(20, 380)
    puntos.append((x, y))

# Variables para el tiempo y el clic
clics = 0

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            for punto in puntos:
                distancia = ((x - punto[0]) ** 2 + (y - punto[1]) ** 2) ** 0.5
                if distancia < 15:
                    clics += 1
                    if clics == 1:
                        inicio = time.time()
                    if clics == 3:
                        fin = time.time()
                        ejecutando = False

    ventana.fill((0, 0, 0))
    for punto in puntos:
        pygame.draw.circle(ventana, (255, 0, 0), punto, 15)

    pygame.display.update()

# Calcular el tiempo transcurrido en segundos

# Cerrar Pygame
pygame.quit()
