import numpy as np
import re
with open('../Inputs/6.txt') as file:
    input = file.readlines()
input = [line.strip() for line in input]

def line_parser(line):
    expr = '(\w+) (\d+),(\d+) through (\d+),(\d+)'
    action,x1,y1,x2,y2 = re.search(expr,line).groups()
    return action,int(x1),int(y1),int(x2),int(y2)
#define rectangle on 2 coord
grid_pt1 = np.zeros((1000,1000)) - 1 #start at -1 to indicate off
grid_pt2 = np.zeros((1000,1000))  #start at 0

for line in input:
    action,x1,y1,x2,y2 = line_parser(line)
    if action == 'on':
        grid_pt1[x1:x2+1,y1:y2+1] = 1
        grid_pt2[x1:x2 + 1, y1:y2 + 1] += 1
    elif action == 'off':
        grid_pt1[x1:x2+1,y1:y2+1] = -1
        subgrid = grid_pt2[x1:x2 + 1, y1:y2 + 1]
        subgrid[subgrid >= 1] -= 1
        grid_pt2[x1:x2 + 1, y1:y2 + 1] = subgrid
    elif action == 'toggle':
        grid_pt1[x1:x2+1,y1:y2+1] = -1 * grid_pt1[x1:x2+1,y1:y2+1]
        grid_pt2[x1:x2 + 1, y1:y2 + 1] += 2

print(f"Part 1: {np.sum(grid_pt1[grid_pt1 == 1])}")
print(f"Part 2: {np.sum(grid_pt2)}")
