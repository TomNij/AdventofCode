input = '3113322113'

for round in range(50):
    output = ''
    streak = 1
    for ind,char in enumerate(input):
        if ind == len(input) - 1: #case for last character
            output += str(streak) + char
            streak = 1
        elif input[ind+1] == char: #case for streak
            streak += 1
        else:
            output += str(streak) + char
            streak = 1 #reset streak
    #print(f"Output after round {round}: {output}")
    input = output
    if round == 39:
        print(f"Part 1: {len(output)}")
print(f"Part 2: {len(output)}")