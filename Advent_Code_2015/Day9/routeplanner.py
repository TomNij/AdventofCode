from collections import defaultdict
from itertools import permutations
import numpy as np

with open('../Inputs/9.txt') as file:
    distance_list = file.readlines()

city_dict = defaultdict(dict)
city_list = []
for line in distance_list:
    city1,_1,city2,_2,distance = line.split(' ')
    city_dict[city1][city2] = int(distance)
    if city1 not in city_list:
        city_list.append(city1)
    if city2 not in city_list:
        city_list.append(city2)

dist_arr = []
for route in permutations(city_list): #initially missing Abre since it is not in the primary level of keys
    route_dist = 0
    for city1, city2 in zip(route, route[1:]):
        try:
            route_dist += city_dict[city1][city2]
        except KeyError: #if distance not in city_dict then it could be in the other order
            route_dist += city_dict[city2][city1]
    dist_arr.append(route_dist)

print(f"Part 1: {min(dist_arr)}")
print(f"Part 2: {max(dist_arr)}")