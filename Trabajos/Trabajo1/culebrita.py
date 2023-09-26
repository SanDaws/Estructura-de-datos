import pygame 
import time
import random

#me baso en el codigo de geeksforges, luego veo como lo hago mas optimo 
def game_over():
    letra_tipo= pygame.pygame.font.SysFont('Agency FB', 50)     #establecemos una letra para fuente (use una que me gusto, no se si esta en otro sistema)
    superficie_GO= letra_tipo.pygame.font.render('Fin del Juego', True, pygame.Color(225,0,0))  #eso lo pondremos en un color y que diga algo
    rectangulo_GO=rectangulo_GO.Surface.get_rect()  #esto crea un rectangulo
    rectangulo_GO.midtop=(ancho_ventana/2,alto_ventana/2) #ubicacion del rectangulo
    Ventana.pygame.Surface.blit(superficie_GO,rectangulo_GO)    #hace que el rectangulo sea una superficie
    pygame.display.flip()   #ni idea
    time.sleep(2)# tiempo de 2 segundos              (debo ver como hago un while con esto)
    pygame.quit()# se acaba el juego                (debo poner que esto sea condicional para reiniciar)
    quit()#se acaba el programa                     (si lo anteior sucede, esto no puede suceder)


vel_serpiente= 15 #velocidad de la serpiente
ancho_ventana= 720  #tamaño en x
alto_ventana=480 #tamaño en Y       #creo que se puede quitar(@optimizar)

pygame.init() #epecempos el juego
pygame.display.set_caption('culebrita')
Ventana= pygame.display.set_mode((ancho_ventana,alto_ventana))#revisar si solo funciona para esto el tamaño de la pantalla
fps= pygame.time.Clock() #contador de frames per second

serp_posicion_inicial=[ancho_ventana//2,alto_ventana//2]
serp_posicion= [100,50]     #cabeza de la serpiente
serp_cuerpo=[[100,50],
             [90, 50],
             [80,50] ] #cuerpo de la serpiente
manz_posicion=[random.randrange(1,(ancho_ventana//10))*10,  #define lo aleatorio de la serpiente
               random.randrange(1,(ancho_ventana//10))*10]  #alterar para una version para inicial no aleatoria
Manz_aparece= True #aparecen manzanas
direccion='right'
cambia_a=direccion
main()

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



