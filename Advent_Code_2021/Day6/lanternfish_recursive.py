with open('../Input_files/6.txt') as file:
    input = file.read().strip()

def fish_gen(val,days):
    if val >= days:
        return 0
    else:
        new_fish = (days - val) // 7
        #suppose 16 new fishes will be created in 7day intervals each has val 8 at the start and different days left
        return(new_fish + sum([fish_gen(8,day_val) for day_val in range(days-val,0,-7)]))

#approach:
#calculate for each fish how many fish it will spawn as a function of days till end
#store result in dictionary use dictionary for calculations
fish_dict = {}
for day in range(257):
    if day <= 6:
        fish_dict[day] = 1#each fish creates no offspring
    else:
        d_rec = day
        fish_dict[day] = 1 #add entry for fish itself
        #take into account new fish go in cycles of 9 days
        # on day 7 it produces a new fish, but unless that fish has 9 days to live it wont create new fish itself
        while d_rec-7 in fish_dict.keys():
            fish_dict[day] += fish_dict[d_rec-7]
            d_rec -= 7
a = 1

fish_gen_dict = {}
for day in range(257):
    if day <= 6:
        fish_gen_dict[day] = 1#each fish creates no offspring




def fish_sim_rec(nr_of_days):
    lantern_list = list(map(int, input.split(',')))
    #recursive function is too slow and produces wrong result, memoization needed to speed up calculations
    return sum([fish_gen(val,nr_of_days) for val in lantern_list])
    #return sum([fish_dict[nr_of_days - val] for val in lantern_list])

print(f"Part 1:{fish_sim_rec(80)}")
print(f"Part 2:{fish_sim_rec(256)}")
#print(f"Part 2:{fish_sim(256)}")