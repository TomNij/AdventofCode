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
    if key not in bag_dict.keys():#bag without sub-bags
        return 1
    else:
        sub_dict = bag_dict[key]
        return 1 + sum([val * recursive_bag_dict_creator(bag_dict,new_key) for new_key,val in sub_dict.items()])



bag_dict = defaultdict()
parsed_bags = [parser(line) for line in input]
for bag,contents in parsed_bags:
    bag_dict = bag_dict_creator(bag_dict,bag,contents)


key = 'shiny gold'
ans = recursive_bag_dict_creator(bag_dict,key)

print(f"Shiny gold bag sum: {ans-1}")
