import sys
import pygame
from pygame.locals import *
import random

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO = 800
ALTO = 600
MARIO_SIZE = 50
TORTUGA_SIZE = 30
TORTUGA_CANTIDAD = 5
COLOR_FONDO = (255, 255, 255)
COLOR_MARIO = (255, 0, 0)
COLOR_TORTUGA = (0, 255, 0)
VELOCIDAD = 5

# Configuración de pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mario y las tortugas")

# Posición de Mario
mario_pos = [ANCHO // 2, ALTO // 2]

# Lista de tortugas
tortugas = []
for _ in range(TORTUGA_CANTIDAD):
    x = random.randint(0, ANCHO - TORTUGA_SIZE)
    y = random.randint(0, ALTO - TORTUGA_SIZE)
    tortugas.append([x, y])

# Función para dibujar a Mario y las tortugas
def dibujar():
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_MARIO, (mario_pos[0], mario_pos[1], MARIO_SIZE, MARIO_SIZE))
    for tortuga in tortugas:
        pygame.draw.rect(pantalla, COLOR_TORTUGA, (tortuga[0], tortuga[1], TORTUGA_SIZE, TORTUGA_SIZE))
    pygame.display.flip()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Mover a Mario con las teclas
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] or keys[K_a]:
        mario_pos[0] -= VELOCIDAD
    if keys[K_RIGHT] or keys[K_d]:
        mario_pos[0] += VELOCIDAD
    if keys[K_UP] or keys[K_w]:
        mario_pos[1] -= VELOCIDAD
    if keys[K_DOWN] or keys[K_s]:
        mario_pos[1] += VELOCIDAD

    # Mover las tortugas hacia Mario
    for tortuga in tortugas:
        if tortuga[0] < mario_pos[0]:
            tortuga[0] += VELOCIDAD
        elif tortuga[0] > mario_pos[0]:
            tortuga[0] -= VELOCIDAD
        if tortuga[1] < mario_pos[1]:
            tortuga[1] += VELOCIDAD
        elif tortuga[1] > mario_pos[1]:
            tortuga[1] -= VELOCIDAD

    # Comprobar colisiones y remover tortugas si es necesario
    tortugas = [t for t in tortugas if not (
        mario_pos[0] < t[0] < mario_pos[0] + MARIO_SIZE and
        mario_pos[1] < t[1] < mario_pos[1] + MARIO_SIZE
    )]

    # Dibujar todo
    dibujar()

    # Finalizar el juego si no hay más tortugas
    if not tortugas:
        print("¡Has ganado!")
        pygame.quit()
        sys.exit()

    # Controlar velocidad del juego
    pygame.time.delay(30)
