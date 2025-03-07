import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Rect Object")
#creating a rect object
rect = pygame.Rect(0, 0, 50, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Here, we get the keys that are pressed on the keyboard.
        keys = pygame.key.get_pressed()
        #If the left arrow key is pressed, we move the rect to the left.
        if keys[pygame.K_LEFT]:
            #we change the x-coordinate of the rect by -1
            rect.x = rect.x - 1
        #If the right arrow key is pressed, we move the rect to the right.
        if keys[pygame.K_RIGHT]:
            #we change the x-coordinate of the rect by 1
            rect.x = rect.x + 1
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), rect)
    pygame.display.update()
pygame.quit()

