import re
import itertools
import numpy as np
import time

start = time.perf_counter()
f = open('../Input_files/16.txt')
lines = f.read().split('\n\n')
f.close()

#departure location: 32-69 or 86-968
expr = ' (\d+)-(\d+) or (\d+)-(\d+)'
attr_ranges = lines[0].split('\n')
attr_dict = {}
pt1_check_set = set()
for line in attr_ranges:
    attr,attr_range = line.split(':')
    x0,x1,x2,x3 = list(map(int,re.search(expr,attr_range).groups()))
    attr_dict[attr] = [set(itertools.chain(range(x0,x1+1),range(x2,x3+1)))] #add list of 2 ranges
    for val in itertools.chain(range(x0,x1+1),range(x2,x3+1)):
        pt1_check_set.add(val)

#other tickets
other_tickets = lines[2].split('\n')
inval_count = 0
inval_ticket = []
for ind,ticket in enumerate(other_tickets):
    if ticket[0:6] != 'nearby':
        check_vals = list(map(int,ticket.split(',')))
        for val in check_vals:
            if val not in pt1_check_set:
                inval_count += val
                inval_ticket.append(ind)


print(f"Part 1: {inval_count}")

valid_tickets = [ticket for ind,ticket in enumerate(other_tickets) if ind not in inval_ticket and ticket != 'nearby tickets:']
n_attr = valid_tickets[0].count(',')+1
n_ticket= len(valid_tickets)
ticket_arr = np.zeros((n_ticket,n_attr))

for ind,ticket in enumerate(valid_tickets):
    ticket_val = list(map(int, ticket.split(',')))
    ticket_arr[ind,:] = ticket_val

#determine for each position of the valid tickets to which key it belongs
for col in range(np.shape(ticket_arr)[1]):
    check_vals = ticket_arr[:,col]
    for key in attr_dict.keys():
        check_set = attr_dict[key][0]
        output = [val for val in check_vals if val in check_set]
        if len(output) == len(check_vals): #all checkvals were valid
            attr_dict[key].append(col)

pt2_prod = 1
my_ticket = lines[1].split('\n')
my_ticket = my_ticket[1].split(',')
key_list = [(key,len(attr_dict[key])-1) for key in attr_dict.keys()]
key_list = sorted(key_list,key= lambda x:x[1])

for key,ind in key_list:
    if ind == 1:
        attr_num = attr_dict[key][1]
    else:
        prev_key = key_list[ind-2][0]
        options = attr_dict[key][1:]
        attr_list = [option for option in options if option not in attr_dict[prev_key][1:]]
    if key[0:9] == 'departure':
        attr_num = attr_list[0]
        pt2_prod *= int(my_ticket[attr_num])

print(f"Part 2: {pt2_prod}")
end = time.perf_counter()
print(f"Time taken: {end-start}s")