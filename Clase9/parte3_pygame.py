import pygame
import csv
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Juego de Hacer Clic")

# Coordenadas de los 3 puntos
puntos = [(100, 100), (200, 200), (300, 300)]

# Variables para el tiempo y el clic
inicio = 0
fin = 0
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
tiempo = round(fin - inicio, 2)

# Guardar el tiempo en un archivo CSV
with open('tiempos.csv', 'a', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([tiempo])

# Cerrar Pygame
pygame.quit()
