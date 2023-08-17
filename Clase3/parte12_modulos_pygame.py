# Haremos lo mismo que antes, pero ahora le pondremos texto

import pygame

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ventana_ancho = 400
ventana_alto = 300

# Creación de la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ventana Pygame")

# Color
color_cuadrado = (0, 255, 0)  # Verde

# Fuente, en este caso solo definimos el tamaño de la fuente
fuente = pygame.font.Font(None, 36)

# Obtener entrada de texto del usuario, esto aparecera en la consola
texto_usuario = input("Ingresa un texto: ")

# Bucle principal del juego
while True:
    # Llenar la ventana con un color de fondo, azul en este caso
    ventana.fill((0, 0, 255))

    # Dibujar un cuadrado en la ventana
    pygame.draw.rect(ventana, color_cuadrado, (150, 100, 100, 100))


    # Crear un objeto de texto, usamos la fuente y usamos la funcion render que requiere, el texto, un booleano que indica si queremos que el texto tenga bordes y el color del texto en rgb
    texto_superficie = fuente.render(texto_usuario, True, (0, 0, 0))

    # Mostrar el texto en la ventana, especificamente en el borde superios izquierdo
    ventana.blit(texto_superficie, (0, 0))
    
    # Actualizar la ventana
    pygame.display.update()
