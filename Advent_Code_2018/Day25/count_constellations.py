import numpy as np
import os
from collections import deque
print(os.path.dirname(os.path.realpath(__file__)))

f = open("./test1.txt", "r")
input =  f.readlines()
f.close()
input = [line.split(',') for line in input]

constellations = np.array(input,dtype=int)

def manh_dist_4d(planet,planet_set):
    #return min dist of planet to constellation
    delta = abs(planet - planet_set)
    dist = np.sum(delta,axis=1)
    distlist = dist.tolist()
    distlist = [i for i, n in enumerate(distlist) if n <= 3] #get indices of values less/equal than 3
    return distlist

def compare_lists(list1,list2):
    match = False
    for val in list1:
        if val in list2:
           match = True
    return match




n_planets = constellations.shape[0]
indices = np.arange(n_planets)
constel_set= [set() for _ in range(n_planets)]
for ind in range(n_planets):
    planet = constellations[ind,:]
    planet_set = constellations
    dist_ind = manh_dist_4d(planet,planet_set)
    for num in dist_ind:
        constel_set[ind].add(num)

S = set()
ans = 0
for i in range(n_planets): #we loop over each planet, check its fellow constellations and with Q we add the 2nd order constellations
    if i in S:
        continue
    ans += 1
    Q = deque()
    Q.append(i)
    while Q:
        x = Q.popleft()
        if x in S:
            continue
        S.add(x)
        for y in constel_set[x]:
            Q.append(y)

print(ans)