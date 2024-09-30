import pygame

class DebugStats:
    
  def __init__(self):
      self.fps = 0;
      self.font = pygame.font.Font(None, 25)

  def update(self, clock):
      self.fps = int(clock.get_fps())

  def draw(self, screen):
    fps_t = self.font.render(str(self.fps) , 1, pygame.Color("RED"))
    screen.blit(fps_t,(0,0))
