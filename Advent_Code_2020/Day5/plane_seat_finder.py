import re
import math
from datetime import datetime

import numpy as np
import time

start = datetime.now()
start_ms = int(round(time.time() * 1000))

f = open('input.txt','r')
input = f.readlines()
input = [line.strip() for line in input]
f.close()

def range_slicer(low,high,direction): #create function that gets a range and returns half that range based on the value L/R or U/D
    if direction == 'F' or direction == 'L': #front or left indicate we need lower half of range
        high = low+math.floor((high-low)/2)
    else:
        low = low+math.ceil((high-low)/2)
    return low,high

results = np.zeros((len(input),3)) #row,column,seat ID
row_high = 127
col_high = 7
for ind,line in enumerate(input):
    for ind2,directions in enumerate([line[0:7],line[7:]]):
        if directions[0] in ('F','B'):
            high = row_high
        else:
            high = col_high
        low = 0
        for char in directions:
            low,high = range_slicer(low,high,char)
            if low == high:
                results[ind,ind2] = low

#calculate seat ID
results[:,2] = results[:,0]*8 + results[:,1]
print(f"Highest id = {max(results[:,2])}")

#find my seat, find id that is not in list but +1 and -1 are in list
for seat in range(row_high*col_high):
    if (seat+1 in results[:,2]) and (seat-1 in results[:,2]) and (seat not in results[:,2]):
        print(f"My seat is: {seat}")
        break
print(f"Script duration:{datetime.now()-start}")
end_ms = int(round(time.time() * 1000))
print(f"Script duration ms:{end_ms-start_ms}")