import numpy as np

with open('../Inputs/14.txt') as file:
    distance_list = file.readlines()
# Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
tot_time = 2503
end_dist = []
for line in distance_list:
    split_line = line.split(' ')
    name = split_line[0]
    speed = int(split_line[3])
    time = int(split_line[6])
    rest = int(split_line[-2])
    cycles = tot_time // (time + rest)
    leftover = tot_time % (time + rest)
    distance = cycles * speed * time
    if leftover >= time:
        distance += time * speed
    else:
        distance += leftover * speed
    end_dist.append(distance)

print(f"Part 1: {max(end_dist)}")

#Part 2 datastructure: 2503 * #reindeers, determine per row the max dist and the col index of max dist