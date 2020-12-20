import re
import math
import numpy as np
#1 parse puzzle pieces
with open('../Input_files/20_test.txt') as file:
    input = file.read().split('\n\n')

puzzle_dim = math.sqrt(len(input)) #testinput sqrt(9) = 3
puzzle_dict = {}
id_expr = 'Tile (\d+):'
tot_set = set()

def flip_right(puzzle):
    return [row[::-1] for row in puzzle]

def rotate_right(puzzle):
    ans = []
    for col in range(len(puzzle)):
        row = [puzzle[n][col] for n in range(len(puzzle)-1,-1,-1)]
        ans.append(row)
    return ans

for puzzle in input:
    puzzle = puzzle.split('\n')
    id = re.search(id_expr, puzzle[0]).group(1)
    top_rev = puzzle[1]
    bottom = puzzle[-1]
    left_rev = [puzzle[n][0] for n in range(1,len(puzzle))]
    left_rev = ''.join(left_rev)
    right = [puzzle[n][-1] for n in range(1,len(puzzle))]
    right = ''.join(right)
    top = top_rev[::-1]
    b_rev = bottom[:: -1]
    left = left_rev[::-1]
    r_rev = right[::-1]
    puzzle_dict[id] = [(top,right,bottom,left),(top_rev,r_rev,b_rev,left_rev)]
    no_edges = [line[1:len(line)-1] for line in puzzle[2:len(puzzle)-1]] #skip line 0: contains piece ID, skip line 1: part of edge
    puzzle_dict[id].append(no_edges)
    tot_set.update([top,bottom,left,right,left_rev,r_rev,b_rev,top_rev])

a = 1
#2 try brute force:
# create set of all puzzle piece edges: dict{id, set( 8 * edges)}
# for edge in puzzle piece go over all ids except own see if at least 2 sides match, if not add to answer set.
corners = []
for key in puzzle_dict.keys():
    puzzle_match = 0
    allsides = list(puzzle_dict[key][0])
    allsides.extend(list(puzzle_dict[key][1]))
    for side in allsides: #append regular and flipped tuples
        side_match = 0
        for key2 in puzzle_dict.keys():
            if key != key2:
                allsides2 = list(puzzle_dict[key2][0])
                allsides2.extend(list(puzzle_dict[key2][1]))
                for side2 in allsides2: #append regular and flipped tuples
                    if side == side2:
                        side_match += 1 #we dont need to count how many potential matches there are
                        break
        if side_match > 0:
            puzzle_match += 1
    print(f"Piece: {key} has {puzzle_match} matching sides")
    if puzzle_match == 4:
        corners.append(key)


ans = 1
for val in corners:
    ans *= int(val)
print(f"Part 1: {ans}")

#start puzzle solution with (x,y,piece_id):[(edges),piece without edges]
xy_delta = {0:(0,1),
            1:(1,0),
            2: (0,-1),
            3: (-1,0)}
puzzle_solution = {(0,0,corners[0]): [puzzle_dict[corners[0]][0],puzzle_dict[corners[0]][2]]}
x,y = 0,0
id = corners[0]
piece_check = [(x,y,id)]
while piece_check:
    x,y,id = piece_check[0]
    for orient,side in enumerate(puzzle_solution[(x,y,id)][0]): #orientation 0: top, 1: right, 2: bottom, 3: left
        for key in puzzle_dict.keys():
            if id != key:
                # puzzle_dict[key] = [(t,r,b,l),(reverse),list(8)]
                for orient2,side_set in enumerate(puzzle_dict[key][0:2]):
                    for side2 in side_set:
                        if side == side2:
                            x += xy_delta[orient][0] #update x pos of piece with the delta
                            y += xy_delta[orient][1]
                            key = key
                            puzzle_piece = puzzle_dict[key][2]
                            #depending on orient and orient2 we add the puzzle piece to the puzzle solution
                            side_match += 1  # we dont need to count how many potential matches there are
                            break