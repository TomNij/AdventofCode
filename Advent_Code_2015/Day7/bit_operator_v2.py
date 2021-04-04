import re
with open('../Inputs/7.txt') as file:
    input = file.readlines()

input = [line.strip().split(' -> ') for line in input]
operator_dict = {
    'AND' : ' &',
    'OR' : '|',
    'LSHIFT' : '<<',
    'RSHIFT' : '>>',
    'NOT' : '~'
}
def can_process(lhs,result_dict):
    el_list = lhs.split(' ')
    for el in el_list:
        try:
            int(el)
        except ValueError: #el is not an integer
            if not (el in result_dict.keys() or el in operator_dict.keys()):
                return False
    return True


def process_input(result_dict):

    ind = 0
    while len(result_dict.keys()) < len(input):
        lhs,rhs = input[ind]
        if rhs in result_dict:
            ind = (ind + 1) % len(input)
            continue
        #check if lhs contains elements that are not numbers or operators or not already in result_dict
        if can_process(lhs,result_dict):
            if len(lhs.split(' ')) == 3:
                val1, operator, val2 = lhs.split(' ')
                if val1 in result_dict.keys():
                    val1 = result_dict[val1]
                if val2 in result_dict.keys():
                    val2 = result_dict[val2]
                result_dict[rhs] = str(eval(val1 + operator_dict[operator] + val2))
            elif len(lhs.split(' ')) == 2: #NOT case
                operator, val2 = lhs.split(' ')
                if operator == 'NOT':
                    if val2 in result_dict.keys():
                        val2 = result_dict[val2]
                    interm = str(eval(operator_dict[operator] + val2))
                    result_dict[rhs] = str(eval(interm + '& 65535')) #correct signed int to 16bit unsigned int
                else:
                    print(f" {lhs} --> {rhs}, not taken care off")
            else:
                val1 = lhs
                if val1 in result_dict.keys():
                    val1 = result_dict[val1]
                result_dict[rhs] = str(eval(val1))
        ind = (ind + 1) % len(input)
    return result_dict

result_dict = process_input({})
print(f"Part 1: {result_dict['a']}")
b_override = result_dict['a']
result_dict = process_input({'b': str(b_override)})
print(f"Part 2: {result_dict['a']}")