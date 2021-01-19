import anytree

with open('../Input_files/19.txt') as file:
    lines = file.read().split('\n\n')

rules = lines[0].split('\n')
codes = lines[1].split('\n')

def create_rule_set(rule_list): #replace rulenr with 'a' or 'b' and check if all nrs are replaced
    pass

def list_combo(l1,l2):
    output = []
    if not l1:
        return l2
    for item1 in l1:
        for item2 in l2:
            output.append(item1 +item2) #item1 and item2 should be list of strings that can be appended
    return output

rule_dict = {rule.split((':'))[0]: rule.split((':'))[1].strip() for rule in rules
}

def code_solved(code_list,rule_dict): #return nr of items in list where the output == a or b
    solve_count = 0
    #solved_rules = [key for key,item in rule_dict.items() if item in ('a','b')]
    #solved_rules.extend(['a','b']) #a's and b's are solved of course
    solved_rules = ['a','b']
    for code in code_list: #code list is a list with in itself codes [['3','4'],
        code_solved = len([c for c in code if c in solved_rules])
        if code_solved == len(code):
            solve_count += 1
    return solve_count

code_list = [rule_dict['0'].split(' ')]
solved_rules = [key for key,item in rule_dict.items() if item in ('a','b')]
solve_count = code_solved(code_list,rule_dict)

while solve_count < len(code_list):
    new_list = []
    for ind,code in enumerate(code_list): #each code becomes a list of sub_codes so code_list is a double list [[l1],[l2],[l3]]
        new_code = []
        for sub_code in code:
            if sub_code in ('a','b'):
                sub_rules = [[sub_code]]
            else:
                sub_rules = rule_dict[sub_code]
                sub_rules = sub_rules.split(' | ')
                sub_rules = [rule.split(' ') for rule in sub_rules] # [['4','4'],['5','5']] or [['4', '4']] or [['a']] if no pipe
            #operation needed that combines the output of sub_rules with the code_list so far
            #split operations for  [['4','4'],['5','5']] and ['4', '4']
            if not new_code:
                new_code = sub_rules
            else:
                if len(sub_rules) == 1:
                    _ = [code.extend(sub_rules[0]) for code in new_code]
                else: #[['4','4'],['5','5']]
                    new_code = list_combo(new_code,sub_rules)
        new_list.extend(new_code)
    code_list = new_list
    solve_count = code_solved(code_list, rule_dict)
    print(len(code_list))

code_options = [''.join(code) for code in code_list]
solved_count = 0
for code in codes:
    if code in code_options:
        solved_count += 1

print(solved_count)