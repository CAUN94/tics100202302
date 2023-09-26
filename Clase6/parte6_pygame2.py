# Ahora crearemos un juego de "tiro al blanco" 
# Crearemos círculos que aparecerán en posiciones random de la pantalla con tamaños variables
# Cada vez que le hagamos click a uno de los círculos antes de que desaparezcan agregaremos un punto a nuestra
# racha ganadora. Cuando lleguemos a 10, seremos unos crack y se cerrara el programa.

import pygame
import random
import time
# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 500
ventana_alto = 500
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Tiro al blanco")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
otro = (255, 20, 100)

# Fuente para mostrar el contador y
fuente = pygame.font.Font(None, 36)

# Inicialización del contador
multiplicador = 1 #este parametro nos ayudara a mantener el juego funcionando sin que sleep o delay afecten el funcionamiento
tiempo = 30 #es el tiempo que espera el juego entre cada ciclo while, mientras mas pequeño este numero es mas fluida 
            #la jugabilidad pero mas complejo el control de la deteccion de clicks y el tiempo en que aparecen y desaparecen
            #los circulos
ganadas = 0 #contador de partidas ganadas
fin_juego = 3    #contador que indica con cuantas partidas se gana el juego
ventana.fill(blanco)
# Bucle principal del juego
while ganadas<fin_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
    if (tiempo*multiplicador >= 1000): #multiplicamos estos valores para fijar el tiempo de reinicio de circulos
        ventana.fill(blanco)
        radio = random.randint(2, 20)
        x = random.randint(radio, ventana_ancho - radio)
        y = random.randint(radio, ventana_alto - radio)
        pygame.draw.circle(ventana, otro, (x, y), radio)
        multiplicador = 1
    
    if evento.type == pygame.MOUSEBUTTONDOWN:# Comprobar si el usuario hizo clic en un círculo
        pos_mouse = pygame.mouse.get_pos() #obtenemos la posicion donde se hizo el click con el mouse
        distancia = ((pos_mouse[0] - x) ** 2 + (pos_mouse[1] - y) ** 2) ** 0.5 #vemos si se hizo el click en el circulo
        pygame.time.delay(80) #esperamos unos milisegundos ya que el pc es muy rapido y 1 click puede considerarlo como N
        if distancia <= radio:     
            ganadas +=1
        contador_texto = fuente.render(f"Contador: {ganadas}", True, negro)
        ventana.blit(contador_texto, (10, 10))
        print(distancia)
    multiplicador +=1
    if ganadas >= fin_juego:
        ventana.fill(blanco)
        fin_del_juego_texto = fuente.render("Fin del Juego", True, negro)
        ventana.blit(fin_del_juego_texto, (ventana_ancho // 2 - 100, ventana_alto // 2 - 20))
        pygame.display.flip()
        time.sleep(2)  # Espera 2 segundos antes de cerrar el juego
    pygame.display.flip()
    pygame.time.delay(tiempo)
pygame.quit()