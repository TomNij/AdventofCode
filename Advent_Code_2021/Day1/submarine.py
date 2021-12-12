
with open('../Input_files/1.txt') as file:
    input = file.readlines()

input = list(map(int,input))
incr_counter = 0
for ind in range(1,len(input)):
    if input[ind] - input[ind-1] > 0:
        incr_counter += 1

print(f"Part 1: {incr_counter}")

#will take sliding window sum of i, i-1 and i-2
def slide_sum(input,i):
    return input[i] + input[i-1] +input[i-2]

incr_sl_counter = 0
for ind in range(3,len(input)):
    if slide_sum(input,ind) - slide_sum(input,ind-1) > 0:
        incr_sl_counter += 1

print(f"Part 2: {incr_sl_counter}")