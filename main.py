import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))

done = False

while not done :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True 
    pygame.draw.rect(screen, (250,0,0),pygame.Rect(6,6,300,150))
    pygame.display.flip()