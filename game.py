from grid import Grid
from blocks import*
import random
import pygame

class Game:
  def __init__(self):
    self.grid = Grid()
    self.bloks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    self.current_block = self.get_random_block()
    self.next_block = self.get_random_block()
    self.game_over = False
    self.score = 0
    self.rotate_sound = pygame.mixer.Sound("sounds/rotate.ogg")
    self.clear_sound = pygame.mixer.Sound("sounds/clear.ogg")
    pygame.mixer.music.load('sounds/music.ogg')
    pygame.mixer.music.play(-1)
    
  def get_random_block(self):
    if not self.bloks:
        self.bloks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    block = random.choice(self.bloks)
    self.bloks.remove(block)
    return block
  
  def update_score(self, rows_eliminated, move_down_points):
    if rows_eliminated == 1:
      self.score += 100
    elif rows_eliminated == 2:
      self.score += 300
    elif rows_eliminated == 3:
      self.score += 500
    self.score += move_down_points
  
  def move_left(self):
    self.current_block.move(0, -1)
    if not self.block_inside() or not self.block_fits():
      self.current_block.move(0, 1)
  
  def move_rigth(self):
    self.current_block.move(0, 1)
    if not self.block_inside() or not self.block_fits():
      self.current_block.move(0, -1)
    
  def move_down(self):
    self.current_block.move(1, 0)
    if not self.block_inside() or not self.block_fits():
      self.current_block.move(-1, 0)
      self.lock_block()
  
  def lock_block(self):
    tiles = self.current_block.get_cell_position()
    for position in tiles:
      self.grid.grid[position.row][position.column] = self.current_block.id
    self.current_block = self.next_block
    self.next_block = self.get_random_block()
    rows_cleared = self.grid.clear_full_rows()
    if rows_cleared > 0:
      self.clear_sound.play()
      self.update_score(rows_cleared, 0)
    if not self.block_fits():
      self.game_over = True
  
  def rotate(self):
    self.current_block.rotate()
    if not self.block_inside() or not self.block_fits():
      self.current_block.undo_rotation()
    else:
      self.rotate_sound.play()
  
  def block_inside(self):
    tiles = self.current_block.get_cell_position()
    for tile in tiles:
      if not self.grid.is_inside(tile.row, tile.column):
        return False
    return True
  
  def block_fits(self):
    tiles = self.current_block.get_cell_position()
    for tile in tiles:
      if not self.grid.is_empty(tile.row, tile.column):
        return False
    return True
  
  def reset(self):
    self.grid.reset()
    self.bloks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    self.current_block = self.get_random_block()
    self.next_block = self.get_random_block()
    self.score = 0
  
  def draw(self, screen):
    self.grid.draw_grid(screen)
    self.current_block.draw(screen, 11, 11)
    self.next_block.draw(screen, 270, 270)