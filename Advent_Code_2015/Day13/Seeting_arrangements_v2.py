import re
import numpy as np
from collections import defaultdict
from itertools import permutations

with open('../Inputs/13.txt') as file:
    seat_preferences = file.readlines()

expr = '(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).'

person_dict = defaultdict(dict) #assign new persons an integer to enable matrix row/column assignments
pers_ind = 0

for pref in seat_preferences:
    pers1, sign, value,pers2 = re.search(expr,pref).groups()
    interaction = int(value) if sign == 'gain' else -1 * int(value)
    person_dict[pers1][pers2] = interaction

def find_max_happiness(m):
    maxhappiness = 0
    for ordering in permutations(person_dict.keys()):
        #shift persons in ordering by 1: Alice/Bob, Bob,Carol etc until George/Mallory
        happiness = sum(m[a][b]+m[b][a] for a, b in zip(ordering, ordering[1:]))
        #add missing ordering: Mallory,Alice Alice/Mallory
        happiness += m[ordering[0]][ordering[-1]] + m[ordering[-1]][ordering[0]]
        maxhappiness = max(maxhappiness, happiness)
    return maxhappiness

print(f"Part 1:{find_max_happiness(person_dict)}")

#add myself to the person_dict with values 0:
for key in list(person_dict.keys()):
    person_dict[key]['me'] = 0
    person_dict['me'][key] = 0

print(f"Part 2:{find_max_happiness(person_dict)}")