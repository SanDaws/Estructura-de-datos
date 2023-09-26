import pygame 
import time
import random

#me baso en el codigo de geeksforges, luego veo como lo hago mas optimo 

vel_serpiente= 15 #velocidad de la serpiente
ancho_ventana= 720  #tamaño en x
alto_ventana=480 #tamaño en Y       #creo que se puede quitar(@optimizar)

pygame.init() #epecempos el juego
pygame.display.set_caption('culebrita')
Ventana= pygame.display.set_mode((720,480))#revisar si solo funciona para esto el tamaño de la pantalla
fps= pygame.time.Clock() #contador de frames per second

serp_posicion= [100,50]     #cabeza de la serpiente
serp_cuerpo=[[100,50],
             [90, 50],
             [80,50] ] #cuerpo de la serpiente
manz_posicion=[random.randrange(1,(ancho_ventana//10))*10,  #define lo aleatorio de la serpiente
               random.randrange(1,(ancho_ventana//10))*10]  #alterar para una version para inicial no aleatoria
Manz_aparece= True #aparecen manzanas
direccion='right'
cambia_a=direccion







