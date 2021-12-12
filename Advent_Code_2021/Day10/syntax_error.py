from collections import Counter

with open('../Input_files/10.txt') as file:
    input = file.readlines()

error_val_dict = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

complete_val_dict = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}

closed_open_check = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}

syntax_error_score = 0
completion_score = []
for line in input:
    bracket_stack = []
    stop_line = False
    for char in line.strip():
        #closing char
        if char in closed_open_check.keys():
            if bracket_stack[-1] == closed_open_check[char]:
                bracket_stack.pop(-1)
            else: #closed char does not match opening char: syntax error
                syntax_error_score += error_val_dict[char]
                stop_line = True
                break
        else: #opening char
            bracket_stack.append(char)
        if stop_line:
            break
    if not stop_line:
        line_completion = 0
        for char in reversed(bracket_stack):
            line_completion *= 5
            line_completion += complete_val_dict[char]
        completion_score.append(line_completion)

print(f"Part 1: {syntax_error_score}")
#get middle completion score
middle_ind = len(completion_score)//2
print(f"Part 2: {sorted(completion_score)[middle_ind]}")