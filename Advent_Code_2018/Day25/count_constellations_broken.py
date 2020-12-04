import numpy as np
import os
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
constel_list = [set() for _ in range(n_planets)]
for ind in range(n_planets):
    planet = constellations[ind,:]
    planet_set = constellations
    dist_ind = manh_dist_4d(planet,planet_set)

    # check if planet in constellations
    planet_in_constel = False
    for list_ind in range(len(constel_list)):
        constel = constel_list[list_ind]
        if compare_lists(dist_ind,constel): #if there is overlap between 2 lists
            constel_list[list_ind].extend(dist_ind)
            planet_in_constel = True
    if not planet_in_constel:
        constel_list.append(dist_ind)
    # first planet
    if not constel_list:
        constel_list.append(dist_ind)

print(len(constel_list))