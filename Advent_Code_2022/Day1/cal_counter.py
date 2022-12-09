with open('../Input_files/1.txt') as file:
    input = file.read()
input = input.split('\n\n')

cal_list = []
max_cal = 0
for elf in input:
    elf_cal = sum(map(int,elf.strip().split('\n')))
    cal_list.append(elf_cal)
    if elf_cal > max_cal:
        max_cal = elf_cal

print(f"Part 1: {max_cal}")
cal_list.sort(reverse=True)
print(f"Part 2: {sum(cal_list[0:3])}")
