import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ventana_ancho = 800
ventana_alto = 600

# Creación de la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Figuras Aleatorias")

# Colores
color_1 = (255, 0, 0)   # Rojo
color_2 = (0, 255, 0)   # Verde
color_3 = (0, 0, 255)   # Azul

# Bucle principal del juego
while True:
    ventana.fill((255, 255, 255))  # Fondo blanco

    # Generar tamaños aleatorios para los cuadrados
    tamano_1 = random.randint(10, 150)
    tamano_2 = random.randint(10, 150)
    tamano_3 = random.randint(10, 150)

    # Generar posiciones aleatorias para los cuadrados
    pos_x_1 = random.randint(0, ventana_ancho - tamano_1)
    pos_y_1 = random.randint(0, ventana_alto - tamano_1)

    pos_x_2 = random.randint(0, ventana_ancho - tamano_2)
    pos_y_2 = random.randint(0, ventana_alto - tamano_2)

    pos_x_3 = random.randint(0, ventana_ancho - tamano_3)
    pos_y_3 = random.randint(0, ventana_alto - tamano_3)

    # Dibujar los cuadrados en la ventana
    pygame.draw.rect(ventana, color_1, (pos_x_1, pos_y_1, tamano_1, tamano_1))
    pygame.draw.rect(ventana, color_2, (pos_x_2, pos_y_2, tamano_2, tamano_2))
    pygame.draw.rect(ventana, color_3, (pos_x_3, pos_y_3, tamano_3, tamano_3))

    # Actualizar la ventana
    pygame.display.update()

    # Pausa de 3 segundos
    time.sleep(3)
