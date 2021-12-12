with open('../Input_files/2.txt') as file:
    input = file.readlines()

def input_parser1(line):
    dir,num = line.split(' ')
    if dir == 'forward':
        dx = int(num)
        dy = 0
    elif dir == 'up':
        dx = 0
        dy = -1*int(num)
    else: #down
        dx = 0
        dy = int(num)
    return dx,dy

def input_parser2(line,aim):
    dir,num = line.split(' ')
    if dir == 'forward':
        dx = int(num)
        dy = aim*int(num)
        da = 0
    elif dir == 'up':
        dx = 0
        dy = 0
        da = -1 * int(num)
    else: #down
        dx = 0
        dy = 0
        da = int(num)
    return dx,dy,da

(x1,x2) = 0,0
(y1,y2) = 0,0
aim = 0
#pt1
for line in input:
    dx,dy = input_parser1(line)
    x1 += dx
    y1 += dy
    dx,dy,da = input_parser2(line,aim)
    x2 += dx
    y2 += dy
    aim += da

print(f"Part 1:{x1*y1}")
print(f"Part 2:{x2*y2}")
