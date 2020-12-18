#AoC 2020 day 17
from itertools import product
from operator import add
delta_range = product(range(-1, 2), repeat=dimensions) #generate all possible combos of -1 to 1 in 4D, -1,1,0,1 -1,-1
    if delta != dimensions * (0,):
        neighbour_counts[tuple(map(add, cell, delta))]
