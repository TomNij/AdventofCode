import re
import math

with open('../Inputs/day1.txt') as file:
    input = file.read()

upward = input.count('(')
downward = input.count(')')
start = 0
end = start + upward - downward

print(f"Part 1: {end}")

floor = 0
for ind,char in enumerate(input):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

    if floor == -1:
        print(f"Part 2: {ind+1}")
        break