with open('../Input_files/12.txt') as file:
    input = file.readlines()

#graph = {'A': ['B', 'C'],
             # 'B': ['C', 'D'],
             # 'C': ['D'],
             # 'D': ['C'],
             # 'E': ['F'],
             # 'F': ['C']}
def draw_graph(input):
    graph = {}
    for line in input:
        n1,n2 = line.strip().split('-')
        if not n1 in graph.keys():
            graph[n1] = [n2]
        else: #start node already present
            graph[n1].append(n2)
        if not n2 in graph.keys():
            graph[n2] = [n1]
        else: #start node already present
            graph[n2].append(n1)
    return graph

class Cave:
     def __init__(self, name):
        self.name = name
        self.size = 'small' if name.lower() == name else 'big'

graph = draw_graph(input)
cave_dict = {}
for cave_name in graph.keys():
    cave_dict[cave_name] = Cave(cave_name)

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        #if cave = small we are allowed to go back to big nodes
        if cave_dict[start].size == 'small' and cave_dict[node].size == 'big':
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    #paths is list of all paths (not all of them will contain end)
    return paths

def find_all_paths_specialcave(graph, start, end,special_cave, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        #if cave = small we are allowed to go back to big nodes
        if cave_dict[start].size == 'small' and cave_dict[node].size == 'big':
            newpaths = find_all_paths_specialcave(graph, node, end,special_cave, path)
        #if node is in path once and node == special_cave
        elif node == special_cave and path.count(node) == 1:
            newpaths = find_all_paths_specialcave(graph, node, end,special_cave, path)
        elif node not in path:
            newpaths = find_all_paths_specialcave(graph, node, end,special_cave, path)
        else:
            newpaths = []
        for newpath in newpaths:
            paths.append(newpath)
    #paths is list of all paths (not all of them will contain end)
    return paths

graph = draw_graph(input)
paths = find_all_paths(graph,'start','end')
print(f"Part 1:{len(paths)}")
#find all additional paths per special_cave
set_path = set(tuple(path) for path in paths)
for special_cave in cave_dict.keys():
    if cave_dict[special_cave].size == 'small' and special_cave not in ('start','end'):
        new_path = find_all_paths_specialcave(graph,'start','end',special_cave)
        new_set = set(tuple(path) for path in new_path)
        set_path = set_path.union(new_set)
#151430 too high
print(f"Part 2:{len(set_path)}")