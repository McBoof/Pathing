from math import cos
import pygame
import random
import math

class HexGrid:
  x=1;
  y=1;
  r=30;
  height=20;
  gap = 4;
  col = (255, 0, 0);

  def __init__(self, x, y):
      self.col = (0,0,0)
      self.x = x;
      self.y = y;
      print("Made new grid at " + str(x) + "," + str(y))
    
  def update(self, clock):
      return
      
  def draw(self, screen):
      y_diff =  math.sin(math.radians(60)) * self.r
      
      points = [
          (self.x - self.r/2, self.y - y_diff),
          (self.x + self.r/2, self.y - y_diff),
          (self.x + self.r, self.y),
          (self.x + self.r/2, self.y + y_diff),
          (self.x - self.r/2, self.y + y_diff),
          (self.x - self.r, self.y)
      ]
      pygame.draw.polygon(screen, self.col, points, 3) 
