import time
from collections import deque
input = [1,0,16,5,17,4]

start = time.perf_counter()
spoken_list = list(input)


spoken_dict = {val: deque([ind],maxlen=2) for ind,val in enumerate(input)}#dict keeps track of numbers when they were last spoken

counter = len(spoken_list)
last = input[-1]
cutoff = 30000000
while counter < cutoff:
    if counter % 1000 == 0:
        print(f"List length: {counter}")

    if last not in spoken_dict.keys():
        spoken_dict[last] = deque([counter],maxlen=2)
    elif len(spoken_dict[last]) == 1:
        spoken_dict[0].append(counter) #first time the number was added.
        last = 0
    else:
        last = spoken_dict[last][1] - spoken_dict[last][0]
        if last not in spoken_dict.keys():
            spoken_dict[last] = deque([counter],maxlen=2)
        else:
            spoken_dict[last].append(counter)
    counter += 1
    if counter == (cutoff):
        print(last)
end = time.perf_counter()
print(f"Time taken: {end-start}s")