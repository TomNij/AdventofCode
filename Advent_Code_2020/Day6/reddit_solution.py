def day6():
    with open('input.txt', 'r') as f:
        data = [list(map(set, line.splitlines())) for line in f.read().split('\n\n')]
    # Part1
    part1 = 0
    part2 = 0
    for group in data:
        part1 += len(set.union(*group))
        part2 += len(set.intersection(*group))
    print(f"Part1: {part1}")
    print(f"Part2: {part2}")
day6()