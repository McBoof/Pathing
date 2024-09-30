from math import cos
from queue import Empty
import pygame
import random
import math

class Grid:
  x=1;
  y=1;

  def __init__(self, x, y, s, n):
      self.col = (0,0,0)
      self.x = x;
      self.y = y;
      self.s = s;
      self.n = n;
      gs = round(abs(n*255));
      self.col = (gs, gs, gs)
      self.col = self.get_col_from_n(n)
      self.dotcol = None
      self.passable = True
      if (n < -0.2 or n > 0.11):
        self.passable = False

  def __str__(self):
    return f'T({self.x},{self.y})'

  def get_col_from_n(self, n):
      if (n < -0.2):
          return "blue"
      elif (n < -0.15):
        return "yellow"
      elif (n < 0.11):
        return "green"
      else:
        return "grey"

  def visit(self):
    self.dotcol  = "pink"

  def queue(self):
    self.dotcol = "orange"
  
  def update(self, clock):
      return
      
  def draw(self, screen):  
      pygame.draw.rect(screen, self.col, (
        self.x*self.s,
        self.y*self.s,
        self.s,
        self.s
      ), 0)
      if (self.dotcol):
        pygame.draw.circle(screen, self.dotcol,(self.s*(self.x+0.5),self.s*(self.y+0.5)),5,0)
