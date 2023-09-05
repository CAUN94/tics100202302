import pygame
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 200
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Fila de Cuadrados en Movimiento")

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)

# Tamaño y cantidad de cuadrados
cuadrado_lado = 30
cantidad_cuadrados = 3

# Posición inicial de la fila de cuadrados
x = 0
y = 100

# Velocidad de movimiento
velocidad = 1

# Bucle principal del juego
while True:
    # Quit if
    if pygame.event.get(pygame.QUIT):
        pygame.quit()

    # Limpiar la pantalla
    ventana.fill(blanco)
    # Dibujar y mover la fila de cuadrados utilizando un ciclo for
    for i in range(cantidad_cuadrados):
        x = x + i * (cuadrado_lado + 10)  # Espaciado entre cuadrados
        pygame.draw.rect(ventana, azul, (x, y, cuadrado_lado, cuadrado_lado))

        # Mover los cuadrados hacia la derecha y verificar si han llegado al final
        x += velocidad
        if x > ventana_ancho:
            x = -cuadrado_lado  # Volver al inicio
    time.sleep(1)
    # Actualizar la pantalla
    pygame.display.update()
