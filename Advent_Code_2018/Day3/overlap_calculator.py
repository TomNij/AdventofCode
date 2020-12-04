import numpy as np
import re
from collections import defaultdict

f = open("input.txt", "r")
claims =  f.readlines()
claims = [claim.strip() for claim in claims]
f.close()

#idea: create a list of lists [[x1,x2,y1,y2], []]
# #123 @ 3,2: 5x4 starts at 4,3 ends at 8,6
def claim_parser(claim):
    expr = '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    id = int(re.search(expr, claim).group(1))
    x = int(re.search(expr, claim).group(2))
    y = int(re.search(expr, claim).group(3))
    w = int(re.search(expr, claim).group(4))
    h = int(re.search(expr, claim).group(5))
    coord_list = [id,x,y,w,h]
    return coord_list

parsed_claims = [claim_parser(claim) for claim in claims]

#calculate overlap between claims, divide by 2 in the end to account for double claims (a,b) (b,a)
fabric = np.zeros((1000,1000))
for claim in parsed_claims:
    id, x, y, w, h = claim
    fabric[x:x+w,y:y+h] += 1
            # create empty matrix of zeroes that get upgraded to 1
print(sum(sum(fabric>1)))
        #overlap x2 left - x1 right * y2 top - y1 bottom = bad idea!
        #overlap += (left[3] - right[1]) * (top[4] - bottom[2])

#part 2, check which claim has no overlap
for claim in parsed_claims:
    id, x, y, w, h = claim
    if (sum(sum(fabric[x:x+w,y:y+h])) == (w*h)): #check if fabric contains only ones (zero is not possible since we ran every claim.
        print(id)