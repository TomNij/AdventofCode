from collections import deque

with open('../Input_files/5.txt') as file:
    input = file.read()

stacks,moves = input.split('\n\n')

def rotate_right(stacks):
    ans = []
    for col in range(len(stacks[0])):
        row = [stacks[n][col] for n in range(len(stacks)-1,-1,-1)]
        row = ''.join(row)
        ans.append(row)
    return ans


stacks = rotate_right(stacks.split('\n'))
stack_list = []
stack_list2 = []

for ind in range(1,len(stacks),4):
    stack = stacks[ind].strip()[1:]
    stack_list.append(deque(stack))
    stack_list2.append(deque(stack))

#input contains white line
for move in moves.split('\n')[:-1]:
    #move 3 from 6 to 2
    _,n,_,origin,_,dest = move.split(' ')
    #substract 1 to account for 0 based python
    n, origin, dest = int(n), int(origin) - 1, int(dest) - 1
    move_list1 = []
    move_list2 = []
    for _ in range(n):
        move_list1.append(stack_list[origin].pop())
        move_list2.append(stack_list2[origin].pop())
    stack_list[dest].extend(move_list1)
    #for part 2 we need to reverse the movelist
    moves_rev = move_list2[::-1]
    stack_list2[dest].extend(moves_rev)

top_containers = [s[-1] for s in stack_list]
top_containers2 = [s[-1] for s in stack_list2]

print('Part 1:', ''.join(top_containers))
print('Part 2:', ''.join(top_containers2))