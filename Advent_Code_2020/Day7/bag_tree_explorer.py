import re
from collections import defaultdict,deque

f = open('input.txt','r')
input = f.readlines()
input = [line.strip().replace('.','') for line in input] #remove dots at end of sentence
f.close()

def parser(line):
    expr = '^(\w+ \w+) bags contain (.+)'
    bag, contents = re.search(expr,line).groups()
    return [bag,contents]

def bag_dict_creator(bag_dict,bag,contents):
    if contents == 'no other bags':
        return bag_dict
    contents = contents.split(',')
    content_dict = defaultdict()
    for sub_bag in contents:
        elements = sub_bag.strip().split(' ') #first remove leading/trailing spaces before splitting
        key = elements[1] +' '+ elements[2]
        val = int(elements[0])
        content_dict[key] = val
    bag_dict[bag] = content_dict
    return bag_dict

def recursive_bag_dict_creator(bag_dict,key):
    try:
        check_keys = deque(bag_dict[key].keys())
    except(AttributeError):
        check_keys = []
    while check_keys:
        sub_key = check_keys[0]
        try:
            multiplier = bag_dict[key][sub_key]
            #rint(f"Multiplier: {multiplier}")
            #bag_dict[sub_key].update((x, y * multiplier) for x, y in bag_dict[sub_key].items())
            bag_dict[key].update(bag_dict[sub_key]) #add subkeys to initial dict
            check_keys.extend(bag_dict[sub_key].keys())  # append new found keys to list to check per bag
        except(KeyError): #key not found
            pass
        except(ValueError):
            print(f"Key: {key},subkey {sub_key}")
            print(f"Subkey dict: {bag_dict[sub_key]}")
        check_keys.popleft()
    return bag_dict

def update_dict(dict,key):
    sub_dict = dict[key]
    for sub_key in sub_dict.keys():
        dict[key][sub_key] += dict[key][sub_key] * sub_dict

bag_dict = defaultdict()
parsed_bags = [parser(line) for line in input]
for bag,contents in parsed_bags:
    bag_dict = bag_dict_creator(bag_dict,bag,contents)

original_dict = dict(bag_dict)
gold_counter = 0
for key in bag_dict.keys():
    #bag_dict = recursive_bag_dict_creator(bag_dict,key)
    if 'shiny gold' in bag_dict[key].keys():
        gold_counter += 1

print(f"Part 1 Gold bag counter: {gold_counter}")

bag_counter = 0
key = 'shiny gold'
check_keys = deque(original_dict['shiny gold'].keys())
checked_keys = deque()
while check_keys:
    sub_key = check_keys[0]
    #bag_counter += original_dict['shiny gold'][key]
    try:
        print(f"{key}, {sub_key}")
        print(f"Multiplier: {original_dict[key][sub_key]}")
        print(f"Keys to check: {check_keys}")
        multiplier = original_dict[key][sub_key]
        new_keys = original_dict[sub_key].keys()
        for new_key in new_keys:
            if new_key not in checked_keys:
                original_dict[key][new_key] = multiplier * original_dict[sub_key][new_key]
            else:
                original_dict[key][new_key] += (multiplier)
                print(f"updated bag value: {key},{sub_key},{new_key} = {original_dict[key][new_key]}, added: {(multiplier)}")
            try:
                if new_key not in checked_keys:
                    check_keys.append(new_key)
            except(KeyError):  # key not found
                pass
        checked_keys.extend(new_keys)

    except(KeyError):  # key not found
        pass
    check_keys.popleft()

print(f"Shiny gold bag sum: {sum(original_dict['shiny gold'].values())}")
