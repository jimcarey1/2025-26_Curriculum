import pygame 

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Drawing two rectangle objects")

rect1 = pygame.Rect(0, 0, 100, 150)
rect2 = pygame.Rect(150, 50, 70, 90)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(window, (255, 0, 0), rect1)
    pygame.draw.rect(window, (0, 255, 0), rect2)
    pygame.display.update()
