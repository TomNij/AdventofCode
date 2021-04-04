import itertools
import numpy as np

f = open('input.txt','r')
input = f.readlines()
input = [int(line.strip()) for line in input]
f.close()

for n1 in range(len(input)):
    for n2 in range(len(input)):
        for n3 in range(len(input)):
            if n1 < n2 and n1 < n3 and n2 < n3:
                val1 = input[n1]
                val2 = input[n2]
                val3 = input[n3]
                if val1+val2+val3 == 2020:
                    print(f"{val1},{val2},{val3} ={val1+val2+val3},Answer {val1*val2*val3}")

sumvals = [x*y*z for x in input for y in input for z in input if x+y+z == 2020]
print(sumvals[0])

#roald approach:
for nums in itertools.combinations(input, 3):
    if sum(nums) == 2020:
        print(nums[0] * nums[1] * nums[2])

data = [int(i) for i in input]
inp_len = len(data)
data_array = np.zeros((inp_len,inp_len,inp_len))
for x in range(np.shape(data_array)[0]):
    for y in range(np.shape(data_array)[1]):
        for z in range(np.shape(data_array)[2]):
            data_array[x,y,z] = data[x]+ data[y]+data[z]
indices = np.where(data_array == 2020)
indices = set(indices[0])
prod = 1
for ind in indices:
    prod *= data[ind]
print(prod)

print('New method')
numbers = data
for num1 in numbers:
    for num2 in numbers:
        if num1 + num2 > 2020:
            continue
        for num3 in numbers:
            if num1 + num2 + num3 > 2020:
                continue
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)