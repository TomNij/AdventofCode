with open('../Input_files/9.txt') as file:
    input = file.readlines()

def height_checker(height_map,indx,indy):
    reference = height_map[indx][indy]
    check_pos = []
    hmap_x = len(height_map)
    hmap_y = len(height_map[0])
    if indx - 1 in range(hmap_x):
        check_pos.append((indx-1,indy))
    if indx + 1 in range(hmap_x):
        check_pos.append((indx + 1, indy))
    if indy - 1 in range(hmap_y):
        check_pos.append((indx, indy -1))
    if indy +1 in range(hmap_y):
        check_pos.append((indx, indy + 1))
    low = all([reference < height_map[x][y] for x,y in check_pos])
    return low
height_map = [list(map(int,line.strip())) for line in input]

low_points = []
for x in range(len(height_map)):
    for y in range(len(height_map[0])):
        if height_checker(height_map,x,y):
            low_points.append(height_map[x][y])

print(f"Part 1:{sum(low_points) + len(low_points)}")

basins = []
height_map_basins = [[val < 9 for val in line] for line in height_map]
basin_checked = []
hmap_x = len(height_map_basins)
hmap_y = len(height_map_basins[0])
for x in range(len(height_map_basins)):
    for y in range(len(height_map_basins[0])):
        if (x,y) not in basin_checked:
            basin = []
            locations_to_check = [(x, y)]
            while locations_to_check:
                check_x,check_y = locations_to_check[0]
                if (check_x,check_y) not in basin_checked:
                    if height_map_basins[check_x][check_y]:
                        basin.append((check_x,check_y))
                        basin_checked.append((check_x,check_y))
                        if check_x - 1 in range(hmap_x):
                            if (check_x - 1, check_y) not in basin_checked:
                                locations_to_check.append((check_x - 1, check_y))
                        if check_x + 1 in range(hmap_x):
                            if (check_x + 1, check_y) not in basin_checked:
                                locations_to_check.append((check_x + 1, check_y))
                        if check_y - 1 in range(hmap_y):
                            if (check_x , check_y - 1) not in basin_checked:
                                locations_to_check.append((check_x , check_y - 1))
                        if check_y + 1 in range(hmap_y):
                            if (check_x, check_y+ 1) not in basin_checked:
                                locations_to_check.append((check_x , check_y + 1))
                locations_to_check.pop(0)
            if basin:
                basins.append(basin)

basin_size = [len(basin) for basin in basins]
basin_size = sorted(basin_size,reverse=True)
pt2 = basin_size[0] * basin_size[1] *basin_size[2]
print(f"Part 2: {pt2}")