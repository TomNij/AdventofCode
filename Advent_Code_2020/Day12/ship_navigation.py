f = open('../Input_files/12.txt')
lines = f.readlines()
lines = [line.strip() for line in lines]
input = [(line[0],int(line[1:])) for line in lines]
f.close()

direction_dict = {0: (0,1),
                  1: (1,0),
                  2: (0,-1),
                  3: (-1,0)} #0 maps to north, 1 to east, 2 south and 3 west

turn_dict = {'L': -1,
             'R': 1}

wind_dir_dict = {'N' : 0,
                 'E' : 1,
                 'S' : 2,
                 'W' : 3}

x = 0
y = 0
dir = 1
for action,val in input:
    if action in ('L','R'):
        turns = val/90
        dir = (dir + turn_dict[action]*turns) % 4 #add nr of 90 degree turns to dir and mod 4 to get value between 0 and 3
    elif action == 'F':
        x += val*direction_dict[dir][0]
        y += val*direction_dict[dir][1]
    else:
        x += val * direction_dict[wind_dir_dict[action]][0]
        y += val * direction_dict[wind_dir_dict[action]][1]

print(f"Part 1: {x},{y}, distance = {abs(x)+abs(y)}")

x = 0
y = 0
x_wp = 10
y_wp = 1
dx = x_wp - x
dy = y_wp - y
dir = 1
for action,val in input:
    if action in ('L','R'):
        turns = int(val/90)
        for _ in range(turns):
            dx_n = (turn_dict[action]) * dy
            dy_n = (-1 * turn_dict[action]) * dx
            dx = dx_n
            dy = dy_n
        x_wp = x + dx
        y_wp = y + dy
    elif action == 'F':
        x += val*dx
        y += val*dy
        x_wp = x + dx
        y_wp = y + dy
    else:
        x_wp += val * direction_dict[wind_dir_dict[action]][0]
        y_wp += val * direction_dict[wind_dir_dict[action]][1]
        dx = x_wp - x
        dy = y_wp - y

print(f"Part 2: {x},{y}, distance = {abs(x)+abs(y)}")