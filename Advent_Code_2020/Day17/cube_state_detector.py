import re
import itertools
import numpy as np
import time

start = time.perf_counter()
f = open('../Input_files/17.txt')
lines = f.readlines()
lines = [line.strip() for line in lines]
f.close()

max_turns = 6
n_x = len(lines)+2*max_turns
n_y = len(lines[0])+2*max_turns
n_z = 1+2*max_turns
n_w = 1+2*max_turns


space = np.zeros((n_x,n_y,n_z,n_w))

def input_parser(line):
    arr = np.zeros((len(line)))
    for ind in range(len(line)):
        if line[ind] == '#':
            arr[ind] = 1
    return arr

def cube_state_switcher(space,space_old,xc,yc,zc,wc):
    check_ind = [(x, y, z, w)
                 for x in range(n_x)
                 for y in range(n_y)
                 for z in range(n_z)
                 for w in range(n_w)
                 if
                 abs(x - xc) <= 1 and abs(y - yc) <= 1 and abs(z - zc) <= 1 and abs(w - wc) <= 1 and not
                 (x == xc and y == yc and z == zc and w == wc)]
    # space needs to be updated, space old is the same in each turn, next turn space_old = space and space gets updated again
    count = 0
    for x, y, z, w in check_ind:
        count += space_old[x, y, z, w]
    if space_old[xc, yc, zc, wc] == 1 and count in (2, 3):
        space[xc, yc, zc, wc] = 1
    elif space_old[xc, yc, zc, wc] == 1:
        space[xc, yc, zc, wc] = 0
    elif space_old[xc, yc, zc, wc] == 0 and count == 3:
        space[xc, yc, zc, wc] = 1
    return space


for ind,line in enumerate(lines):
    space[max_turns+ind,max_turns:max_turns+len(lines[0]),max_turns,max_turns] = input_parser(line)

for turn in range(max_turns):
    print(f"Turn: {turn}")
    space_old = np.array(space)
    for xc in range(n_x):
        for yc in range(n_y):
            for zc in range(n_z):
                for wc in range(n_w):
                    space = cube_state_switcher(space,space_old,xc,yc,zc,wc)


print(np.sum(space))