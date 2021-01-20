
with open('../Inputs/2.txt') as file:
    input = file.readlines()
input = [line.strip().split('x') for line in input]

def packing_paper(list):
    list = sorted(list,key=lambda x:int(x))
    x1, x2, x3 = map(int, list)
    min_surface = x1 * x2
    paper_surface = 2*x1*x2 + 2*x2*x3 + 2*x3*x1 + min_surface
    return paper_surface

def packing_lint(list):
    list = sorted(list,key=lambda x:int(x))
    x1,x2,x3 = map(int,list)
    ribbon = x1*x2*x3
    wrapping = 2*x1 + 2*x2
    lint_len = ribbon + wrapping
    return lint_len

print(f"Part1: {sum([packing_paper(line) for line in input])}")
print(f"Part2: {sum([packing_lint(line) for line in input])}")