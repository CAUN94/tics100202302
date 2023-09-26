# Importar librerías
import pygame
import time
import random

# Inicializar pygame
pygame.init()
# Pantalla de 400 x 300
screen = pygame.display.set_mode((400, 300))

# Imágenes de mario y de la tortuga
mario = pygame.image.load('Clase6/mario.png')
tortuga = pygame.image.load('Clase6/tortuga.png')

# Redimensionamos las imágenes
mario = pygame.transform.scale(mario, (50, 50))
tortuga = pygame.transform.scale(tortuga, (50, 50))


#Posición inicial de MArio
x = screen.get_width()//2
y = screen.get_height()//2

#velocidad de Mario
velocity_x = 20
velocity_y = 20

#velocidad de la tortuga
vel_tor = 3 

#Posición inicial de las tortugas
pos_tor_x = []
pos_tor_y = []

for i in range(5):
    pos_tor_x.append(random.randint(0, 400))
    pos_tor_y.append(random.randint(0, 300))

#Impedimos con un False que se muestre la tortuga
muestra_tortuga = False

# Que no se termine
running = True
while running:
    #escuchamos los eventos del programa
    for event in pygame.event.get():
        #hacemos que se detecte si apretamos la cruz que cierra la ventana
        if event.type == pygame.QUIT:
            running = False
        
        #activamos la escucha de los eventos del teclado
        elif event.type == pygame.KEYDOWN:
            #hacemos que el evento del teclado nos permita over a Mario
            if event.key == pygame.K_LEFT:
                x -= velocity_x
            elif event.key == pygame.K_RIGHT:
                x += velocity_x
            elif event.key == pygame.K_UP:
                y -= velocity_y
            elif event.key == pygame.K_DOWN:
                y += velocity_y
            #hacemos que el evento del teclado nos permita mostrar a la tortuga
            elif event.key == pygame.K_SPACE:
                muestra_tortuga = True 
    
    #Pintamos un fondo negro y dibujamos a Mario en la posición (x,y)
    screen.fill((0, 0, 0))
    screen.blit(mario, (x, y))
    
    #La imagen se muestra sólo si muestra_imagen es True.
    j=0
    while (j <5):    
        if muestra_tortuga:
            screen.blit(tortuga,(pos_tor_x[j],pos_tor_y[j])) 
            # Comparamos las posiciones de mario y de la tortuga. 
            # Si la tortuga está a la izquierda de mario, hacemos que se mueva a la derecha.
            if pos_tor_x[j] < x:
                pos_tor_x[j] += vel_tor
            # Si la tortuga está a la arriba de mario, hacemos que se mueva hacia abajo.
            if pos_tor_y[j] < y:
                pos_tor_y[j] += vel_tor
            # Si la tortuga está a la derecha de mario, hacemos que se mueva a la izquierda.
            if pos_tor_x[j] > x:
                pos_tor_x[j] -= vel_tor
            # Si la tortuga está abajo de mario, hacemos que se mueva hacia arriba.
            if pos_tor_y[j] > y:
                pos_tor_y[j] -= vel_tor
        j+=1

    pygame.display.flip()
    pygame.time.delay(200)
    #time.sleep(1)

pygame.quit()

#Sugerencias para complegizar el programa:
#1. Que otro jugador pueda mover la tortuga
#2. Que se cuente un puntaje cada vez que la tortuga toca a mario
#3. Mostrar un fondo que parezca un tablero de un juego y que tanto mario como la tortuga puedan navegar sólo por los espacios habilitados.