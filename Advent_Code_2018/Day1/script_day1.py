import numpy as np
import re

start_freq = 0
f = open("input.txt", "r")
deltas =  f.readlines()
f.close()
deltas = [re.sub('\+','',str) for str in deltas]
num_delta = np.array(deltas, dtype=np.int_)

tot_delta = np.sum(num_delta)

answer = start_freq + tot_delta
print(answer)

#Part 2
num_delta = np.tile(num_delta,100) #iterate 100 times for part 2
freq_track = np.tile(0,len(num_delta))
freq_track[0] = num_delta[0]
for i in range(1,len(num_delta)):
    freq_track[i] =num_delta[i]+freq_track[i-1] #add num to last element of freq_track and append it to freq track
test = list(set(freq_track))

unique_freq = []
for freq in freq_track:
    if freq in unique_freq:
        print(freq)
        break
    else:
        unique_freq.append(freq)