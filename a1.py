import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

screen.fill((255,255,255))

pygame.draw.circle(screen, (255,0,0), (200,200), 150) 

pygame.display.update()

done = False 

if pygame.init == True :
    pygame.quit
while not done :
    for event in pygame.event.get() :
        if pygame.event == pygame.QUIT :
            done = True



pygame.quit()