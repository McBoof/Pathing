import sys
import pygame
import math
import queue

from pygame.locals import QUIT
from pygame.locals import KEYDOWN
from pygame.locals import MOUSEBUTTONDOWN

from debugstats import DebugStats
from map import Map

from player import Player
from simplegraph import SimpleGraph




def loop(gameobjects, screen, clock):
    for gameobj in gameobjects:
        gameobj.update(clock)
    
    screen.fill((255, 255, 255))   
    
    for gameobj in gameobjects:
        gameobj.draw(screen)
    
    clock.tick(5)
    pygame.display.flip()

def breadth_first_search(graph, start, end):
    frontier = queue.Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    

    while not frontier.empty():
        current = frontier.get()
        # print("  Visiting %s" % current)
        current.visit()
        if (current == end):
            print("Yay")
            break
        loop(gameobjects, screen, clock)

        for next in graph.neighbors(current):
            if next not in came_from:
                next.queue()
                frontier.put(next)
                came_from[next] = current


def handleEvents():
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        print("hello " +  str(event.key))
      if event.type == MOUSEBUTTONDOWN:
        print("hello " +  str(event.pos))

pygame.init()

width=500
height=400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption('Hello Test World!')

map = Map(20,20)

gameobjects = []
gameobjects.append(map)
gameobjects.append(Player())
gameobjects.append(Player())
gameobjects.append(Player())
gameobjects.append(DebugStats())

start = map.tiles[3][3]
end = map.tiles[12][15]
start.col = "purple"
end.col = "red"
print('Reachable from ' + str(start))
breadth_first_search(map, start, end)

'''
example_graph = SimpleGraph()
print('Reachable from A:')
breadth_first_search(example_graph, 'A', None)

print('Reachable from E:')
breadth_first_search(example_graph, 'E')
'''

while True:

    handleEvents()
    loop(gameobjects, screen, clock)

'''
In Pygame, both pygame.display.update() and pygame.display.flip() are used to update the display surface (i.e., the screen) during your game loop, but they function slightly differently in terms of what they update and when they should be used.
'''
