import numpy as np

f = open('input.txt','r')
input = f.readlines()
input = [line.strip() for line in input]
f.close()

n_rows = len(input) #vertical length is defined by the input
n_col = len(input[0])

def input_parser(line):
    arr = np.zeros((len(line)))
    for ind in range(len(line)):
        if line[ind] == '.':
            arr[ind] = -1
    return arr

def changeseating(old_config,new_config,x,y): #apply seating changing rules to a seat for Part 1
    check_ind = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
    occ_counter = 0
    for x_c,y_c in check_ind:
        if x_c in range(old_config.shape[0]) and y_c in range(old_config.shape[1]):
            if old_config[x_c,y_c] == 1:
                occ_counter += 1
    if new_config[x,y] == 0 and occ_counter == 0:
        new_config[x,y] = 1
    elif new_config[x,y] == 1 and occ_counter >= 4:
        new_config[x, y] = 0
    return new_config

def los_changeseating(old_config,new_config,x,y): #apply seating changing rules to a seat for Part 2
    check_vec = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    occ_counter = 0
    for dx,dy in check_vec:
        x_c = x
        y_c = y
        while x_c in range(old_config.shape[0]) and y_c in range(old_config.shape[1]):
            x_c += dx
            y_c += dy
            if x_c in range(old_config.shape[0]) and y_c in range(old_config.shape[1]):
                if old_config[x_c,y_c] != -1: #keep on looking unless there is no floor,error
                    if old_config[x_c,y_c] == 1:
                        occ_counter += 1
                    break
    if new_config[x,y] == 0 and occ_counter == 0:
        new_config[x,y] = 1
    elif new_config[x,y] == 1 and occ_counter >= 5:
        new_config[x, y] = 0
    return new_config


seating = np.zeros((n_rows,n_col)) #rows correspond to vertical dist, cols to hor dist
for ind,line in enumerate(input):
    seating[ind,:] = input_parser(line)

#first iteration: all seats get occupied
new_iteration = np.array(seating[:,:])
new_iteration[new_iteration == 0] = 1
#seating = np.dstack((seating,new_iteration))

round = 1
while True: #continue while there is a difference between rounds
    new_iteration = np.array(seating[:, :]) #initialize new iteration by equaling to old gen
    #old_iteration = seating[:, :]
    for x in range(n_rows):
        for y in range(n_col):
            new_iteration = los_changeseating(seating,new_iteration,x,y)
    if np.sum(new_iteration - seating) == 0:
        print(f"Seats occupied: {np.sum(new_iteration[new_iteration == 1])}")
        print(f"Round: {round}")
        break
    seating = np.array(new_iteration)
    round += 1