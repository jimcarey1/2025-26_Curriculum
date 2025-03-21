#Task: Change the radius of the circle.
#Task: Change the first two numbers in the rect argument of line 18 and observe the output.

import pygame

pygame.init()
width, height = 500, 500
window = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Here we are drawing a circle with center at (250, 250) and radius 50
    pygame.draw.circle(surface = window, color= (255, 0, 0), center= (300, 300), radius=50)
    #Here we are drawing a rectangle with top left corner at (50, 50) and width 100, height 100
    pygame.draw.rect(surface=window, color=(0, 255, 0), rect=(100, 100, 100, 100))
    pygame.display.flip()