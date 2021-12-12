with open('../Input_files/6.txt') as file:
    input = file.read().strip()



def fish_sim(nr_of_days):
    lantern_list = list(map(int, input.split(',')))
    for day in range(nr_of_days):
        if day % 16 == 0:
            print(f"Day = {day},list is {len(lantern_list)} long.")
        #order of events: reduce all values in list by 1, 0 --> 6
        zero_count = lantern_list.count(0)
        lantern_list = list(map(lambda x: x - 1 if x > 0 else 6,lantern_list))
        #generate list of 8's and add to lantern_list
        new_spawn = zero_count * [8]
        lantern_list = lantern_list + new_spawn
    return len(lantern_list)

print(f"Part 1:{fish_sim(80)}")
print(f"Part 2:{fish_sim(256)}")