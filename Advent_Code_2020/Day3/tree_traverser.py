import numpy as np

f = open('input.txt','r')
input = f.readlines()
input = [line.strip() for line in input]
f.close()

v_len = len(input) #vertical length is defined by the input
input_len = len(input[0])

def input_parser(line):
    arr = np.zeros((len(line)))
    for ind in range(len(line)):
        if line[ind] == '#':
            arr[ind] = 1
    return arr

forest = np.zeros((v_len,input_len)) #rows correspond to vertical dist, cols to hor dist
for ind,line in enumerate(input):
    forest[ind,:] = input_parser(line)

rc_list = [(1,1),(3,1),(5,1),(7,1),(1,2)] #syntax (right,down)
answer_prod = 1
for rc_h,rc_v in rc_list:
    v_pos,h_pos,tree_count = (0,0,0)
    while v_pos <= v_len-1: #python 0 index
            tree_count += forest[v_pos,h_pos]
            h_pos = (h_pos + rc_h) % input_len #since forest repeats itself we can use modulo operator
            v_pos += rc_v

    print(f"Rc hor: {rc_h},Rc vert: {rc_v},Count ={tree_count}")
    answer_prod = answer_prod * tree_count

print(answer_prod)