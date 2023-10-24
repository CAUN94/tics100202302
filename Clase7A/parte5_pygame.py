import pygame
import random
import sys

pygame.init()

alto = 600
ancho = 600
ventana = pygame.display.set_mode([alto,ancho])
pygame.display.set_caption('Snake')

# Colores
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
verde = (20,255,200)

# Inicialización de la serpiente

velocidad = 0.5
velocidad_x = 0
velocidad_y = 0
snake_size = 30
direccion = 0

# Comida
comida_size = 30
comida_x = round(random.randint(0,alto-comida_size),1)
comida_y = round(random.randint(0,ancho-comida_size),1)

font = pygame.font.Font(None,36)

# Informacion
puntuacion = 0
eje_x = ancho/2
eje_y = alto/2
jugador = 1
lista_nombres = []
lista_puntajes = []

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ventana.fill(blanco)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:         #la direccion en su respectivo eje
        velocidad_x = -velocidad
        velocidad_y = 0
    if keys[pygame.K_RIGHT]:
        velocidad_y = 0
        velocidad_x = velocidad
    if keys[pygame.K_UP]:
        velocidad_x = 0
        velocidad_y = -velocidad
    if keys[pygame.K_DOWN]:
        velocidad_x = 0
        velocidad_y = velocidad
    eje_x = round((eje_x + velocidad_x),1)
    eje_y = round((eje_y + velocidad_y),1)
    pygame.draw.rect(ventana,negro,(eje_x,eje_y,snake_size,snake_size))
    pygame.draw.rect(ventana,rojo,(comida_x,comida_y,comida_size,comida_size))
    texto_puntuacion = font.render(f"Puntuacion: {puntuacion}", True, verde)
    ventana.blit(texto_puntuacion, (10, 10))
    nombre_jugador = font.render(f"jugador_n{jugador}", True, verde)
    ventana.blit(nombre_jugador, (10, 40))

    if (((eje_x+snake_size/2) >= comida_x and (eje_x-snake_size/2) <= comida_x) and 
    ((eje_y+snake_size/2) >= comida_y and (eje_y-snake_size/2) <= comida_y)):
        puntuacion += 1
        comida_x = round(random.randint(0,alto-comida_size),1)
        comida_y = round(random.randint(0,ancho-comida_size),1)

    if (eje_x<=0) or (eje_x>=(ancho-snake_size)) or (eje_y<=0) or (eje_y>=(alto-snake_size)) :
        lista_nombres.append(jugador)
        lista_puntajes.append(puntuacion)
        puntuacion = 0
        eje_x = ancho/2
        eje_y = alto/2
        jugador += 1

    pygame.display.update()
sys.exit()