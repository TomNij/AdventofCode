from operator import add
from collections import defaultdict
from copy import copy
#1 parse input
with open('../Input_files/24.txt') as file:
    input = file.read().split('\n')

#add delta to reference
ref = (0,0,0)
delta_dict = {
    'nw': (-1, 1),
    'ne': (1, 1),
    'sw': (-1,-1),
    'se': (1,-1),
    'e': (2, 0),
    'w': (-2, 0)
}
#Example: order does not matter, opposing directions can be eliminated
#nw w sw e e = nw sw e
tile_dict = defaultdict(lambda : 1) #create defaultdict with values 1
for line in input:
    position = (0,0)
    line_ind = 0
    while line_ind <len(line):
        if line[line_ind] in delta_dict.keys():
            char = line[line_ind]
            delta = delta_dict[char]
            position = tuple(map(add, position, delta))
            line_ind += 1
        else: #char not in deltadict_keys
            char = line[line_ind:line_ind+2] #add right char
            delta = delta_dict[char]
            position = tuple(map(add, position, delta))
            line_ind += 2
    tile_dict[position] *= -1 #flip the tile found

black_count  = sum([val == -1 for val in tile_dict.values()])
print(f"Part 1: {black_count}")

start = tile_dict
end = copy(start) # tile_dict that is edited by the flips during the day
for day in range(1,101): #first day is day 1, range until 101
    #comparisons are done on start, changes are made in end
    for key in list(start.keys()): #all black tiles and black tiles that have been flipped twice
        value = start[key]
        neighbors = [tuple(map(add, key, delta)) for delta in delta_dict.values()]
        if value == -1: #we are on a black tile
            black_tiles = sum([start[neighbor] == -1 for neighbor in neighbors])
            if black_tiles == 0 or black_tiles > 2:
                end[key] = 1 #turn current tile white
            #for black tiles check if a white neighbor that has not been flipped yet has 2 black neighbours
            for neighbor in neighbors:
                if start[neighbor] == 1:
                    #neighbours of neighboring white tile
                    w_neighbors = [tuple(map(add, neighbor, delta)) for delta in delta_dict.values()]
                    black_tiles = sum([start[w_neighbor] == -1 for w_neighbor in w_neighbors])
                    if black_tiles == 2:
                        end[neighbor] = -1 #add neighbor to dict with a black value
        elif value == 1:
            black_tiles = sum([start[neighbor] == -1 for neighbor in neighbors])
            if black_tiles == 2:
                end[key] = -1
    start = copy(end)
    print(f"Day:{day}, #black tiles {sum([val == -1 for val in start.values()])}")

pt2_black_val  = sum([val == -1 for val in start.values()])
print(f"Part 2: {pt2_black_val}")