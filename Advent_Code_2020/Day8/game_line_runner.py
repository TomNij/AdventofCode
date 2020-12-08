import re
from collections import defaultdict,deque

f = open('input.txt','r')
input = f.readlines()
input = [line.strip().replace('+','') for line in input] #remove + to make number easier
f.close()

lines_excecuted = []
line = 0
acc_count = 0
expr = '(\w+) (-?\d+)'
input = [(re.search(expr,line).groups()) for line in input]


for ind,input_line in enumerate(input):
    operation,value = input_line
    
    if operation == 'nop':
        new_operation = 'jmp'
    elif operation == 'jmp':
        new_operation = 'nop'

    if operation != 'acc': #only test changing the nopand jmp operator
        test_input = input[:]
        test_input[ind] = (new_operation,value)
        line = 0
        acc_count = 0
        lines_excecuted = []
        while line not in lines_excecuted:
            operation, value = test_input[line]
            value = int(value)
            lines_excecuted.append(line)
            if operation == 'nop':
                line += 1
            elif operation == 'acc':
                acc_count += value
                line += 1
            elif operation == 'jmp':
                line += value
            if line == len(test_input):
                print(f"Acc value: {acc_count}")
                break

