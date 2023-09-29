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
naranja = (255, 128, 0)
rojo = (255, 0, 0)

# Dijbuja la serpiente
def serpiente_pantalla(serpiente):
    for segmento in serpiente:
        pygame.draw.rect(ventana, naranja,
                         (segmento[0] * tamanio_celda, segmento[1] * tamanio_celda, tamanio_celda, tamanio_celda))
 
# Dibuja la manzana
def manzana_pantalla(manzana):
    pygame.draw.rect(ventana, rojo,
                     (manzana[0][0] * tamanio_celda, manzana[0][1] * tamanio_celda, tamanio_celda, tamanio_celda))

# Movimiento de la serpiente
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
    # Condicional para la serpiente que no se toquen las paredes
    if 13 in cabeza or -1 in cabeza:
        controlador[2] = False # Si sucede, se actualiza el controlador (indicando la perdida del juego)
    # Condicional para cuando la serpiente se toca a si misma
    elif cabeza in serpiente:
        mostrar_mensaje_perdida()
        controlador[2] = False # Si sucede, se actualiza el controlador (indicando la perdida del juego)
    # Condicion para si la serpiente se come la manzana
    elif cabeza == list(manzana[0]):
        manzana.pop() # Se elimima la manzana
        serpiente.insert(0, cabeza) # La serpiente crece
        manzana.append((14, 14)) # Se representa la mazana fuera del tablero
        controlador[0] = True # Se actualiza el controlador de de la manzana
        controlador[3]+=1 # Este es el contador del puntaje
    # Si no pasa ninguno nde los casos anteriores, simplemente avanza la serpiente
    else:
        serpiente.insert(0, cabeza)
        serpiente.pop()

# Dibujar una manzana nueva
def manzana_nueva(serpiente, manzana):
    serpiente = [tuple(sublista) for sublista in serpiente] # Se representa la serpiente como una lista de tuplas
    todas_coordenadas = [(x, y) for x in range(13) for y in range(13)] # Se generan todas las coordenadas del tablero
    coordenadas_disponibles = [coord for coord in todas_coordenadas if coord not in serpiente and coord != manzana[0]] # Se seleccionan todas las coordenadas en las que no esta la serpiente y la manzana
    
    # Este condicional es para ver si hay espacio en el tablero
    if coordenadas_disponibles:
        posicion = random.choice(coordenadas_disponibles) # Se escoje una coordenada de manera aleatoria para dibujar la manzana
        manzana[0] = posicion # Se asigna la coordenada para la manzana
    else:
        return None #Si no hay espacio no se retorna nada

# Si se llaman cualquiera de estas dos funciones se muestra el respectivo mensaje
def mostrar_mensaje_ganar():

    fuente = pygame.font.SysFont('Agency FB', 50)   # fuente y tamaño de linea de perdida
    mensaje = fuente.render("¡Ganaste el juego!", True, naranja)
    ventana.blit(mensaje, (ancho // 2 - mensaje.get_width() // 2, alto // 2 - mensaje.get_height() // 2))


def mostrar_mensaje_perdida():

    fuente = pygame.font.SysFont('Agency FB', 50)   # fuente y tamaño de linea de perdida
    mensaje = fuente.render("¡Perdiste el juego!", True, rojo)
    ventana.blit(mensaje, (ancho // 2 - mensaje.get_width() // 2, alto // 2 - mensaje.get_height() // 2))

# Parametros iniciales
jugando = True
direccion = "arriba"  # Comienza moviéndose hacia arriba
serpiente = [(6, 6), (6, 7), (6, 8)]
manzana = [(10, 2)]
controlador = [False, random.randint(1, 10), True, 0] #  [Si no se ha comido la manzana, Numero de moviminetos aleatorios, Si no se ha perdido, contador]
jugadas = 0
tiempo_anterior = pygame.time.get_ticks()  # Inicializa el temporizador

# Velocidad de la serpiente (número de celdas por segundo)
velocidad_serpiente = 6  

# Bucle principal del juego
while jugando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
            
        # Control de la dirección de la serpiente y movimientos permitidos
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and direccion != "derecha":
                direccion = "izquierda"
            elif evento.key == pygame.K_RIGHT and direccion != "izquierda":
                direccion = "derecha"
            elif evento.key == pygame.K_UP and direccion != "abajo":
                direccion = "arriba"
            elif evento.key == pygame.K_DOWN and direccion != "arriba":
                direccion = "abajo"
        
        # Si se comio la manzana
        if controlador[0]:
            jugadas += 1
            # verificar cuantos movimientos hay que hacer para que la manzana vuelva a aparecer
            if controlador[1] == jugadas:
                manzana_nueva(serpiente, manzana)
                controlador[0] = False
                controlador[1] = random.randint(1, 10)
                jugadas = 0
        # Si la serpiente ocupa la totaliodad del tablero se llama la funcion mostrar_mensaje_ganar
    
    #Se estable un reloj interno, el temporizador se comprueba constantemente para ejecutar la funcion de moverse automaticamente
    if pygame.time.get_ticks() - tiempo_anterior >= 1000 / velocidad_serpiente:
        tiempo_anterior = pygame.time.get_ticks()
        moverse(direccion, serpiente, manzana, controlador)

    # Se actualiza constamente la pantalla en color negro, esto para desdibijar el recorrido de la serpiente
    ventana.fill(negro)

    # Mostrar el puntaje en la parte superior izquierda
    fuente_puntaje = pygame.font.Font(None, 24)
    texto_puntaje = fuente_puntaje.render(f"Puntaje: {controlador[3]}", True, blanco)
    ventana.blit(texto_puntaje, (10, 10))

    # Si aun no se ha perdido que se sigan dibujando la serpiente y la manzana
    if controlador[2] and len(serpiente)<169:
        serpiente_pantalla(serpiente)
        manzana_pantalla(manzana)
    # Si la serpiente ocupa todo el espacio del tablero se llama la funcion mostrar_mensaje_ganar
    elif len(serpiente)==169:
        mostrar_mensaje_ganar()
    # Si se pierde el juego, se llama a la funcion mostrar_mensaje_perdida
    else:
        mostrar_mensaje_perdida()
    # Cada vez que suceda un envento, es necesario que se actualice la pantalla para poder darle continuidad al juego
    pygame.display.update()

pygame.quit()