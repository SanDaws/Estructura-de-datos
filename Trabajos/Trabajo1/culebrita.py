import pygame 
import time
import random

#me baso en el codigo de geeksforges, luego veo como lo hago mas optimo 
def game_over():
    letra_tipo= pygame.pygame.font.SysFont('Agency FB', 50)     #establecemos una letra para fuente (use una que me gusto, no se si esta en otro sistema)
    superficie_GO= letra_tipo.pygame.font.render('Fin del Juego', True, pygame.Color(225,0,0))  #eso lo pondremos en un color y que diga algo
    rectangulo_GO=rectangulo_GO.Surface.get_rect()  #esto crea un rectangulo
    rectangulo_GO.midtop=(ancho_ventana/2,alto_ventana/2) #ubicacion del rectangulo
    ventana.pygame.Surface.blit(superficie_GO,rectangulo_GO)    #hace que el rectangulo sea una superficie
    pygame.display.flip()   #ni idea
    time.sleep(2)# tiempo de 2 segundos              (debo ver como hago un while con esto)
    pygame.quit()# se acaba el juego                (debo poner que esto sea condicional para reiniciar)
    quit()#se acaba el programa                     (si lo anteior sucede, esto no puede suceder)


vel_serpiente= 15 #velocidad de la serpiente
ancho_ventana= 720  #tamaño en x                                
alto_ventana=480 #tamaño en Y       #creo que se puede quitar(@optimizar)
        #72 x 48 de interfaz, ahora necesito hacerlo de 13 x 13(delimitar sin reducir, puedo aumentar el tamaño de todo)

#colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init() #epecempos el juego
pygame.display.set_caption('culebrita')
ventana= pygame.display.set_mode((ancho_ventana,alto_ventana))#revisar si solo funciona para esto el tamaño de la pantalla
fps= pygame.time.Clock() #contador de frames per second

serp_posicion_inicial=[ancho_ventana//2,alto_ventana//2]
serp_posicion= [100,50]     #cabeza de la serpiente
serp_cuerpo=[[100,50],
             [90, 50],
             [80,50] ] #cuerpo de la serpiente
manz_posicion=[random.randrange(1,(ancho_ventana//10))*10,  #define lo aleatorio de la serpiente
               random.randrange(1,(ancho_ventana//10))*10]  #alterar para una version para inicial no aleatoria
manz_aparece= True #aparecen manzanas
direccion='right'
cambia_a=direccion



def main():
    while True:
        for event in pygame.event.get():# esto muestra el movimiento (vere si lo puedo optimizar)
            if event.key== pygame.K_D:
                cambia_a='right'
            if event.key== pygame.K_A:
                cambia_a='left'
            if event.key== pygame.K_W:
                cambia_a='up'
            if event.key== pygame.K_S:
                cambia_a='down'     
         #evita la mezcla de 2 botones a oprimirce juntos se anulen          uno anula al otro   
        if cambia_a =='up' and direccion != 'down': direccion= 'up'
        if cambia_a =='down' and direccion != 'up': direccion= 'down'
        if cambia_a =='left' and direccion != 'right': direccion= 'left'
        if cambia_a =='rigth' and direccion != 'left': direccion= 'right'
		#movimineto
        if direccion == 'UP':
            serp_posicion[1] -= 10
        if direccion == 'DOWN':
            serp_posicion[1] += 10
        if direccion == 'LEFT':
            serp_posicion[0] -= 10
        if direccion == 'RIGHT':
            serp_posicion[0] += 10
        #intecambia posiciones
        serp_cuerpo.insert(0, list(serp_posicion))
        if serp_posicion[0] == fruit_position[0] and serp_posicion[1] == fruit_position[1]:
            manz_aparece = False
        else:
            serp_cuerpo.pop()
        
        if not manz_aparece:
            fruit_position = [random.randrange(1, (ancho_ventana//10)) * 10,
			random.randrange(1, (alto_ventana//10)) * 10]
        manz_aparece = True
        ventana.fill(black)


        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(vel_serpiente)

		            
main()
# Main Function


    
if not manz_aparece:
    fruit_position = [random.randrange(1, (ancho_ventana//10)) * 10,
                    random.randrange(1, (alto_ventana//10)) * 10]
    
manz_aparece = True
ventana.fill(black)

for pos in serp_cuerpo:
    pygame.draw.rect(ventana, green, pygame.Rect(
    pos[0], pos[1], 10, 10))
    
pygame.draw.rect(ventana, white, pygame.Rect(
fruit_position[0], fruit_position[1], 10, 10))

# Game Over conditions
if serp_posicion[0] < 0 or serp_posicion[0] > window_x-10:
    game_over()
if serp_posicion[1] < 0 or serp_posicion[1] > window_y-10:
    game_over()

# Touching the snake body
for block in serp_cuerpo[1:]:
    if serp_posicion[0] == block[0] and serp_posicion[1] == block[1]:
        game_over()


