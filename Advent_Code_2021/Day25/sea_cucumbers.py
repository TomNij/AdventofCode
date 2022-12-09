with open('../Input_files/25.txt') as file:
    input = file.readlines()

input= [line.strip() for line in input]

sea_dict = {(row,col):char for row,line in enumerate(input) for col,char in enumerate(line) if char in 'v>'}
max_col = len(input[0])
max_row = len(input)

def print_sea_dict(sea_dict):
    grid = ['.' * max_col for _ in range(max_row)]
    for key,char in sea_dict.items():
        row,col = key
        grid[row] = grid[row][0:col] + char + grid[row][col+1:]
    return grid

steps = 1
while True:
    move_count = 0
    hor_cucumbers = {coord:val for coord,val in sea_dict.items() if val == '>'}
    moves = []
    for coord,val in hor_cucumbers.items():
        row,col = coord
        new_coord = (row,(col + 1) % max_col)
        if new_coord not in sea_dict.keys():
            moves.append((coord,new_coord))
            move_count += 1
    for move in moves:
        old,new = move
        sea_dict[new] = sea_dict.pop(old)


    vert_cucumbers = {coord: val for coord, val in sea_dict.items() if val == 'v'}
    moves = []
    for coord,val in vert_cucumbers.items():

        row,col = coord
        new_coord = ((row+1) % max_row,col)
        if new_coord not in sea_dict.keys():
            moves.append((coord,new_coord))
            move_count += 1
    for move in moves:
        old,new = move
        sea_dict[new] = sea_dict.pop(old)
    #reorder seadict
    # sea_dict_keys = sorted(sea_dict.keys(),key= lambda t: (t[0], t[1]))
    # sea_dict = {key:sea_dict[key] for key in sea_dict_keys}
    if move_count == 0:
        print(steps)
        break
    else:
        steps += 1

