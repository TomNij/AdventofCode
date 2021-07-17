with open('../Inputs/12.txt') as file:
    input = file.readlines()

def list_eval(list_obj): #if a nested listobject is encountered this function should return the sum of entries in the list
    sum_out = 0
    for item in list_obj:
        if type(item) is list:
            sum_out += list_eval(item)
        elif type(item) is dict:
            sum_out += dict_eval(item)
        else:
            try:
                sum_out += int(item)
            except ValueError:
                continue
    return sum_out

def dict_eval(dict_obj): #if a nested dict object is encountered this function should return the sum of entries in the dict
    sum_out = 0
    if pt1 or 'red' not in dict_obj.keys() and 'red' not in dict_obj.values(): #ignore red check in pt1
        for item in dict_obj.values():
            if type(item) is list:
                sum_out += list_eval(item)
            elif type(item) is dict:
                sum_out += dict_eval(item)
            else:
                try:
                    sum_out += int(item)
                except ValueError:
                    continue
    return sum_out


input = eval(input[0])

output = 0
pt1 = True
if type(input) is list:
    output += list_eval(input)
elif type(input) is dict:
    output += dict_eval(input)

print(f"Part 1: {output}")

output = 0
pt1 = False
if type(input) is list:
    output += list_eval(input)
elif type(input) is dict:
    output += dict_eval(input)

print(f"Part 2: {output}")