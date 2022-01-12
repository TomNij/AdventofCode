import numpy as np
from itertools import combinations,permutations,product


with open('../Input_files/11.txt') as file:
    input = file.readlines()

input = [list(map(int,line.strip())) for line in input]
octo_arr = np.array(input)

def get_neighbors(coord,diag = True):
    if diag:
        return [(coord[0] + dx,coord[1] + dy) for dx,dy in product(range(-1, 2, 1), repeat=2) if ((dx != 0) or (dy != 0))] #9 neighbors
    else:
        direct_neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        return [(coord[0] + dx,coord[1] + dy) for dx,dy in direct_neighbors]

flash_count = 0
xdim = np.shape(octo_arr)[0]
ydim = np.shape(octo_arr)[1]
for step in range(1000):
    octo_arr += 1
    flash_list = []
    #determine good method to check if a new flash is needed.
    while np.max(octo_arr) > 9:
        flash_ind = np.argmax(octo_arr)
        #convert 14 into 1,4
        flash_coord = (flash_ind // xdim, flash_ind % xdim)
        neighbors = [(x,y) for x,y in get_neighbors(flash_coord)
                     if x in range(xdim) and
                      y in range(ydim)]
        for n in neighbors:
            octo_arr[n] += 1
        flash_list.append(flash_coord)
        octo_arr[flash_coord] = -9999
    for f in flash_list:
        octo_arr[f] = 0
    flash_count += len(flash_list)
    if np.max(octo_arr) == 0:
        print(f"Part 2: {step+1}")
        break


#2904 too high
print(f"Part 1: {flash_count}")