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
            self.prev = prev
            self.status = 'open'
            self.g = 0
            self.h = 0
            self.f = 0

        def __eq__(self, other):
            return self.pos == other.pos

        def __gt__(self, other):
            return self.f > other.f

        # Print node
        def __repr__(self):
            return f"Node {self.pos},g:{self.g},h:{self.h},f:{self.f}"

    start = Node((0, 0), None)
    start.g = 0
    start.h = abs(finish[0]) + abs(finish[1])
    start.f = start.g + start.h
    node_dict = {(0,0):start}
    finish_node = Node(finish, None)

    waiting = [start]
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
            x,y = n_ind
            #check for each neighbor if its already in waiting and if g is higher -> update g value
            neighbor = Node(n_ind,actual)
            if n_ind not in node_dict.keys():
                node_dict[n_ind] = neighbor
                neighbor.g = actual.g + cave[(x,y)]
                neighbor.h = abs(finish[0] - x) + abs(finish[1] - y)
                neighbor.f = neighbor.g + neighbor.h
            else:
                neighbor = node_dict[n_ind]
                #check if existing node had a higher g value than what we would assign from actual node.
                if actual.g + cave[(x,y)] < neighbor.g:
                    neighbor.g = actual.g + cave[(x,y)]
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.prev = actual


            if node_dict[n_ind].status == 'discard':
                continue
            elif node_dict[n_ind].status == 'open':
                node_dict[n_ind].status = 'waiting'
                waiting.append(neighbor)

        #all neighbors checked and added/updated to waiting, actual can go to discard pile
        node_dict[actual.pos].status = 'discard'
        #sort waiting list by f-value
        waiting.sort(key=attrgetter('f'))
    #after quiting while loop the first entry is the finish node and g is the value we want.
    return waiting[0].g

#pt1
cave = [list(map(int,line.strip())) for line in input]

cave = np.array(cave)
print(f"Part 1:{search_cave(cave)}")

cave2 = cave
#append to right
for incr in range(1, 5):
    cave2 = np.hstack((cave2, (cave + incr - 1) % 9 + 1))
cavewide = cave2
for incr in range(1, 5):
    cave2 = np.vstack((cave2, (cavewide + incr - 1) % 9 + 1))

print(f"Part 2:{search_cave(cave2)}")