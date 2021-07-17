import numpy as np
from collections import Counter
with open('../Inputs/14.txt') as file:
    distance_list = file.readlines()
# Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
tot_time = 2503
n_reindeer = len(distance_list)
dist_arr = np.zeros((tot_time,n_reindeer),dtype=float)

def is_moving(t,time,rest):
    if t % (time + rest) < time: #if the current time in the cycle is less than time, we are moving.
        return True
    else:
        return False

for reindeer,line in enumerate(distance_list):
    distance = 0
    split_line = line.split(' ')
    name = split_line[0]
    speed = int(split_line[3])
    time = int(split_line[6])
    rest = int(split_line[-2])
    for t_ind,t in enumerate(range(tot_time)):
        if is_moving(t,time,rest):
            distance += speed * 1 #time goes with steps of 1
        dist_arr[t_ind,reindeer] = distance


print(f"Part 1: {np.max(dist_arr)}")
#Part 2 datastructure: 2503 * #reindeers, determine per row the max dist and the col index of max dist
t_max = np.max(dist_arr,1)
winner_counter = Counter()
for t_ind,t in enumerate(range(tot_time)):
    winner = np.argwhere(dist_arr[t_ind,:] == t_max[t_ind])
    winner_counter.update(winner.flatten().tolist())

print(f"Part 2: {max(winner_counter.values())}")
