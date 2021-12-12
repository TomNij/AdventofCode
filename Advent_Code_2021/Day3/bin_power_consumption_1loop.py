import numpy as np
with open('../Input_files/3.txt') as file:
    input = file.readlines()

input_org = [line.strip() for line in input]
#convert input in list of lists
input_org = [list(map(int,line)) for line in input_org]
n_bits = len(input_org[0])
#rotate input to have from 1000 x 10, a 10 x 1000 array
def rotate_list(lists):
    ans = []
    for col in range(len(lists[0])):
        row = [lists[n][col] for n in range(len(lists))]
        ans.append(row)
    return ans

def return_median_at_pos(lists,i):
    col_list = [line[i] for line in lists]
    return np.median(col_list)

input = rotate_list(input_org)
gamma = 0
eps = 0
#pt2
co2_scrub = input_org
ox_gen = input_org
for ind,values in enumerate(input):
    if np.median(values) == 1:#1 is most common bit
        gamma += 2**(n_bits-ind-1) #-1 since ind will end at 11 but bin ends at 2**0
    elif np.median(values) == 0: #0 is most common bit
        eps += 2**(n_bits-ind-1)
    else:
        print('Error, a tie occurred!')

    if len(ox_gen)> 1:
        if return_median_at_pos(ox_gen,ind) == 0:
            ox_gen = [line for line in ox_gen if line[ind] == 0]
        else:
            ox_gen = [line for line in ox_gen if line[ind] == 1]
    if len(co2_scrub) > 1:
        if return_median_at_pos(co2_scrub,ind) == 0:
            # median == 0, least common value == 1
            co2_scrub = [line for line in co2_scrub if line[ind] == 1]
        else: #tie,take 0
            co2_scrub = [line for line in co2_scrub if line[ind] == 0]

ox_val = sum([i*(2**(n_bits-bit-1)) for i,bit in zip(ox_gen[0],range(n_bits))])
co2_val = sum([i*(2**(n_bits-bit-1)) for i,bit in zip(co2_scrub[0],range(n_bits))])
print(f"Part 1:{gamma*eps}")
print(f"Part 2:{ox_val*co2_val}")




