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

result_dict = {}
ind = 0
ind_processed = []
while len(result_dict.keys()) < len(input):
    if 'a' in result_dict.keys():
        print(f"Part 1: {result_dict['a']}")
        break
    elif ind in ind_processed:
        continue

    lhs,rhs = input[ind]
    if len(lhs.split(' ')) == 3:
        val1, operator, val2 = lhs.split(' ')
        if val1 not in result_dict.keys():
            ind = (ind + 1) % len(input)
            continue

        if val2 in result_dict.keys():
            result_dict[rhs] = eval(str(result_dict[val1]) +
                                    operator_dict[operator] +
                                    str(result_dict[val2]))
        else:
            #x lshift 2
            try:
                result_dict[rhs] = eval(str(result_dict[val1]) +
                                    operator_dict[operator] +
                                    val2)
            except(NameError):
                ind = (ind + 1) % len(input)
                continue
    elif len(lhs.split(' ')) == 2:
        operator, val2 = lhs.split(' ')
        if val2 not in result_dict.keys():
            ind = (ind + 1) % len(input)
            continue
        result_dict[rhs] = eval(operator_dict[operator] +
                                str(result_dict[val2]))
    else:
        try:
            result_dict[rhs] = eval(lhs)
        except(NameError):
            try:
                result_dict[rhs] = eval(str(result_dict[lhs]))
            except(KeyError):
                ind = (ind + 1) % len(input)
                continue
    ind = (ind + 1) % len(input)

a =1