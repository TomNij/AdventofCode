import math
import re

with open('../Input_files/17.txt') as file:
    input = file.read()

xrange,yrange = re.search('(-?\d+\.\.-?\d+).+y=(-?\d+\.\.-?\d+)',input).groups()
xrange = list(map(int,xrange.split('..')))
yrange = list(map(int,yrange.split('..')))

def calc_traj(xrange,yrange,vx,vy):
    #assume start pos 0,0
    x,y = 0,0
    maxy = 0
    while x <= max(xrange) and (y >= min(yrange) or vy > 0) :

        x += vx
        y += vy
        if y > maxy:
            maxy = y

        #print(f"{x},{y}, vel:{vx},{vy}")
        if vx != 0:
            vx = vx -1 if vx >0 else vx + 1
        vy -= 1
        if x >= min(xrange) and x <= max(xrange) and y >= min(yrange) and y <= max(yrange):
            return True,maxy
    return(False,-1)


#since xrange is positive
tot_maxy = 0
hit_count = 0
for vx in range(1,1000):
    for vy in range(min(yrange),1000):
        hit,maxy = calc_traj(xrange,yrange,vx,vy)
        if hit:
            hit_count += 1
            if maxy > tot_maxy:
                tot_maxy = maxy

#3828 too low
print(f"Max y that hit target zone: {tot_maxy}")
print(f"Nr of distinct velocities that hit: {hit_count}")