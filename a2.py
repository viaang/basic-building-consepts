import pygame

pygame.init()
screen = pygame.display.set_mode((400,400)) 
screen.fill((255,255,255))



pygame.draw.circle(screen,(0,0,255),(200,200), 100, 2)

pygame.display.update()

done = False

while not done :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True

pygame.quit()