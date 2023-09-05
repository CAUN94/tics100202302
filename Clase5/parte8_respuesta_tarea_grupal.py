import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Juego de Cuadrado Rebote")

# Colores
azul = (0, 0, 255)

# Tamaño y posición inicial del cuadrado
cuadrado_lado = 50
cuadrado_x = (ventana_ancho - cuadrado_lado) // 2
cuadrado_y = (ventana_alto - cuadrado_lado) // 2

# Velocidad inicial del cuadrado en píxeles por fotograma
velocidad_x = random.choice([-3, 3])  # Dirección aleatoria en el eje X
velocidad_y = random.choice([-3, 3])  # Dirección aleatoria en el eje Y

# Contador de rebotes
rebotes = 0

# Fuente para el contador de rebotes
fuente = pygame.font.Font(None, 36)

# Bucle principal del juego
while True:
    if pygame.event.get(pygame.QUIT):
        pygame.quit()

    # Mover el cuadrado
    cuadrado_x += velocidad_x
    cuadrado_y += velocidad_y

    # Rebote en los bordes
    if cuadrado_x <= 0 or cuadrado_x + cuadrado_lado >= ventana_ancho:
        velocidad_x = -velocidad_x
        rebotes += 1

    if cuadrado_y <= 0 or cuadrado_y + cuadrado_lado >= ventana_alto:
        velocidad_y = -velocidad_y
        rebotes += 1

    # Limpiar la pantalla
    ventana.fill((255, 255, 255))

    # Dibujar el cuadrado
    pygame.draw.rect(ventana, azul, (cuadrado_x, cuadrado_y, cuadrado_lado, cuadrado_lado))

    # Mostrar el contador de rebotes
    contador_texto = fuente.render(f"Rebotes: {rebotes}", True, (0, 0, 0))
    ventana.blit(contador_texto, (ventana_ancho - 200, 20))

    # Actualizar la pantalla
    pygame.display.update()