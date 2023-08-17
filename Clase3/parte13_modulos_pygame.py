# Agrueguemos un texto que muestre el tiempo transcurrido desde que se inició el programa. Para ello, utilizaremos el módulo time.

import pygame
import time

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ventana_ancho = 400
ventana_alto = 300

# Creación de la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ventana Pygame")

# Color
color_cuadrado = (255, 0, 0)  # Rojo

# Fuente
fuente = pygame.font.Font(None, 36)

# Tiempo de inicio
tiempo_inicio = time.time()

# Obtener entrada de texto del usuario
texto_usuario = input("Ingresa un texto: ")

# Bucle principal del juego
while True:
    # Llenar la ventana con un color de fondo
    ventana.fill((255, 255, 255))  # Blanco

    # Dibujar un cuadrado en la ventana
    pygame.draw.rect(ventana, color_cuadrado, (150, 100, 100, 100))

    # Crear un objeto de texto para el texto ingresado por el usuario
    texto_superficie = fuente.render(texto_usuario, True, (255, 0, 0))

    # Mostrar el texto en la ventana, especificamente en el borde superios izquierdo
    ventana.blit(texto_superficie, (0, 0))

    # Calcular segundos transcurridos
    segundos_transcurridos = int(time.time() - tiempo_inicio)

    # Crear un objeto de texto para los segundos
    segundos_superficie = fuente.render(f"Segundos: {segundos_transcurridos}", True, (255, 0, 0))

    # Mostrar el texto en la ventana dando la posición del borde superior izquierdo, en este caso, el texto del usuario se mostrará en la esquina superior izquierda
    ventana.blit(segundos_superficie, (150, 250))

    # Actualizar la ventana
    pygame.display.update()
