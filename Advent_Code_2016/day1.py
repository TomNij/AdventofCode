import numpy as np

with open('1.txt') as file:
    input = file.read()
input = input.split(',')
input = [line.strip() for line in input]

# input = ['R5', 'L5', 'R5', 'R3']

dir = np.array([0,1]) #North

#N,E,S,W
dir_arr = [(0,1),(1,0),(0,-1),(-1,0)]
dir_ind = 0
x = y = 0
loc_list = []
double_loc = False
#instead loop through 4 directions in a list.
def update_dir(input,dir):
    theta = np.pi/2 if input == 'L' else -1*np.pi/2
    rot_mat = np.array([[np.cos(theta),-1*np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    dir = np.dot(rot_mat,dir)
    return dir

for i in input:
    input = i[0]
    steps = int(i[1:])
    # dir = update_dir(input,dir)
    dir_ind = (dir_ind + 1) % 4 if input == 'R' else (dir_ind - 1) % 4
    # pos = (pos[0] + dir[0]*steps,pos[1] + dir[1]*steps)
    dir = dir_arr[dir_ind]
    x = x + steps * dir[0]
    y = y + steps * dir[1]
print(abs(x) + abs(y))