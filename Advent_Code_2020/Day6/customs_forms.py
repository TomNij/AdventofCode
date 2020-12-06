import re

f = open('input.txt','r')
input = f.read().split('\n\n')
input = [line.strip().replace('\n','') for line in input]
f.close()

def unique_char(line):
    return len(set(line))

def match_ans(list):
    match = 0
    n_ans = len(list)
    ans_line = ''.join(list)
    for char in set(ans_line):
        if ans_line.count(char) == n_ans:
            match += 1
    return match

output = [unique_char(line) for line in input]
print(f"Part 1: {sum(output)}")

f = open('input.txt','r')
input = f.read().split('\n\n')
input = [line.strip().split('\n') for line in input]
f.close()

output2 = [match_ans(line) for line in input]
print(f"Part 2: {sum(output2)}")
#You don't need to identify the questions to which anyone answered "yes";
# you need to identify the questions to which everyone answered "yes"!