import re
import numpy as np
with open('../Inputs/13.txt') as file:
    seat_preferences = file.readlines()

def match_possible(seats_avail,pers1,pers2):
    if sum(seats_avail.values()) == 2*tot_pers:
        return True
    elif seats_avail[pers1] > 0 and seats_avail[pers2] > 0 and sum([val == 1 for val in seats_avail.values()]) >= 2:
        return True
    return False

expr = '(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).'

person_dict = {} #assign new persons an integer to enable matrix row/column assignments
pers_ind = 0

tot_pers = 8 #based on lenght input n*(n-1) = len input
pref_matrix = np.zeros((tot_pers,tot_pers),dtype=float)
for pref in seat_preferences:
    pers1, sign, value,pers2 = re.search(expr,pref).groups()
    if pers1 not in person_dict.keys():
        person_dict[pers1] = pers_ind
        pers_ind += 1
    if pers2 not in person_dict.keys():
        person_dict[pers2] = pers_ind
        pers_ind += 1
    interaction = int(value) if sign == 'gain' else -1 * int(value)
    pref_matrix[person_dict[pers1],person_dict[pers2]] = interaction

#convert pref_matrix in to lower matrix
pref_matrix_net = pref_matrix + np.transpose(pref_matrix)
pref_matrix_net = np.tril(pref_matrix_net)
#all values equal to zero have to be set to the min to not become part of the solution
pref_matrix_net[pref_matrix_net == 0] = np.min(pref_matrix_net)

seats_avail = {ind:2 for ind in range(tot_pers)}
happiness = 0
while sum(seats_avail.values()) > 0:
    ind = np.unravel_index(np.argmax(pref_matrix_net, axis=None), pref_matrix_net.shape) #get x,y of max value
    pers1, pers2 = ind
    # we cannot close the circle until we arrive at the last two seats, there should always be at least 2 persons that have an opening
    if match_possible(seats_avail,pers1,pers2):
        new_max = pref_matrix_net[ind]
        happiness += new_max
        seats_avail[pers1] -= 1
        seats_avail[pers2] -= 1
    else:
        print(f"Combination {pers1} and {pers2} no longer possible!")
    pref_matrix_net[ind] = -1 * np.inf

print(f'Part1: happiness: {happiness}')

#alternative approach: get dict of all relations and loop trough all permutations and return max happiness:
import re
from collections import defaultdict
from itertools import permutations

m = defaultdict(dict)
for line in input.split('\n'):
    x = re.match(r'(\S+) would (lose|gain) (\d+) happiness units by sitting next to (\S+)\.', line)
    p1, op, ch, p2 = x.group(1, 2, 3, 4)
    m[p1][p2] = -int(ch) if op == 'lose' else int(ch)

def find_max_happiness(m):
    maxhappiness = 0
    for ordering in permutations(m.keys()):
        happiness = sum(m[a][b]+m[b][a] for a, b in zip(ordering, ordering[1:]))
        happiness += m[ordering[0]][ordering[-1]] + m[ordering[-1]][ordering[0]]
        maxhappiness = max(maxhappiness, happiness)
    return maxhappiness

print(find_max_happiness(m))

for k in list(m.keys()):
    m['me'][k] = 0
    m[k]['me'] = 0

print(find_max_happiness(m))