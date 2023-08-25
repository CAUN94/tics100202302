# Ahora que ya tenemos una idea de como se usa if, elif y else, veamos como podemos usarlos en un programa de pygame.

# Ejemplo 1: Cambio de Color al Hacer Clic

import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((400, 300))

# Título e ícono de la pantalla
pygame.display.set_caption("Cambio de Color al Hacer Clic")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Rectángulo inicial
rect_color = BLUE
rect = pygame.Rect(150, 100, 100, 100)

# Si bien aun no sabemos usar while, podemos ver que dice True que es una forma de decir que siempre es verdadero, por lo que el bucle se ejecutara siempre, lo mismo que poner 1 > 0 en una condición de if.
while True:
    # Llamos a la funcion pygame.event.poll() que nos permite obtener los eventos que ocurren en la ventana
    event = pygame.event.poll()

    # Si el evento es pygame.QUIT, significa que el usuario ha presionado el botón de cerrar la ventana, por lo que llamos al comando break para salir del bucle while y cerrar el juego.
    if event.type == pygame.QUIT:
        break

    # Si el evento es pygame.MOUSEBUTTONDOWN, significa que el usuario ha presionado el botón del mouse, por lo que verificamos si el mouse se encuentra dentro del rectángulo.
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Si el mouse se encuentra dentro del rectángulo, cambiamos el color del rectángulo.Para esto usamos la funcion collidepoint() que nos permite verificar si el mouse se encuentra dentro de un rectangulo.
        if rect.collidepoint(event.pos):
            # Si el color del rectángulo es azul, lo cambiamos a rojo, de lo contrario lo cambiamos a azul.
            if rect_color == BLUE:
                rect_color = RED
            else:
                rect_color = BLUE

    # Llenamos la pantalla con el color blanco
    screen.fill(WHITE)

    # Dibujamos el rectángulo en la pantalla
    pygame.draw.rect(screen, rect_color, rect)

    # Actualizamos la pantalla
    pygame.display.flip()

# Salimos de Pygame
pygame.quit()
