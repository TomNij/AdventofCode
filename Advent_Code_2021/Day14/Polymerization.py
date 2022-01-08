from collections import Counter

with open('../Input_files/14.txt') as file:
    input = file.read().strip()

template,rules = input.split('\n\n')
rules = rules.split('\n')
rule_dict = {}
for rule in rules:
    pattern,insert = rule.split(' -> ')
    rule_dict[pattern] = insert

couple_dict = {}
for rule in rules:
    pattern,insert = rule.split(' -> ')
    couple_dict[pattern] = [pattern[0]+insert,insert+pattern[1]]
in_str = template

#pt1 approach
for step in range(10):
    n_insert = 0
    out_str = in_str
    for ind in range(len(in_str)):
        pattern = in_str[ind:ind+2]
        if pattern in rule_dict.keys():
            #pattern[0] + rule_dict[pattern] + pattern[1]
            out_str = out_str[:2*n_insert+1] + rule_dict[pattern] + in_str[ind+1:]
            n_insert += 1
    in_str = out_str
    if step == 9:
        count_list = [out_str.count(letter) for letter in set(out_str)]
        count_list.sort()
        print(f"Part 1: {count_list[-1] - count_list[0]}")

#pt2 approach
def dict_to_counts(couple_count,first,last):
    letters = set(''.join(couple_count.keys()))
    letter_value = dict.fromkeys(letters,0)
    for key,val in couple_count.items():
        #we are counting the first key (val-1) times twice and once correct, similar for last key
        if key == first:
            letter_value[key[0]] += 0.5 * (val - 1) + 1
            letter_value[key[1]] += 0.5*val
        elif key == last:
            letter_value[key[0]] += 0.5 *val
            letter_value[key[1]] += 0.5 * (val - 1) + 1
        else:
            letter_value[key[0]] += 0.5 * val
            letter_value[key[1]] += 0.5 * val
    ans = max(letter_value.values()) - min(letter_value.values())
    return ans

couple_count = Counter()
for ind in range(len(template)-1):
    couple_count.update([template[ind:ind+2]])
first = template[0:2]
last = template[-2:]
for step in range(40):
    if first in couple_dict.keys():
        first = couple_dict[first][0]
    if last in couple_dict.keys():
        last = couple_dict[last][1]
    #issue += means couples before splitting are kept, issue = means couples from different originating couples are not added
    new_count = Counter()
    for key,val in list(couple_count.items()):
        if key in couple_dict.keys():
            l,r = couple_dict[key]
            new_count[l] += val
            new_count[r] += val
        else:
             new_count.update(key)
    #update couple count with the results from the new iteration
    couple_count = new_count
    if step == 9:
        print(f"Part 1: {dict_to_counts(couple_count, first, last)}")
    if step == 39:
        print(f"Part 2: {dict_to_counts(couple_count, first, last)}")