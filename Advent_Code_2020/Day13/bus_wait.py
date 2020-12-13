f = open('../Input_files/13.txt')
lines = f.readlines()
lines = [line.strip().split(',') for line in lines]
f.close()

time = int(lines[0][0])
bus_options = [int(bus) for bus in lines[1] if bus != 'x']

wait_arr = []
min_wait = 999999
min_bus = 0
for bus in bus_options:
    wait = bus - (time % bus)
    wait_arr.append((bus,wait))
    if wait < min_wait:
        min_wait = wait
        min_bus = bus
print(f"Part 1: {min_wait}*{min_bus} = {min_wait*min_bus}")


#Part 2
bus_options = [(wait_ind,int(bus_id)) for wait_ind,bus_id in enumerate(lines[1]) if bus_id != 'x']
#test = [1789,37,47,1889]
#bus_options = [(wait_ind,int(bus_id)) for wait_ind,bus_id in enumerate(test) if bus_id != 'x']
bus_options = sorted(bus_options, key=lambda x: -x[1])
last_bus = bus_options[len(bus_options)-1][1]

start_wait,start_busnr = bus_options[0]
check_val = start_busnr - start_wait
ind = 0
check_step = 1
for wait, bus_nr in bus_options:
    check_step *= bus_nr
    next_wait,next_bus = bus_options[ind+1]
    while check_val % next_bus != (next_bus - (next_wait % next_bus)) % next_bus:
        check_val += check_step
        #print(f"check_val: {check_val},step = {check_step}")
        if check_val % next_bus == (next_bus - (next_wait % next_bus)) % next_bus:
            ind += 1
    if next_bus == last_bus:
        print(f"Part2: {check_val}")
        break
