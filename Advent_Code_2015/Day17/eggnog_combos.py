from  itertools import combinations

with open('../Inputs/17.txt') as file:
    container_input = file.readlines()

container_input = [int(container) for container in container_input]

counter = 0
for nr_containers in range(len(container_input)):
    for container_set in combinations(container_input,nr_containers):
        if sum(container_set) == 150:
            counter += 1

print(f"Part 1: {counter}")


for nr_containers in range(len(container_input)):
    container_counter = 0
    for container_set in combinations(container_input,nr_containers):
        if sum(container_set) == 150:
            container_counter += 1
    if container_counter > 0:
        print(f"Part 2: {container_counter}")
        break
