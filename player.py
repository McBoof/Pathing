import pygame
import random

class Player:
  x=1;
  y=1;
  width=20;
  height=20;
  col = (255, 0, 0);

  def __init__(self):
      self.col = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
      );
      self.x = random.randint(0, 400);
      self.y = random.randint(0, 400);

  def update(self, clock):
      self.x += random.randint(-3, 3);
      self.y += random.randint(-3, 3);

  def draw(self, screen):
      pygame.draw.rect(screen, self.col, (self.x, self.y, self.width, self.height)) 
