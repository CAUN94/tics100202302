import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 300, 300
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Gato")

# Colores
BLANCO = (255, 255, 255)
LINEA_COLOR = (0, 0, 0)

# Tamaño del tablero y cuadrícula
TAM_CUADRO = ancho // 3
tablero = []
for _i in range(0,3):
    fila = []
    for i in range(0,3):
        fila.append(' ')
    tablero.append(fila)

# Función para dibujar el tablero
def dibujar_tablero():
    ventana.fill(BLANCO)
    for x in range(1, 3):
        pygame.draw.line(ventana, LINEA_COLOR, (x * TAM_CUADRO, 0), (x * TAM_CUADRO, alto), 2)
        pygame.draw.line(ventana, LINEA_COLOR, (0, x * TAM_CUADRO), (ancho, x * TAM_CUADRO), 2)

    for fila in range(3):
        for columna in range(3):
            jugador = tablero[fila][columna]
            if jugador == 'X':
                pygame.draw.line(ventana, LINEA_COLOR, (columna * TAM_CUADRO, fila * TAM_CUADRO),
                                 ((columna + 1) * TAM_CUADRO, (fila + 1) * TAM_CUADRO), 2)
                pygame.draw.line(ventana, LINEA_COLOR, (columna * TAM_CUADRO, (fila + 1) * TAM_CUADRO),
                                 ((columna + 1) * TAM_CUADRO, fila * TAM_CUADRO), 2)
            elif jugador == 'O':
                centro_x = columna * TAM_CUADRO + TAM_CUADRO // 2
                centro_y = fila * TAM_CUADRO + TAM_CUADRO // 2
                radio = TAM_CUADRO // 2 - 5
                pygame.draw.circle(ventana, LINEA_COLOR, (centro_x, centro_y), radio, 2)

# Función para verificar si alguien ha ganado
def verificar_ganador(jugador):
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador:
            return True
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False


jugador_actual = 'X'
juego_terminado = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
    if evento.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        columna = x // TAM_CUADRO
        fila = y // TAM_CUADRO
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador_actual
            if verificar_ganador(jugador_actual):
                print(f'¡{jugador_actual} ha ganado!')
                juego_terminado = True

            empate = True
            for fila in tablero:
                if ' ' in fila:
                    empate = False
                    break

            if empate:
                print('¡Empate!')
                juego_terminado = True

            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X"

    dibujar_tablero()
    pygame.display.update()

