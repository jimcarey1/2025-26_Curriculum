import pygame
pygame.init()
width, height = 500, 500
window = pygame.display.set_mode((width, height))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Here we are storing and managing rectangular coordinates in a Rect object.
    rect = pygame.Rect(0, 50, 100, 150)
    #Here we are drawing a rectangle with top left corner at (0, 50) and width 100, height 150
    pygame.draw.rect(window, (0, 255, 0), rect)
    pygame.display.flip()


    