import pygame
from colors import Colors

class Grid:
  def __init__(self):
    self.num_rows = 20
    self.num_columns = 10
    self.cell_size = 30
    self.grid = [[0 for j in range(self.num_columns)] for i in range (self.num_rows)]
    self.colors = Colors.get_all_colors()
    
  def draw_grid(self, screen):
    for row in range(self.num_rows):
      for column in range(self.num_columns):
        cell_value = self.grid[row][column]
        cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11, self.cell_size -1, self.cell_size -1)
        pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
      
  def is_inside(self, row, column):
    return 0 <= row < self.num_rows and 0 <= column < self.num_columns
  
  def is_empty(self, row, column):
    if self.grid[row][column] == 0:
      return True
    return False
  
  def is_row_full(self, row):
    for column in range(self.num_columns):
      if self.grid[row][column] == 0:
        return False
    return True
  
  def clean_row(self, row):
    self.grid[row] = [0 for i in range (self.num_columns)]
    
  def move_row_down(self, row, num_rows):
    self.grid[row+num_rows] = self.grid[row]
  
  def clear_full_rows(self):
    completed = 0
    for row in range(self.num_rows-1, 0, -1):
      if self.is_row_full(row):
        self.clean_row(row)
        completed += 1
      elif completed > 0:
        self.move_row_down(row, completed)
    return completed
  
  def reset(self):
    for row in range(self.num_rows):
      for col in range(self.num_columns):
        self.grid[row][col] = 0    
      
  def print_grid(self):
    for row in range (self.num_rows):
      print(self.grid[row])
      