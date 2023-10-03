import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 500
ventana_alto = 500
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Desplaza el Cuadro")

# Colores
blanco = (255, 255, 255)

# Tamaño y posición inicial del cuadro
cuadro_lado = 50
cuadro_x = (ventana_ancho - cuadro_lado) // 2
cuadro_y = (ventana_alto - cuadro_lado) // 2

# Velocidad de desplazamiento
velocidad = 0.1

# Contador
contador = 10
fondo_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# Fuente para el contador
fuente = pygame.font.Font(None, 36)

# Bucle principal del juego
while contador > 0:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    # Obtener el estado de las teclas
    teclas = pygame.key.get_pressed()

    # Actualizar la posición del cuadro según las teclas presionadas
    if teclas[pygame.K_LEFT]:
        cuadro_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        cuadro_x += velocidad
    if teclas[pygame.K_UP]:
        cuadro_y -= velocidad
    if teclas[pygame.K_DOWN]:
        cuadro_y += velocidad

    # Lógica de colisión con las paredes
    if cuadro_x < 0 or cuadro_x + cuadro_lado > ventana_ancho or cuadro_y < 0 or cuadro_y + cuadro_lado > ventana_alto:
        # Devolver el cuadro al centro de la ventana
        cuadro_x = (ventana_ancho - cuadro_lado) // 2
        cuadro_y = (ventana_alto - cuadro_lado) // 2

        # Cambiar el fondo a un color RGB aleatorio
        fondo_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ventana.fill(fondo_color)

        # Disminuir el contador en 1
        contador -= 1

    # Limpiar la pantalla con el color de fondo actual
    ventana.fill(fondo_color)

    # Dibujar el cuadro
    pygame.draw.rect(ventana, (0, 0, 0), (cuadro_x, cuadro_y, cuadro_lado, cuadro_lado))

    # Mostrar el contador en la parte superior
    contador_texto = fuente.render(f"Contador: {contador}", True, blanco)
    ventana.blit(contador_texto, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Cuando el contador llega a 0, finaliza el juego
pygame.quit()
