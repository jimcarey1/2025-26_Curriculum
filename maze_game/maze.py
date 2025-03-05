#Task: Run the game and collide with the obstacle. Observe the screen doesn't flicker. Which line of code is responsible for this?

import pygame

green = (0, 255, 0)
brown = (110, 38, 14)
blue = (0, 0, 255)

window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

obstacles = [
    pygame.Rect(0, 0, 400, 50),
    pygame.Rect(60, 90, 50, 200),
    pygame.Rect(200, 150, 400, 50),
    pygame.Rect(60, 280, 150, 50),
    pygame.Rect(180, 350, 200, 50),
    pygame.Rect(450, 420, 30, 200)
]

player_x, player_y = 0, 450
player_speed = 1

pygame.font.init()
font = pygame.font.Font(None, 36)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    player_x += player_speed
    print(player_x)
  if keys[pygame.K_LEFT]:
    player_x -= player_speed
  if keys[pygame.K_UP]:
    player_y -= player_speed
  if keys[pygame.K_DOWN]:
    player_y += player_speed

  window.fill((255, 255, 255))

  player = pygame.draw.rect(window, green, (player_x, player_y, 50, 50))

  win = pygame.draw.rect(window, blue, (450, 0, 70, 70))

  for obstacle in obstacles:
    if player.colliderect(obstacle):
      game_over_text = font.render('Game Over', True, (255, 0, 0))
      window.blit(game_over_text, (230, 250))
      pygame.display.update()
      pygame.time.delay(2000)  #adding delay
      pygame.quit()  #to close window after 2 seconds

  if player.colliderect(win):
    you_win_text = font.render('You Win', True, (0, 255, 0))
    window.blit(you_win_text, (230, 250))

  for object in obstacles:
    pygame.draw.rect(window, brown, object)

  pygame.display.update()