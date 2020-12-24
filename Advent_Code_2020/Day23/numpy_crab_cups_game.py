# test input: 389125467 answer should be: 1+92658374 after 10 rounds, 1+ 67384529 after 100 = correct
import numpy as np
import itertools

input = list(map(int,list('389125467')))

input.extend([n for n in range(10,1000000+1)])
nrounds = 10000000 #10.0000.000 10 million moves
#convert to numpy array
input = np.array(input,dtype=int)
minval = min(input)
maxval = max(input)
cc_ind = 0 #current cup index
cc = input[cc_ind]  # current cup
prev_sums = []
ind = 0
input_sum = sum([ind*val for ind,val in enumerate(input)])
while input_sum not in prev_sums: #does not work to find looping
    prev_sums.append(input_sum)
    ind += 0
    if ind % 1000 == 0:
        print(f"Round: {ind}")
    min_pickup = (cc_ind + 1) % maxval
    max_pickup = (cc_ind + 4) % maxval
    if max_pickup < min_pickup: #pickup wraps around max value
        pick_up = input[min_pickup:]
        pick_up = np.hstack((pick_up,input[0:max_pickup]))
        ind_list = list(range(min_pickup,len(input)))
        ind_list.extend(list(range(0,max_pickup)))
        input = np.delete(input,ind_list)
    else:
        pick_up = input[min_pickup:max_pickup] #pickup next 3 cups
        input = np.delete(input, list(range(min_pickup,max_pickup)))
    if not pick_up.any():
        print(f'Error at step {ind}.')
    #input = [val for val in input if val not in pick_up] #create input list without pickup values
    dest = (cc - 1) if (cc -1) != 0 else maxval
    while dest in pick_up:
        dest = (dest - 1) if (dest -1) != 0 else maxval
    dest_ind = np.where(input == dest)[0]
    input = np.insert(input,dest_ind+1,pick_up)
    cc_ind = np.where(input == cc)[0]
    cc_ind = (int(cc_ind) + 1) % len(input)
    cc = input[cc_ind]
    input_sum = sum([ind*val for ind,val in enumerate(input)])

#
print(f"Loop after {ind} rounds.")
one_ind = np.where(input == 1)[0]

print(f"{input[one_ind + 1] *input[one_ind + 2]}")