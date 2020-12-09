f = open('input.txt','r')
input = f.readlines()
input = [int(line.strip()) for line in input]
f.close()

def sum_options(list):
    answer = []
    for ind,val in enumerate(list):
        for ind2,val2 in enumerate(list):
            if ind < ind2:
                answer.append(val+val2)
    return answer

pre_amble_len = 25
for ind,number in enumerate(input):
    if ind >= pre_amble_len:#24 still part of preamble, 25 is ok
        check_list = input[ind-25:ind] #for ind = 25 it should run from 0 to 24
        if input[ind] not in sum_options(check_list):
            print(f"First number not in preamble: {input[ind]}")
            check_val = input[ind]

start = 0 #start with empty list
end = 0
while True:
    if sum(input[start:end]) == check_val:
        lowest = min(input[start:end])
        highest = max(input[start:end])
        print(f"Min,max,sum = {lowest},{highest}, {lowest+highest}")
        break
    elif sum(input[start:end]) > check_val:
        start += 1
    elif sum(input[start:end]) < check_val:
        end += 1