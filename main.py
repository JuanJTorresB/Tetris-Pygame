import pygame
import sys
from game import Game

pygame.init()
primary_color = (245, 245, 245)

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, (0, 0, 0))
next_surface = title_font.render("Next", True, (0, 0, 0))
game_over_surface = title_font.render("Game Over", True, (0, 0, 0))

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)


width = 500
height = 620

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if game.game_over == True:
        game.game_over = False
        game.reset()
      if event.key == pygame.K_LEFT and not game.game_over:
        game.move_left()
      if event.key == pygame.K_RIGHT and not game.game_over:
        game.move_rigth()
      if event.key == pygame.K_DOWN and not game.game_over:
        game.move_down()
      if event.key == pygame.K_UP and not game.game_over:
        game.rotate()
    if event.type == GAME_UPDATE and not game.game_over:
      game.move_down()
        
  screen.fill(primary_color)
  screen.blit(score_surface, (365, 20, 50, 50))
  screen.blit(next_surface, (365, 180, 50, 50))
  
  if game.game_over:
    screen.blit(game_over_surface, (320, 450, 50, 50))
  
  pygame.draw.rect(screen, (10,10,10), score_rect, 0, 10)
  pygame.draw.rect(screen, (10,10,10), next_rect, 0, 10)
  
  game.draw(screen)
  
  pygame.display.update()
  clock.tick(60)