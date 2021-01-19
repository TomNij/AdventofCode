import re
import math

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


def code_solved(code_list,solved_rules): #return nr of items in list where the output == a or b
    solve_count = 0
    for code in code_list: #code list is a list with in itself codes [['3','4'],
        code_solved = len([c for c in code if c in solved_rules])
        if code_solved == len(code):
            solve_count += 1
    return solve_count

code_list = [rule_dict['0'].split(' ')]
solved_rules = ['a','b','8','11'] #8 and 11 can be considered solved because we will solve them manually
#solved_rules_2 = [key for key,item in rule_dict.items() if item in ('a','b')]
solved_dict = {}
for solve_rule in ['42','31']:
    print(f"Solve rule nr: {solve_rule}")
    code_list = [r.split(' ') for r in rule_dict[solve_rule].split(' | ')]
    solve_count = code_solved(code_list, solved_rules)
    while solve_count < len(code_list):
        new_list = []
        for ind,code in enumerate(code_list): #each code becomes a list of sub_codes so code_list is a double list [[l1],[l2],[l3]]
            new_code = []
            for sub_code in code:
                if sub_code in ['a','b','8','11']:
                    sub_rules = [[sub_code]]
                else:
                    sub_rules = rule_dict[sub_code]
                    sub_rules = sub_rules.split(' | ')
                    sub_rules = [rule.strip().split(' ') for rule in sub_rules] # [['4','4'],['5','5']] or [['4', '4']] or [['a']] if no pipe
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
        solve_count = code_solved(code_list, solved_rules)
        print(f"Nr codes:{len(code_list)}, nr solved: {solve_count}")
    solved_dict[solve_rule] = [''.join(code) for code in code_list]
#create patterns that match 42 and 31
pattern_42 = '('
for pattern in solved_dict['42']:
    pattern_42 += pattern + '|'
pattern_42 = pattern_42[0:-1]+')'
pattern_31 = '('
for pattern in solved_dict['31']:
    pattern_31 += pattern + '|'
pattern_31 = pattern_31[0:-1] + ')'

solved_count = 0
for code in codes: # 0 means 8 11, with new rules means n times 42 AND m times 42  AND m times 31: 42 42 31 of 42 42 42 31
    #check if code matches n times 42 strings or n times 42 plus 31
    n_sets = int(len(code) / 8)  # for code die uit 5 sets bestaat kan het zijn 42 42 42 42 31 of 42 42 42 31 31
    if len(code) % 8 != 0 or n_sets <= 2:
        print(f"Code: {code}, len: {len(code)}")
        continue
    n_sets = int(len(code) / 8) #for code die uit 5 sets bestaat kan het zijn 42 42 42 42 31 of 42 42 42 31 31
   # 5 sets = 4 * 42 + 31, 3* 42 + 2 * 31
    #n sets = n -1 * 42 + 31 tot math.ceil(n/2) + 1 * 42 + math.floor(n/2) - 1 * 31
    if n_sets % 2 == 0:
        min_n_42 = int(n_sets / 2) + 1
        max_n_31 = int(n_sets / 2) - 1
    else:
        min_n_42 = math.ceil(n_sets / 2)
        max_n_31 = math.floor(n_sets / 2)
    # code die uit 10 sets bestaat = 8*42 + 42 31 of 6* 42 en 2*42 en 2*31 =
    # 9 * 42 + 31 en 42 42 + 4 * 42 + 4* 31
    #create regex: a|b matches a or b, (a|b){n1,n2}(c|d){m1,m2} matches a or b n times and c or d m times
    # 42set {min_n_42} 31set {max_n_31} #42 +1 EN 31 -1
    n_steps = n_sets - min_n_42

    for step in range(n_steps):
        n_42 = min_n_42 + step
        n_31 = max_n_31 - step
        pattern = pattern_42+'{'+str(n_42)+'}'+pattern_31+'{'+str(n_31)+'}'
        if re.search(pattern,code):
            solved_count += 1
            break

print(f"Part 2: {solved_count}")
