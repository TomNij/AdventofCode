from operator import attrgetter
from itertools import product
import numpy as np

from time import time



with open('../Input_files/15.txt') as file:
    input = file.readlines()

def get_neighbors(coord,diag = True):
    if diag:
        return [(coord[0] + dx,coord[1] + dy) for dx,dy in product(range(-1, 2, 1), repeat=2) if ((dx != 0) or (dy != 0))] #9 neighbors
    else:
        direct_neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        return [(coord[0] + dx,coord[1] + dy) for dx,dy in direct_neighbors]

def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func

@timer_func
def search_cave(cave):
    finish = (len(cave[0]) - 1, len(cave) - 1)

    class Node:
        def __init__(self, coord, prev):
            self.pos = coord
            x, y = coord
            if prev:
                self.prev = prev
                # method below actually penalizes nodes as we move closer to bottom right
                self.g = self.prev.g + cave[(y,x)]
            # else only applies to starting node
            else:
                self.prev = prev
                self.g = 0
            # heuristic for distance to finish
            self.h = abs(finish[0] - x) + abs(finish[1] - y)
            self.f = self.g + self.h

        def __eq__(self, other):
            return self.pos == other.pos

        # Print node
        def __repr__(self):
            return f"Node {self.pos},g:{self.g},h:{self.h},f:{self.f}"

    waiting = [Node((0, 0), None)]
    discard = []
    xdim = finish[0]
    ydim = finish[1]
    #end algorithm when finish node is the first one in the waiting queue
    while waiting[0].pos != finish:

        #get current node and find neighbours
        actual = waiting[0]
        waiting.pop(0)
        neighbors = [(x, y) for x, y in get_neighbors(actual.pos, diag= False)
                      if x in range(xdim+1) and
                      y in range(ydim+1)]
        for n_ind in neighbors:
            #check for each neighbor if its already in waiting and if g is higher -> update g value
            neighbor = Node(n_ind,actual)
            if neighbor in discard:
                continue
            elif neighbor not in waiting:
                waiting.append(neighbor)
            elif neighbor in waiting:
                n = [node for node in waiting if node == neighbor][0]
                if n.g > neighbor.g: #current waiting node g is bigger than neighbor.g so update
                    n.prev = actual
                    n.g = neighbor.g
                    n.f = n.h + neighbor.g
        #all neighbors checked and added/updated to waiting, actual can go to discard pile
        discard.append(actual)
        waiting = sorted(waiting, key=attrgetter('f'))


    #go back through discard pile and keep track of previous
    # prev = waiting[0].prev
    # path = [waiting[0].pos]
    # while prev.g != 0:
    #     path.append(prev.pos)
    #     prev = prev.prev
    #print(list(reversed(path)))
    return waiting[0].g

#pt1
cave = [list(map(int,line.strip())) for line in input]

cave = np.array(cave)
pt1 = search_cave(cave)
print(f"Part 1:{pt1}")

#first append 5 times to the right:
cavewide = cave
for incr in range(1,5):
    cavewide = np.hstack((cavewide,(cave+incr-1) % 9 + 1))

cavelong = cavewide
for incr in range(1, 5):
    cavelong = np.vstack((cavelong, (cavewide+incr-1) % 9 + 1))

pt2 = search_cave(cavelong)
print(f"Part 2:{pt2}")