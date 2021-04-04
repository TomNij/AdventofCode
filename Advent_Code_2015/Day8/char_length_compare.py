import re
with open('../Inputs/8.txt') as file:
    input = file.readlines()

#chr to convert \x+int to char
#"\x27" to chr(int('27',16))

len("\x27")
a = "\x27"
for line in input:
    line = line.strip()
    a = line[1:len(line)-1] #remove opening and ending "
    print(a)