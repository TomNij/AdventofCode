with open('../Input_files/6.txt') as file:
    input = file.read().strip()



def fish_sim(nr_of_days):
    lantern_list = list(map(int, input.split(',')))
    lantern_cohort = [lantern_list.count(val) for val in range(9)]
    for day in range(nr_of_days):
        zero_count = lantern_cohort[0]
        lantern_cohort[7] += zero_count
        lantern_cohort.pop(0)
        lantern_cohort.append(zero_count)
    return sum(lantern_cohort)

print(f"Part 1:{fish_sim(80)}")
print(f"Part 2:{fish_sim(256)}")