with open('../Inputs/16.txt') as file:
    sue_input = file.readlines()

sue_match = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

sue_list = []
for sue_line in sue_input:
    sue_id_attr1,*attr_list = sue_line.strip().split(',')
    sue_id,attr0,val0 = sue_id_attr1.split(':')
    sue_entry = {sue_id : {attr0.strip():int(val0)}}
    for attr_item in attr_list:
        attr,value = attr_item.split(':')
        sue_entry[sue_id][attr.strip()] = int(value)
    sue_list.append(sue_entry)


for sue in sue_list:
    (name,sue_dict), = sue.items()
    true_sue = False
    for key,val in sue_dict.items():
        if key not in sue_match.keys():
            continue
        elif sue_dict[key] != sue_match[key]:
            true_sue = False  # this sue does not match our real sue
            break
        elif sue_dict[key] == sue_match[key]:
            true_sue = True #this sue does match our real sue
    if true_sue:
        print(f"Part 1: {name}")

for sue in sue_list:
    (name,sue_dict), = sue.items()
    true_sue = False
    for key,val in sue_dict.items():
        if key not in sue_match.keys():
            continue
        elif key in ['cats','trees']:
            if sue_dict[key] > sue_match[key]:
                true_sue = True #this sue does match our real sue
            else:
                true_sue = False  # this sue does not match our real sue
                break
        elif key in ['pomerians','goldfish']:
            if sue_dict[key] < sue_match[key]:
                true_sue = True #this sue does match our real sue
            else:
                true_sue = False  # this sue does not match our real sue
                break
        elif sue_dict[key] != sue_match[key]:
            true_sue = False  # this sue does not match our real sue
            break
        elif sue_dict[key] == sue_match[key]:
            true_sue = True #this sue does match our real sue
    if true_sue:
        print(f"Part 2: {name}") #305 is too low