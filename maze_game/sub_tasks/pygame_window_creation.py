#Task1: Change the values of width, height and then observe the size of the window.
#Task2: Change the title and background colour of the window.

import pygame #importing the pygame module

pygame.init() #initialize the pygame module

#setting the width and height of the window
width, height = 500, 500

#creating the window with the specified width and height
window = pygame.display.set_mode((width, height))