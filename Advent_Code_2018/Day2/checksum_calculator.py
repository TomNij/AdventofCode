import numpy as np
import re

f = open("input.txt", "r")
codes =  f.readlines()
codes = [code.strip() for code in codes]
f.close()

#abcdef contains no letters that appear exactly two or three times.
#bababc contains two a and three b, so it counts for both.
#abbcde contains two b, but no letter appears exactly three times.
#abcccd contains three c, but no letter appears exactly two times.
#aabcdd contains two a and two d, but it only counts once.
#abcdee contains two e.
#ababab contains three a and three b, but it only counts once.

def check_letters(str):
    letter_list = [letter for letter in str]
    dict_list = list(set(letter_list))
    code_dict = dict.fromkeys(dict_list,0)
    for letter in str:
        code_dict[letter] = code_dict[letter]+1
    return code_dict

def count_dict_values(dict,n):
    val_arr = np.array(list(dict.values()), dtype=np.int_)
    if np.max(val_arr == n):
        return True
    else:
        return False


dict_arr = [check_letters(code) for code in codes]
two_count = [count_dict_values(dict,2) for dict in dict_arr]
three_count = [count_dict_values(dict,3) for dict in dict_arr]
two_arr = np.array(two_count)
three_arr = np.array(three_count)
checksum = np.sum(two_arr) * np.sum(three_arr)
print(checksum)

#Part 2:
# for each string compare all other strings to find 1 char difference

for code in codes:
    for check_code in codes:
        char_diff = 0
        ind = 0
        for letter in code:
            check_letter = check_code[ind]
            ind += 1
            if letter != check_letter:
                char_diff += 1
            if char_diff > 1:
                break
        if (char_diff == 1):
            print(f"Code is: {code}")
            print(f"Compared against: {check_code}")