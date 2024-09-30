import noise 
from grid import Grid

class Map:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.tiles = [[0 for xx in range(x)] for yy in range(y)]

    for i in range(0,self.x):
        for j in range(0,self.y):
          self.tiles[i][j] = (Grid(i,j,round(300/x),
                noise.pnoise2(j/self.x, i/self.y, 6, 5)
                    #octaves=6, persistence=0.5, lacunarity=2,
                    #repeatx=x_cells, repeaty=y_cells, base=23
            ))

  def inbounds(self, x, y):
    if (x < 0 or x >= self.x or y < 0 or y >= self.y):
      return False;
    print(x,y)
    return True

  def neighbors(self, id):
    n = [];
    for i in [[1,0],[-1,0],[0,1],[0,-1]]:
        print(i)
        if (self.inbounds(id.x + i[0],id.y + i[1]) and self.tiles[id.x + i[0]][id.y + i[1]].passable):
          n.append(self.tiles[id.x + i[0]][id.y + i[1]])
      
    return n

  def update(self, clock):
    return
  
  def draw(self, screen):  
    for i in range(0,self.x):
      for j in range(0,self.y):
        self.tiles[i][j].draw(screen)