with open('../Input_files/19_test.txt') as file:
    lines = file.read().split('\n\n')

rules = lines[0].split('\n')
codes = lines[1].split('\n')



def create_rule_set(rule_list,output): #replace rulenr with 'a' or 'b' and check if all nrs are replaced
    ab_count = 0
    for element in rule_list:
        if element in ('a','b'):
            ab_count += 1
    if ab_count == len(rule_list):
        output.append(''.join(rule_list))

    if isinstance(rule_list[0],list): #if the rule_list is a list of lists
        create_rule_set(rule_list[0], output)
        create_rule_set(rule_list[1], output)
    else:
        for ind,rule in enumerate(rule_list): #go over rule list, return a,b if rule_dict[rule_set] = a or b
            if rule in rule_dict.keys():
                if rule_dict[rule] in ('a','b'):
                    rule_list[ind] = rule_dict[rule]
                else:  # e.g. [38,54]
                    create_rule_set(rule_list= rule_dict[rule], output = output)






rule_dict = { rule.split((':'))[0]: rule.split((':'))[1].strip() for rule in rules
}
for key,val in rule_dict.items():
    if val not in ('a','b'):
        new_rules = rule_dict[key].split(' | ')
        new_rules = [rule.split(' ') for rule in new_rules]
        #change [[4, 3]] to ['4','3'] keep [[2,3],[4,5]] as is.
        if len(new_rules) == 1:
            new_rules = new_rules[0]
        rule_dict[key] = new_rules

a =[]
create_rule_set(rule_dict['0'],a)