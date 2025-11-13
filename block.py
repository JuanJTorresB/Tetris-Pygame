from colors import Colors
from position import Position
import pygame

class Block:
  def __init__(self, id):
    self.id = id
    self.cells = {}
    self.cell_size = 30
    self.row_offset = 0
    self.column_offset = 0
    self.rotation_state = 0
    self.colors = Colors.get_all_colors()
  
  def move(self, rows, columns):
    self.row_offset += rows
    self.column_offset += columns
  
  def get_cell_position(self):
    titles = self.cells[self.rotation_state]
    moved_tiles = []
    for position in titles: 
      position = Position(position.row + self.row_offset, position.column + self.column_offset)
      moved_tiles.append(position)
    return moved_tiles
  
  def rotate(self):
    self.rotation_state += 1
    if self.rotation_state == len(self.cells):
      self.rotation_state = 0

  def undo_rotation(self):
    self.rotation_state -= 1
    if self.rotation_state == -1:
      self.rotation_state = len(self.cells) -1
  
  def draw(self, screen, offsety, offsetx):
    titles = self.get_cell_position()
    for tile in titles:
      tile_rect = pygame.Rect(tile.column * self.cell_size + offsetx, tile.row * self.cell_size + offsety, self.cell_size - 1, self.cell_size - 1)
      pygame.draw.rect(screen, self.colors[self.id], tile_rect)