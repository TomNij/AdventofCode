f = open('input.txt','r')
input = f.readlines()
input = [int(line.strip()) for line in input]
f.close()

input = sorted(input)
input.insert(0,0) #add 0 at the start of the list to calculate also the first difference

def diff_list(list):
    output = []
    for ind in range(len(list)-1):
        output.append(list[ind+1] - list[ind]) # element 0 is difference between input 1 and input 0
    return output

differences = diff_list(input)
differences.append(3) #add another 3 jolt difference at the end to go to your device

print(f"Part1: 1jolt diff {differences.count(1)}, 3jolt diff: {differences.count(3)}, answer: {differences.count(1)*differences.count(3)}  ")

#Part2 calculate ranges of 1 and add multiplier: 1 1 gives 2 options, 1 1 1 gives 4 options, 1 1 1 1 gives 6, 1 1 1 1 1 = 12


multiplier_dict = {0:1,
                   1:1,
                   2:2,
                   3:4,
                   4:7,
                   5:12}
multiplier = 1
streak = 0
#differences = [1,3,1,3] #
for ind,val in enumerate(differences):
    if val == 1:
        streak += 1
    if val == 3 and differences[ind-1] == 1:
        multiplier *= multiplier_dict[streak]
        streak = 0

print(f"Part 2 answer: {multiplier}")