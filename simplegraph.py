class SimpleGraph:
  def __init__(self):
      self.edges = {
        'A': ['B'],
        'B': ['C'],
        'C': ['B', 'D', 'F'],
        'D': ['C', 'E'],
        'E': ['F'],
        'F': [],
      }

  def neighbors(self, id):
      return self.edges[id]

