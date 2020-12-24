import math
import re
from collections import deque


#1 parse puzzle pieces
with open('../Input_files/20.txt') as file:
    input = file.read().split('\n\n')

puzzle_dim = math.sqrt(len(input)) #testinput sqrt(9) = 3
puzzle_dict = {}
id_expr = 'Tile (\d+):'
tot_set = set()

def flip_right(puzzle):
    ans = [row[::-1] for row in puzzle]
    return ans

def rotate_right(puzzle):
    ans = []
    for col in range(len(puzzle)):
        row = [puzzle[n][col] for n in range(len(puzzle)-1,-1,-1)]
        row = ''.join(row)
        ans.append(row)
    return ans

def add_hor_puzzle(puzzle1,puzzle2): #add piece 2 to existing piece 1
    if not puzzle1:
        return puzzle2
    else:
        ans = [puzzle1[row]+puzzle2[row] for row in range(len(puzzle2))]
        return ans

def add_vert_puzzle(puzzle1,puzzle2): # add piece 2 below piece 1
    if not puzzle1:
        return puzzle2
    else:
        ans = list(puzzle1)
        ans.extend(puzzle2)
        return ans

for puzzle in input:
    puzzle = puzzle.split('\n')
    id = re.search(id_expr, puzzle[0]).group(1)
    #regular format is clockwise, reverse is counterclockwise
    top = puzzle[1]
    b_rev = puzzle[-1]
    left_rev = [puzzle[n][0] for n in range(1,len(puzzle))]
    left_rev = ''.join(left_rev)
    right = [puzzle[n][-1] for n in range(1,len(puzzle))]
    right = ''.join(right)
    top_rev = top[::-1]
    bottom = b_rev[:: -1]
    left = left_rev[::-1]
    r_rev = right[::-1]
    puzzle_dict[id] = [(top,right,bottom,left),(top_rev,r_rev,b_rev,left_rev)]
    no_edges = [line[1:len(line)-1] for line in puzzle[2:len(puzzle)-1]] #skip line 0: contains piece ID, skip line 1: part of edge
    puzzle_dict[id].append(no_edges)
    tot_set.update([top,bottom,left,right,left_rev,r_rev,b_rev,top_rev])

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
            1: (1,0),
            2: (0,-1),
            3: (-1,0)}

flip_r_dict = {0:0,
               1:3,
               2:2,
               3:1}

#alternative way finding corners: x in (xmin,xmax) and y in (ymin,ymax)
#finding all edges x in (xmin,xmax) or y in (ymin,ymax)
puzzle_solution = {(0,0,corners[0]): [puzzle_dict[corners[0]][0],puzzle_dict[corners[0]][2]]}
x,y = 0,0
id = corners[0]
piece_check = deque([(x,y,id)])
solved_keys = [id]
while piece_check:
    x,y,id = piece_check[0]
    for orient,side in enumerate(puzzle_solution[(x,y,id)][0]): #orientation 0: top, 1: right, 2: bottom, 3: left
        for key in puzzle_dict.keys():
            if key not in solved_keys:
                # puzzle_dict[key] = [(t,r,b,l),(reverse),list(8)]
                for flip,side_set in enumerate(puzzle_dict[key][0:2]):
                    for orient2,side2 in enumerate(side_set):
                        if side == side2:
                            #print(f"Match {id}, side: {orient}, with {key} side {flip},{orient2}.")
                            xn = x + xy_delta[orient][0] #update x pos of piece with the delta
                            yn = y + xy_delta[orient][1]
                            puzzle_piece = puzzle_dict[key][2] #3rd element is the actual puzzle
                            if flip == 0: #match in non flipped edges -> flip
                                edge_list = puzzle_dict[key][1]
                                puzzle_piece = flip_right(puzzle_piece)
                                edge_list = (
                                edge_list[0], edge_list[3], edge_list[2], edge_list[1])  # flip elements 1 and 3
                                orient2 = flip_r_dict[orient2] #flip orientation:
                            elif flip == 1: #match in flipped edges, only rotation is needed
                                edge_list = puzzle_dict[key][0]
                            target = (orient + 2) % 4  # side 0 has to match 2, 2: 0, 1: 3 and 3:1
                            n_rot = ((target - orient2) + 4) % 4  # n_rot is diff between target and orient of matching edg
                            if flip == 0:
                                print(f"{key} has to be flipped and rotated {n_rot} times to match:{target}")
                            else:
                                print(f"{key} has to be rotated {n_rot} times to match:{target}")
                            for _ in range(n_rot):
                                puzzle_piece = rotate_right(puzzle_piece)
                                edge_list = (edge_list[3], edge_list[0], edge_list[1], edge_list[2]) #shift elements to right
                            #add solved puzzle with coord to solution
                            puzzle_solution[(xn, yn, key)] = [edge_list, puzzle_piece]
                            piece_check.append((xn,yn,key))
                            solved_keys.append(key)
    piece_check.popleft()

#puzzle solution has the relative orientation of puzzle pieces
coord_list = [(x,y) for x,y,id in puzzle_solution.keys()]
#go row by row puzzle pieces horizontaly to form a list of (3* 8) elements with length 8
x_list = [x for x,_ in coord_list]
y_list = [y for _,y in coord_list]
xmin = min(x_list)
xmax = max(x_list)
ymin = min(y_list)
ymax = max(y_list)

final_puzzle = []
for y in range(ymax,ymin-1,-1):
    hor_slice = []
    for x in range(xmin, xmax + 1):
        puzzle_id = [(xp,yp,id) for xp,yp,id in puzzle_solution.keys() if xp ==x and yp ==y][0]
        hor_slice = add_hor_puzzle(hor_slice,puzzle_solution[puzzle_id][1])
    final_puzzle = add_vert_puzzle(final_puzzle,hor_slice)

puzzle_width = len(final_puzzle[0])
gap = 1 + (puzzle_width - 20)
monster_len = 1+gap+20+gap+16
monster_char = 15 #15 # are part of each sea monster
sea_monster_expr = '#[.#]{'+str(gap)+'}#[.#]{4}##[.#]{4}##[.#]{4}###[.#]{'+str(gap)+'}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#'
#convert final puzzle in 8 orientations, check for each orientation the nr of sea monsters
final_flip = flip_right(final_puzzle)
final_list = [final_puzzle,
              rotate_right(final_puzzle),
              rotate_right(rotate_right(final_puzzle)),
              rotate_right(rotate_right(rotate_right(final_puzzle))),
              final_flip,
              rotate_right(final_flip),
              rotate_right(rotate_right(final_flip)),
              rotate_right(rotate_right(rotate_right(final_flip)))]
for puzzle in final_list:
    puzzle = ''.join(puzzle)
    n_monsters_rough = len(re.findall(sea_monster_expr, puzzle))
    if n_monsters_rough > 0:
        n_monsters_fine = 0
        for ind in range(0,len(puzzle)-monster_len):
            test = puzzle[ind:ind+monster_len]
            if len(re.findall(sea_monster_expr,test))>0:
                n_monsters_fine += 1
        roughness = puzzle.count('#') - (monster_char*n_monsters_fine)
        print(f"Part 2:Monsters:{n_monsters_fine}, roughness: {roughness}")

