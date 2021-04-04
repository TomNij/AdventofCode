from collections import defaultdict

with open('../Inputs/3.txt') as file:
    input = file.read().strip()

direction_dict = {
    '^' : (0,1),
    'v' : (0,-1),
    '>' : (1,0),
    '<' : (-1,0)
}

adress_counter = defaultdict(lambda: 0)
#start at home adress
adress_counter[(0,0)] += 1
x,y = 0,0
for char in input:
    dx,dy = direction_dict[char]
    x = x +dx
    y = y + dy
    adress_counter[(x,y)] += 1

adr_w_gift = [key for key in adress_counter.keys() if adress_counter[key] > 0]
print(f"Part 1: {len(adr_w_gift)}")

adress_counter = defaultdict(lambda: 0)
adress_counter[(0,0)] += 2 #2gifts at the starting house
x1,x2,y1,y2 = 0,0,0,0
for ind,char in enumerate(input):
    dx,dy = direction_dict[char]
    if ind % 2 == 0:
        x1 = x1 + dx
        y1 = y1 + dy
        adress_counter[(x1,y1)] += 1
    else:
        x2 = x2 + dx
        y2 = y2 + dy
        adress_counter[(x2, y2)] += 1

adr_w_gift = [key for key in adress_counter.keys() if adress_counter[key] > 0]
print(f"Part 2: {len(adr_w_gift)}")