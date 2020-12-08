f = open('input.txt','r')
gr = {container.split('bags')[0].strip(): [(0 if x[0] == 'no' else int(x[0]), ' '.join(x[1:-1])) for x in (x.split() for x in containees.split(','))] for [container, containees] in map (lambda x: x.split('contain'), f.readlines())}
f.close()
def has_bag(container, bag):
    return any(1 for _, containee in gr.get(container, [(0, None)])
               if containee == bag or containee and has_bag(containee, bag))

def count_bags(container):
    return 1 + sum(count * count_bags(containee) if containee else 0 for count, containee in gr.get(container, [(0, None)]))

# Part 1
print(sum(1 for x in gr.keys() if has_bag(x, 'shiny gold')))

# Part 2
print(count_bags('shiny gold')-1)