from collections import Counter

with open('../Input_files/5.txt') as file:
    input = file.readlines()



input  = [line.split(' -> ') for line in input]
def parse(line):
    #list with 2 el
    x1,y1 = map(int,line[0].split(','))
    x2, y2 = map(int, line[1].split(','))
    return x1,y1,x2,y2

def solve(diag = False):
    vent_counter = Counter()
    for line in input:
        x1,y1,x2,y2 = parse(line)
        if not diag:
            if x1 == x2: #only straight lines
                #define range
                update_list = [(x1,y) for y in range(min(y1,y2),max(y1,y2)+1)]
            elif y1 == y2:
                update_list = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
            else:
                update_list = ()
        if diag:
            if x1 == x2: #only straight lines
                #define range
                update_list = [(x1,y) for y in range(min(y1,y2),max(y1,y2)+1)]
            elif y1 == y2:
                update_list = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
            elif abs(y2-y1) == abs(x2-x1): #diagonal lines
                #9,7 to 7,9 is 9,7, 8,8, 7,9 x goes from x1 to x2, y goes from y1 to y2
                #need to know if x1 > x2 and y1 > y2?
                dx = -1 if x2 < x1 else 1
                dy = -1 if y2 < y1 else 1
                update_list = [(x,y) for x,y in zip(range(x1,x2+dx,dx),range(y1,y2+dy,dy))]
            else:
                update_list = ()
        vent_counter.update(update_list)
    double_coord = [k for k, v in vent_counter.items() if v > 1]
    return len(double_coord)

if __name__ == '__main__':
    pt1 = solve()
    print(f"Part 1: {pt1}")
    pt2 = solve(diag=True)
    print(f"Part 2: {pt2}")