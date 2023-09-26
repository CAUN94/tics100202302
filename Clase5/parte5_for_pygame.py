# Ejercicio de Pygame con Ciclo For y Temporizador

# En este ejercicio, crearás un programa utilizando Pygame que generará una fila de cuadrados azules en una ventana. Los cuadrados se dibujaran hacia la derecha usando el ciclo for, además, se mostrará un temporizador que indicará cuánto tiempo ha pasado desde que se inició el programa.


import pygame
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ejemplo de Pygame con Ciclo For y Temporizador")

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)

# Variables para los cuadrados
cuadrado_ancho = 50
cuadrado_alto = 50
cantidad_cuadrados = 10  # Número de cuadrados en la fila
velocidad = 5  # Velocidad de movimiento hacia la derecha

# Contador de tiempo
tiempo_inicial = time.time()

# Bucle principal del juego
while True:
    if pygame.event.get().type == pygame.QUIT:
        pygame.quit()


    # Calcular el tiempo transcurrido
    tiempo_actual = time.time()
    segundos_transcurridos = int(tiempo_actual - tiempo_inicial)

    # Rellenar la ventana de color blanco
    ventana.fill(blanco)

    # Dibujar y mover cuadrados utilizando un ciclo for
    for i in range(cantidad_cuadrados):
        x = i * (cuadrado_ancho + 10)  # Espaciado entre cuadrados
        y = 250  # Altura fija para la fila
        pygame.draw.rect(ventana, azul, (x, y, cuadrado_ancho, cuadrado_alto))
        

    # Dibujar el tiempo transcurrido
    fuente = pygame.font.SysFont("Arial", 30)
    texto = fuente.render(str(segundos_transcurridos), True, (0, 0, 0))
    ventana.blit(texto, (10, 10))


    # Actualizar la pantalla
    pygame.display.update()
