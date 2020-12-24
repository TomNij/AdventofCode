import re
from collections import deque,Counter


#1 parse input
with open('../Input_files/21.txt') as file:
    input = file.read().split('\n')

#1 create dict per allergen with possible ingredients that can contain the allergen
food_dict = {}
ingr_counter = Counter()

allergen_expr = 'contains (.+)\)'
for line in input:
    ingr,allergens = line.split(' (') #split line on opening bracket
    allergens = re.search(allergen_expr,allergens).group(1).split(', ')
    ingr = ingr.split(' ')
    for item in ingr:
        ingr_counter[item] += 1
    for allergen in allergens:
        if allergen not in food_dict.keys():
            food_dict[allergen] = set(ingr)
        else: #allergen already known, create intersection of prev ingr and new ingredients
            food_dict[allergen] = food_dict[allergen].intersection(set(ingr))

ingr_allergen_set = set()
for allergen in food_dict.keys():
    ingr_allergen_set.update(food_dict[allergen])

ans = 0
for key in ingr_counter.keys():
    if key not in ingr_allergen_set:
        ans += ingr_counter[key]

print(f"Part 1: {ans}")

#generate list of tuple of ingredients that match allergens alphabetically:
solved = [] #(ingr,allergen)
while len(solved) < len(food_dict):
    for key in food_dict.keys():
        if len(food_dict[key]) == 1:
            solved_ingr = food_dict[key].pop()
            solved.append((solved_ingr,key))
            for allergen in food_dict.keys(): #remove solved ingr from other allergen_sets
                food_dict[allergen].discard(solved_ingr)

solved_alpha = sorted(solved,key = lambda x:x[1])
ans = [ingr for ingr,allergen in solved_alpha]
ans = ','.join(ans)
print(f"Part 2: {ans}")