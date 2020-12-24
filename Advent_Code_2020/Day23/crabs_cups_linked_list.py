# test input: 389125467 answer should be: 1+92658374 after 10 rounds, 1+ 67384529 after 100 = correct
#puzzle input: 614752839, too low 1+48795362, 1+37826459
input = list(map(int,list('614752839')))
input.extend([n for n in range(10,1000000+1)])
#nrounds = 100
nrounds = int(1e7) #ten million
cup_dict = {input[n]: input[(n+1) % len(input)] for n in range(len(input))}

cc = input[0]
for round in range(nrounds):
    if round % int(1e5) == 0:
        print(round)
    right1 = cup_dict[cc]
    right2 = cup_dict[right1]
    right3 = cup_dict[right2]
    cup_dict[cc] = cup_dict[right3]   #let current cup link to the value right of right3: closing the circle again
    pickup = [cc,right1,right2,right3]
    #dict keys are the labels
    dest = cc
    while dest in pickup:
        dest -= 1
        if dest == 0:
            dest = max(input) #wrap around to highest label on any cup
    insert_before = cup_dict[dest]
    cup_dict[dest] = right1
    cup_dict[right1] = right2
    cup_dict[right2] = right3
    cup_dict[right3] = insert_before
    cc = cup_dict[cc]

print(f"{cup_dict[1]},{cup_dict[cup_dict[1]]}: ans: {cup_dict[1]*cup_dict[cup_dict[1]]}")