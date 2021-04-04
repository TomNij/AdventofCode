import re

with open('../Inputs/12.txt') as file:
    input = file.readlines()

a =1
#input is a list with a string that you can run through.
num_char = '-1234567890'
num_sum = 0
streak = ""
for char in input[0]:
    if char in num_char:
        streak += char
    elif streak:
        num_sum += int(streak)
        streak = ""

print(f"Part 1: {num_sum}")

def list_eval(list): #if a nested listobject is encountered this function should return the sum of entries in the list
    sum_out = 0
    for item in list:
        if item.type()

def dict_eval(dict): #if a nested dict object is encountered this function should return the sum of entries in the dict
    pass


input = eval(input[0])

for