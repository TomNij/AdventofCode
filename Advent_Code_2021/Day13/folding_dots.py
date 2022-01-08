import re
from itertools import repeat
import matplotlib.pyplot as plt

with open('../Input_files/13.txt') as file:
    input = file.read().strip()

def parse(line):
    x,y = line.split(',')
    return (int(x),int(y))

def fold(dir,n,dot):
    if dir == 'x' and dot[0] > n:
        return (2 * n - dot[0],dot[1])
    elif dir == 'y' and dot[1] > n:
        return (dot[0],2 * n - dot[1])
    else:
        return dot
dots,instructions = input.split('\n\n')

dots = set(parse(line) for line in dots.split('\n'))
step = 1
for instr in instructions.split('\n'):
    pattern = 'fold along ([]xy])=(\d+)'
    dir,n = re.match(pattern,instr).groups()
    n = int(n)
    dots = set(map(fold,repeat(dir),repeat(n),dots))
    if step ==1:
        print(f"Pt 1: {len(dots)}")
    step += 1
#converts a list of tuples (x1,y1) into x and y tuples.
x, y = zip(*list(dots))
y2 = tuple(-yel for yel in y)
plt.scatter(x,y2)