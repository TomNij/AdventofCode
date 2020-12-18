from collections import Counter
from itertools import product
from operator import add


def solve(lines, cycles, dimensions):
    board = set()
    for row, line in enumerate(lines):
        for col, elem in enumerate(line):
            if elem == '#':
                cell = dimensions * [0, ]
                cell[0], cell[1] = col, row
                board.add(tuple(cell))

    for _ in range(cycles):
        new_board = set()

        neighbour_counts = Counter()
        for cell in board: #for every active cube
            delta_range = product(range(-1, 2), repeat=dimensions) #generate all possible combos of -1 to 1 in 4D, -1,1,0,1 -1,-1,1,0 etc etc.
            for delta in delta_range:
                if delta != dimensions * (0,): # exclude delta (0,0,0,0)
                    neighbour_counts[tuple(map(add, cell, delta))] += 1 #update neighbours of cell with += 1

        for cell, count in neighbour_counts.items():
            if count == 3 or (cell in board and count == 2):
                new_board.add(cell) #add indexes of next active cubes to next board
        board = new_board

    return len(board) #board is set with active cells so len(set) = #active cells.


with open('../Input_files/17.txt') as file:
    lines = file.read().splitlines()

print(solve(lines, 6, 3))
print(solve(lines, 6, 4))