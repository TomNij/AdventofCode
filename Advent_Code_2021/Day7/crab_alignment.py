with open('../Input_files/7.txt') as file:
    input = file.read().strip()

crab_pos = list(map(int, input.split(',')))
min_fuel = 99999999999999999
for pos in range(min(crab_pos),max(crab_pos)+1):
    tot_fuel = sum(map(lambda x: abs(x-pos),crab_pos))
    if tot_fuel < min_fuel:
        min_fuel = tot_fuel
print(f"Part 1:{min_fuel}")

min_fuel = 99999999999999999
for pos in range(min(crab_pos),max(crab_pos)+1):
    #use sum (1:n)  = 0.5*n*(n+1)
    tot_fuel = sum(map(lambda x: 0.5*abs(x-pos)*(abs(x-pos)+1),crab_pos))
    #tot_fuel = sum(map(lambda x: sum(range(abs(x - pos))), crab_pos))

    if tot_fuel < min_fuel:
        min_fuel = tot_fuel

print(f"Part 2:{min_fuel}")