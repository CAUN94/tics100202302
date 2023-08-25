# Ejemplo 2: Movimiento de un Personaje con Flechas

import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Movimiento de Personaje con Flechas")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Nuestro personaje va a ser un rectángulo
player = pygame.Rect(150, 100, 50, 50)

# Velocidad del personaje, en este caso cuando presionemos una flecha, el personaje se moverá 5 pixeles en esa dirección.
player_speed = 5

while True:
    # Llamos a la funcion pygame.event.poll() que nos permite obtener los eventos que ocurren en la ventana
    event = pygame.event.poll()

    # Si el evento es pygame.QUIT, significa que el usuario ha presionado el botón de cerrar la ventana, por lo que llamos al comando break para salir del bucle while y cerrar el juego.
    if event.type == pygame.QUIT:
        break

    # Verificamos si el usuario ha presionado alguna flecha usando la funcion pygame.key.get_pressed() que nos permite obtener una lista con las teclas que se han presionado.
    keys = pygame.key.get_pressed()

    # Si el usuario ha presionado la flecha izquierda, restamos la velocidad del personaje a la posición en x del personaje, este valor esta almacenado en la variable player.x., usamos -= que es el equivalente a player.x = player.x - player_speed
    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    # Si el usuario ha presionado la flecha derecha, sumamos la velocidad del personaje a la posición en x del personaje, este valor esta almacenado en la variable player.x., usamos += que es el equivalente a player.x = player.x + player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Si el usuario ha presionado la flecha arriba, restamos la velocidad del personaje a la posición en y del personaje, este valor esta almacenado en la variable player.y., usamos -= que es el equivalente a player.y = player.y - player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed

    # Si el usuario ha presionado la flecha abajo, sumamos la velocidad del personaje a la posición en y del personaje, este valor esta almacenado en la variable player.y., usamos += que es el equivalente a player.y = player.y + player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Llenamos la pantalla con el color blanco
    screen.fill(WHITE)

    # Dibujamos el personaje en la pantalla
    pygame.draw.rect(screen, GREEN, player)
    pygame.display.flip()

# Salimos de Pygame
pygame.quit()

