#Task: Change the antialias argument in the line 10 to False and observe the output text.

import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Font Rendering")
#Here, we are creating a new custom Font object.
#We set the size of the Font to 36.
font = pygame.font.Font(None, 36)
#We then render the text "Hello, World!" using the Font object.
#The third argument is color, Here it is black color.
text = font.render(text= "Hello, World!", antialias=True, color=(0, 0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        window.fill((255, 255, 255))
        #font.render() returns a Surface object.
        #We blit this Surface object to the window using blit method.
        window.blit(text, (100, 100))
        pygame.display.flip()
pygame.quit()

