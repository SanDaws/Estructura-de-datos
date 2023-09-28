import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True
blanco=pygame.Color(255,255,255)
rectanglo= pygame.Rect(1,1,120,200)
while running:
    screen.fill("purple")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, blanco, rectanglo, 12)#x,y,base,altura), grosor de la linea(null=relleno)

    # fill the screen with a color to wipe away anything from last frame
    

    # RENDER YOUR GAME HERE


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()