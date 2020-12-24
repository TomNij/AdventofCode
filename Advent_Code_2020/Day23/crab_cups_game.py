# test input: 389125467 answer should be: 1+92658374 after 10 rounds, 1+ 67384529 after 100 = correct
#puzzle input: 614752839, too low 1+48795362, 1+37826459
input = list(map(int,list('389125467')))
nrounds = 100

minval = min(input)
maxval = max(input)
cc_ind = 0 #current cup index
cc = input[cc_ind]  # current cup
for ind in range(nrounds):
    if ind % 1000 == 0:
        print(f"Round: {ind}")
    min_pickup = (cc_ind + 1) % maxval
    max_pickup = (cc_ind + 4) % maxval
    if max_pickup < min_pickup: #pickup wraps around max value
        pick_up = input[min_pickup:]
        pick_up.extend(input[0:max_pickup])
    else:
        pick_up = input[min_pickup:max_pickup] #pickup next 3 cups
    if not pick_up:
        print(f'Error at step {ind}.')
    input = [val for val in input if val not in pick_up] #create input list without pickup values
    dest = (cc - 1) if (cc -1) != 0 else maxval
    while dest in pick_up:
        dest = (dest - 1) if (dest -1) != 0 else maxval
    dest_ind = [ind for ind,val in enumerate(input) if val == dest][0]
    pick_up = pick_up[::-1] #reverse pickup to ensure that the insertion goes well
    for val in pick_up:
        input.insert(dest_ind+1,val)
    cc_ind = ([ind for ind,val in enumerate(input) if val == cc][0] + 1) % len(input)
    cc = input[cc_ind]
input = list(map(str,input))
print(''.join(input))
