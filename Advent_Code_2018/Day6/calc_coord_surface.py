import numpy as np
import re
from collections import defaultdict
import os
print(os.path.dirname(os.path.realpath(__file__)))

f = open(".\input.txt", "r")
coords =  f.readlines()
coords = [coord.strip() for coord in coords]
f.close()
coord_arr = np.zeros((len(coords),4))

ind = 0
for item in coords:
    x,y = item.split(',')
    coord_arr[ind,:-1] = (ind,x,y)
    ind+=1


xmax = int(np.max(coord_arr[:,1])) #0 is ind, 1 = x, y = 2
ymax = int(np.max(coord_arr[:,2]))


def manh_distance(x,y,coord_arr):
    #calculate manhattan distance for each x,y to all coord in array
    #return zero if multiple coord have the same distance, return id+1 for coord that is closest, return np.inf if coord on edge
    dist_arr = abs(x-coord_arr[:,1])+abs(y-coord_arr[:,2])
    if sum(dist_arr == np.min(dist_arr)) == 1: #one coord was closest:
        coord_ind = np.argmin(dist_arr)
        if on_edge(x,y,xmax,ymax):
            coord_arr[coord_ind,3] += np.inf
        else:
            coord_arr[coord_ind, 3] += 1
    return coord_arr

def on_edge(x,y,xmax,ymax):
    xdim = xmax - 1#python counts at zero
    ydim = ymax - 1
    if (x ==0 or x == xdim or y == 0 or y == ydim):
        return True
    else:
        return False

def calc_surface(coord_arr):
    for x in range(xmax+1):
        for y in range(ymax+1):
            coord_arr = manh_distance(x,y,coord_arr)
    no_inf = coord_arr[coord_arr[:,3] != np.inf,3]
    return(np.max(no_inf))

def calc_region(coord_arr):
    region = 0
    manh_limit  = 10000
    for x in range(xmax+1):
        for y in range(ymax+1):
            dist_arr = abs(x - coord_arr[:, 1]) + abs(y - coord_arr[:, 2])
            if sum(dist_arr) < manh_limit:
                region += 1
    return region

print(calc_surface(coord_arr))
print(calc_region(coord_arr))