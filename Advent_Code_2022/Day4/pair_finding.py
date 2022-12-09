with open('../Input_files/4.txt') as file:
    input = [line.strip() for line in file.readlines() if line != '\n']

overlap_count = 0
overlap_count2 = 0

for line in input:
    elf1,elf2 = line.split(',')
    elf1_min,elf1_max = map(int,elf1.split('-'))
    elf2_min, elf2_max = map(int,elf2.split('-'))

    #part 1 only count complete overlap of range 1 in 2 or 2 in 1.
    if elf1_min >= elf2_min and elf1_max <= elf2_max:
        overlap_count += 1
    elif elf2_min >= elf1_min and elf2_max <= elf1_max:
        overlap_count += 1

    #part 2 now any overlap counts: overlap happens if min1 in between min and max or max1 in between min and max
    if (elf1_min >= elf2_min and elf1_min <= elf2_max) or (elf1_max >= elf2_min and elf1_max <= elf2_max):
        overlap_count2 += 1
    elif (elf2_min >= elf1_min and elf2_min <= elf1_max) or (elf2_max >= elf1_min and elf2_max <= elf1_max):
        overlap_count2 += 1

print('Part 1:',overlap_count)
print('Part 2:',overlap_count2)