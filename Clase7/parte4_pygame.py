# Título del Ejemplo: Creación de Figuras Aleatorias en Pygame

# Descripción:
# En este ejemplo, aprenderemos cómo utilizar Pygame para crear figuras aleatorias en una ventana y almacenar sus coordenadas en una lista. Utilizaremos círculos como ejemplo de figura. Este ejercicio te ayudará a comprender cómo generar figuras con propiedades aleatorias y cómo gestionar listas en Pygame.

# Paso a Paso:

# Paso 1: Inicializar Pygame y configurar la ventana.

#     Importa la biblioteca Pygame.
#     Inicializa Pygame.
#     Configura las dimensiones de la ventana (ancho y alto).
#     Establece un título para la ventana.

# Paso 2: Preparar la lista para las coordenadas.

#     Crea una lista llamada coordenadas_circulos para almacenar las coordenadas de los círculos.

# Paso 3: Definir colores.

#     Define los colores que utilizarás, como NEGRO, BLANCO y AZUL, utilizando tuplas de valores RGB.

# Paso 4: Crear una función para generar círculos aleatorios.

#     Define una función llamada crear_circulo que generará círculos aleatorios.
#     Dentro de la función, elige un radio aleatorio y coordenadas (x, y) aleatorias para el círculo.
#     Añade las coordenadas del círculo a la lista coordenadas_circulos.

# Paso 5: Configurar el bucle principal del juego.

#     Inicializa una variable ejecutando como True.
#     En un bucle while, verifica si se ha producido un evento de cierre de ventana (pygame.QUIT).
#     En cada iteración del bucle, llama a la función crear_circulo para generar un nuevo círculo aleatorio y agrégalo a la lista coordenadas_circulos.

# Paso 6: Dibujar los círculos en la ventana.

#     Limpia la ventana de fondo (ventana.fill(NEGRO)).
#     Itera a través de las coordenadas almacenadas en coordenadas_circulos y dibuja un círculo con las coordenadas y el radio correspondiente.

# Paso 7: Actualizar la ventana.

#     Llama a pygame.display.update() para mostrar los círculos dibujados en la ventana.

# Paso 8: Salir del juego.

#     Cuando el bucle principal finaliza (el usuario cierra la ventana), llama a pygame.quit() y sys.exit() para salir del juego de manera adecuada.

import pygame
import sys
import random
import time

# Inicializamos Pygame
pygame.init()

# Configuración de la ventana
ancho_ventana = 800
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Figuras Aleatorias")

# Lista para almacenar las coordenadas de los círculos
coordenadas_circulos = []

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Función para crear círculos aleatorios y guardar sus coordenadas
def crear_circulo():
    radio = random.randint(10, 50)
    x = random.randint(radio, ancho_ventana - radio)
    y = random.randint(radio, alto_ventana - radio)
    coordenadas_circulos.append([x, y, radio])

# Bucle principal del juego
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Crear un nuevo círculo aleatorio y guardarlo en la lista
    crear_circulo()

    # Dibujar los círculos en la ventana
    ventana.fill(NEGRO)
    for coordenada in coordenadas_circulos:
        pygame.draw.circle(ventana, AZUL, (coordenada[0], coordenada[1]), coordenada[2])

    # Delay de un segundo
    time.sleep(2)

    pygame.display.update()

# Salir del juego
pygame.quit()
sys.exit()
