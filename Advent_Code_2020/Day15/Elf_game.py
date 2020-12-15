import time
input = [1,0,16,5,17,4]

start = time.perf_counter()
spoken_list = list(input)
spoken_dict = {}
for ind,val in enumerate(input):
    spoken_dict[val] = [ind] #dict keeps track of numbers when they were last spoken

counter = len(spoken_list)
last = input[-1]
cutoff = 30000000
while counter < cutoff:
    if counter % 1000 == 0:
        print(f"List length: {counter}")

    if last not in spoken_dict.keys():
        spoken_dict[last] = [counter]
    elif len(spoken_dict[last]) == 1:
        spoken_dict[0].append(counter) #first time the number was added.
        last = 0
    else:
        [spoken_dict[last].pop(ind) for ind,_ in enumerate(spoken_dict[last][:-2])]
        last = spoken_dict[last][-1] - spoken_dict[last][-2]
        if last not in spoken_dict.keys():
            spoken_dict[last] = [counter]
        else:
            spoken_dict[last].append(counter)
    counter += 1
    if counter == (cutoff):
        print(last)
end = time.perf_counter()
print(f"Time taken: {end-start}s")