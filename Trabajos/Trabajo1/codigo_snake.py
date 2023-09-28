import pygame
import random

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
verde = (255, 128, 0)
rojo = (255, 0, 0)



def serpiente_pantalla(serpiente):
    """Representa la serpiente en la pantalla"""
    for segmento in serpiente:
        pygame.draw.rect(ventana, verde,
                         (segmento[0] * tamanio_celda, segmento[1] * tamanio_celda, tamanio_celda, tamanio_celda))
def manzana_pantalla(manzana):
    """Representa la manzana en la pantalla"""
    pygame.draw.rect(ventana,rojo,
                     (manzana[0][0] * tamanio_celda, manzana[0][1] * tamanio_celda, tamanio_celda, tamanio_celda))
def moverse(direccion, serpiente, manzana, controlador):
    """Determina el proximo movimiento y si es valido"""
    cabeza = list(serpiente[0])

    #Determina las coordenadas
    if direccion == "izquierda":
        cabeza[0] -= 1
    elif direccion == "derecha":
        cabeza[0] += 1
    elif direccion == "arriba":
        cabeza[1] -= 1
    elif direccion == "abajo":
        cabeza[1] += 1

    #Termina el juego si toca una pared
    if 13 in cabeza or -1 in cabeza:
        controlador[2]=False
    #Termina el juego si se toca asi misma
    elif cabeza in serpiente:
        mostrar_mensaje_perdida()
        controlador[2]=False
    #Crece si se come la comida
    elif cabeza==list(manzana[0]):
        manzana.pop()
        serpiente.insert(0, cabeza)
        manzana.append((14,14))
        controlador[0]=True
    #Simplemente se mueve
    else:
        serpiente.insert(0, cabeza)
        serpiente.pop()

def manzana_nueva(serpiente,manzana):
    """Crea una nueva manzana en pantalla"""

    serpiente = [tuple(sublista) for sublista in serpiente]
    # todas las coordenadas posibles en el tablero
    todas_coordenadas = [(x, y) for x in range(13) for y in range(13)]
    # Filtrar las coordenadas para eliminar las que están ocupadas por la serpiente
    coordenadas_disponibles = [coord for coord in todas_coordenadas if coord not in serpiente and coord != manzana[0]]
    # Verificar si hay coordenadas disponibles
    if coordenadas_disponibles:
        # Elegir dos coordenadas aleatorias de las disponibles
        posicion = random.choice(coordenadas_disponibles)
        manzana[0] = posicion

    else:
        # No hay coordenadas disponibles, el juego está lleno
        return None

def mostrar_mensaje_perdida():
        """Termina el juego mostrando el mensaje cuando se pierde"""
        fuente = pygame.font.Font(None, 36)  # Fuente y tamaño
        mensaje = fuente.render("¡Perdiste el juego!", True, rojo)  # Texto y color
        ventana.blit(mensaje, (ancho // 2 - mensaje.get_width() // 2, alto // 2 - mensaje.get_height() // 2))

#Estados iniciales
jugando = True
direccion=""
#La serpiente es una lista de coordenadas
serpiente=[(6,6),(6,7),(6,8)]
#La manzana se representa mediante la segunda tupla
manzana=[(10,2)]
#El controlador tiene el booleano de si se comio la manzana, un numero aleatorio para aparecerla y un booleano para determinar que se pierda o se siga el juego
controlador=[False, random.randint(1, 10), True]
jugadas=0
# Bucle principal del juego
while jugando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        # Control de la dirección de la serpiente
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if direccion!="derecha":
                direccion = "izquierda"
                moverse(direccion, serpiente, manzana, controlador)

        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            if direccion!="izquierda":
                direccion = "derecha"
                moverse(direccion, serpiente, manzana, controlador)

        elif pygame.key.get_pressed()[pygame.K_UP]:
            if direccion!="abajo":
                direccion = "arriba"
                moverse(direccion, serpiente, manzana, controlador)

        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            if direccion!="arriba" and direccion!="":
                direccion = "abajo"
                moverse(direccion, serpiente, manzana, controlador)

        #Si el c[0] cambia durante el movimiento a True quiere decir que se comio la manzana
        if controlador[0]:
            jugadas+=1
            #Si el numero de jugadas es igual al numero aleatorio aparece una nueva manzana
            if controlador[1]==jugadas:
                manzana_nueva(serpiente, manzana)
                controlador[0]=False
                controlador[1]=random.randint(1,10)
                jugadas=0


    # Dibujar el tablero
    ventana.fill(negro)
    """for fila in range(ancho_tablero):
        for columna in range(alto_tablero):
            pygame.draw.rect(ventana, blanco, (columna * tamanio_celda, fila * tamanio_celda, tamanio_celda, tamanio_celda), 1)"""
    #Si c[2] es True significa que no ha perdido
    if controlador[2]:
        serpiente_pantalla(serpiente)
        manzana_pantalla(manzana)
    else:
        mostrar_mensaje_perdida()



    pygame.display.update()

pygame.quit()
