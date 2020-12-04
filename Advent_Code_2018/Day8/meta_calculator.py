import numpy as np

f = open("input.txt", "r")
tree =  f.read()
f.close()

tree = tree.split(' ')
tree = [item.strip() for item in tree]
#convert itemns in integers:
tree = np.array(tree,dtype=int)

n_meta = tree[1]
n_child = tree[0]
meta_sum = np.sum(tree[-n_meta:])
remain = tree[2:-n_meta]
while remain: #break down remain into children and add meta data to meta sum
    pass
