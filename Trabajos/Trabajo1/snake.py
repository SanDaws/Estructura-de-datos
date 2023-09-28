import pygame
import random
import time

# Inicialización de pygame
pygame.init()

# Dimensiones del tablero
ancho_tablero = 13
alto_tablero = 13

# Tamaño de cada celda en el tablero
tamanio_celda = 30

# Configuración de la pantalla
ancho = ancho_tablero * tamanio_celda
alto = alto_tablero * tamanio_celda
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
naranja = (255, 128, 0)
rojo = (255, 0, 0)

def serpiente_pantalla(serpiente):
    for segmento in serpiente:
        pygame.draw.rect(ventana, naranja,
                         (segmento[0] * tamanio_celda, segmento[1] * tamanio_celda, tamanio_celda, tamanio_celda))

def manzana_pantalla(manzana):
    pygame.draw.rect(ventana, rojo,
                     (manzana[0][0] * tamanio_celda, manzana[0][1] * tamanio_celda, tamanio_celda, tamanio_celda))

def moverse(direccion, serpiente, manzana, controlador):
    cabeza = list(serpiente[0])

    if direccion == "izquierda":
        cabeza[0] -= 1
    elif direccion == "derecha":
        cabeza[0] += 1
    elif direccion == "arriba":
        cabeza[1] -= 1
    elif direccion == "abajo":
        cabeza[1] += 1

    if 13 in cabeza or -1 in cabeza:
        controlador[2] = False
    elif cabeza in serpiente:
        mostrar_mensaje_perdida()
        controlador[2] = False
    elif cabeza == list(manzana[0]):
        manzana.pop()
        serpiente.insert(0, cabeza)
        manzana.append((14, 14))
        controlador[0] = True
    else:
        serpiente.insert(0, cabeza)
        serpiente.pop()

def manzana_nueva(serpiente, manzana):
    serpiente = [tuple(sublista) for sublista in serpiente]
    todas_coordenadas = [(x, y) for x in range(13) for y in range(13)]
    coordenadas_disponibles = [coord for coord in todas_coordenadas if coord not in serpiente and coord != manzana[0]]
    
    if coordenadas_disponibles:
        posicion = random.choice(coordenadas_disponibles)
        manzana[0] = posicion
    else:
        return None

def mostrar_mensaje_perdida():
    fuente = pygame.font.Font(None, 36)
    mensaje = fuente.render("¡Perdiste el juego!", True, rojo)
    ventana.blit(mensaje, (ancho // 2 - mensaje.get_width() // 2, alto // 2 - mensaje.get_height() // 2))

jugando = True
direccion = "arriba"  # Comienza moviéndose hacia arriba
serpiente = [(6, 6), (6, 7), (6, 8)]
manzana = [(10, 2)]
controlador = [False, random.randint(1, 10), True]
jugadas = 0
tiempo_anterior = pygame.time.get_ticks()  # Inicializa el temporizador

# Velocidad de la serpiente (número de celdas por segundo)
velocidad_serpiente = 1  # Puedes ajustar este valor para hacerla más lenta

# Bucle principal del juego
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        # Control de la dirección de la serpiente
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and direccion != "derecha":
                direccion = "izquierda"
            elif evento.key == pygame.K_RIGHT and direccion != "izquierda":
                direccion = "derecha"
            elif evento.key == pygame.K_UP and direccion != "abajo":
                direccion = "arriba"
            elif evento.key == pygame.K_DOWN and direccion != "arriba":
                direccion = "abajo"

        if controlador[0]:
            jugadas += 1
            if controlador[1] == jugadas:
                manzana_nueva(serpiente, manzana)
                controlador[0] = False
                controlador[1] = random.randint(1, 10)
                jugadas = 0

    if pygame.time.get_ticks() - tiempo_anterior >= 1000 / velocidad_serpiente:
        tiempo_anterior = pygame.time.get_ticks()
        moverse(direccion, serpiente, manzana, controlador)

    ventana.fill(negro)
    

    if controlador[2]:
        serpiente_pantalla(serpiente)
        manzana_pantalla(manzana)
    else:
        mostrar_mensaje_perdida()

    pygame.display.update()

pygame.quit()
