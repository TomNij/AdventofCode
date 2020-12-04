import re
import numpy as np
import string

f = open("input.txt", "r")
instr =  f.readlines()
f.close()
instr = [line.strip() for line in instr]
order_list = []
blocker_list = []
blocked_list = []
alphabet = string.ascii_uppercase

for line in instr:
    expr = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin.'
    blocker = re.search(expr,line).group(1)
    blocked = re.search(expr,line).group(2)
    blocker_list.append(blocker)
    blocked_list.append(blocked)
    order_list.append([blocker,blocked])

def unblock(char,list,final_order):
    available = [instr[1] for instr in list if instr[0] ==char] #A is done, that means instr blocked by A become available
    #check if available strings are not blocked by other instructions:
    for order in [instr for instr in list if instr[0] not in final_order]: #loop over orders that do not start with char that are unblocked
        blocked = order[1]
        if blocked in available:
            pop_ind = available.index(blocked)
            available.pop(pop_ind)
    return available

def task_time(char):
    time = 60 + alphabet.index(char) + 1
    return time

instr_set = list(set(blocker_list))
start = sorted(np.setdiff1d(instr_set,blocked_list))
final_order = ''
time = 0
n_worker = 5
t_remaining = np.zeros((n_worker))
while start :
    for worker in range(n_worker):
        t = t_remaining[worker]
        if t == 0: #Error in script, once worker starts on task its blockers are inmediately resolved while that should wait.
            letter = start[0]
            print(f"Worker {worker} started with {letter} at time: {time}")
            t_remaining[worker] = task_time(letter)

            # for worker available remove letter from available
            final_order += letter

            available = unblock(letter,order_list,final_order)
            start.extend(available)

            start.pop(0)#take the first element
            start.sort()

    if not start: #start is empty, meaning last task has been picked up and final time is time when that is finished
        time += np.max(t_remaining)
    else:
        time += 1
    t_remaining -= 1  # remove a second from all workers
print(final_order)
print(time)