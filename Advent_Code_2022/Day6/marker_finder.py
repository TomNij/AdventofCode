with open('../Input_files/6.txt') as file:
    input = file.read().strip()

for marker_check in range(len(input)-4):
    text = input[marker_check:marker_check+4]
    if len(set(text)) == len(text):
        print("Part 1:",marker_check+4)
        break

for marker_check in range(len(input)-14):
    text = input[marker_check:marker_check+14]
    if len(set(text)) == len(text):
        print("Part 2:",marker_check+14)
        break