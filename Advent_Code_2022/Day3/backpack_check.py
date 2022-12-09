import string
alpha = list(string.ascii_lowercase) + list(string.ascii_uppercase)
alpha_val = {letter: iter+1 for iter,letter in enumerate(alpha)}



with open('../Input_files/3.txt') as file:
    input = file.readlines()
input = [line.strip() for line in input]

score = 0
for line in input:
    line = line.strip()
    comp1 = set(line[0:len(line)//2])
    comp2 = set(line[len(line)//2:])
    overlap = comp1.intersection(comp2)
    for letter in list(overlap):
        score += alpha_val[letter]

score2 = 0
for group_ind in range(0,len(input),3):
    lines = input[group_ind:group_ind+3]
    line_set = list(map(set,lines))
    set_overlap = line_set[0]
    for test_set in line_set[1:]:
        set_overlap = set_overlap.intersection(test_set)
    for letter in list(set_overlap):
        score2 += alpha_val[letter]

print(f"Part 1: {score}")
print(f"Part 2: {score2}")