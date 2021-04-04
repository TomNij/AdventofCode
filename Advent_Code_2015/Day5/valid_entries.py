with open('../Inputs/5.txt') as file:
    input = file.readlines()
input = [line.strip() for line in input]

def check_forbidden(string):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    out = [string.count(substr) for substr in forbidden]
    if sum(out) > 0:
        return False
    else:
        return True

def check_double(string):
    for ind in range(len(string)-1):
        char = string[ind]
        if string[ind+1] == char:
            return True
    return False

def check_double_no_overlap(string):
    for ind in range(len(string)-1):
        charset = string[ind:ind+2]
        if string.count(charset) >= 2:
            return True
    return False

def check_double_with_letter(string):
    for ind in range(len(string)-2):
        char = string[ind]
        if string[ind+2] == char:
            return True
    return False

def vowel_count(string):
    vowels = 'aeiou'
    vowel_arr = [char for char in string if char in vowels]
    if len(vowel_arr) >= 3:
        return True
    else:
        return False

nice_str_1 = [str for str in input if check_forbidden(str) and check_double(str) and vowel_count(str)]
print(f"Part 1: {len(nice_str_1)}")
nice_str_2 = [str for str in input if check_double_no_overlap(str) and check_double_with_letter(str)]
print(f"Part 2: {len(nice_str_2)}")