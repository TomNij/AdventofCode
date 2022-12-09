with open('../Input_files/2.txt') as file:
    input = file.readlines()

#opp, vs myself : outcome
#A rock, B, paper, C sciccors
rules1 = {('A','X') : 3,
         ('A','Y') : 6,
         ('A','Z') : 0,
         ('B','X'): 0,
         ('B','Y'): 3,
         ('B','Z'): 6,
         ('C','X'): 6,
         ('C','Y'): 0,
         ('C','Z'): 3}

#pt2 X means I lose, Y tie, Z win
rules2 = {('A','X') : 'Z',
         ('A','Y') : 'X',
         ('A','Z') : 'Y',
         ('B','X'): 'X',
         ('B','Y'): 'Y',
         ('B','Z'): 'Z',
         ('C','X'): 'Y',
         ('C','Y'): 'Z',
         ('C','Z'): 'X'}

throw_score = {'X' : 1,
               'Y' : 2,
               'Z' : 3}

tot_score1 = tot_score2 = 0
input = [line.strip() for line in input if line != '\n']
for line in input:
    opp,instr = line.strip().split(' ')
    score1 = rules1[(opp,instr)] + throw_score[instr]
    tot_score1 += score1

    myself = rules2[(opp,instr)]
    score2 = rules1[(opp, myself)] + throw_score[myself]

    tot_score2 += score2

print(f"Part 1: {tot_score1}")
print(f"Part 2: {tot_score2}")