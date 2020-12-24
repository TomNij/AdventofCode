def flip_right(puzzle):
    ans = [row[::-1] for row in puzzle]
    return ans

def rotate_right(puzzle):
    ans = []
    for col in range(len(puzzle)):
        row = [puzzle[n][col] for n in range(len(puzzle)-1,-1,-1)]
        row = ''.join(row)
        ans.append(row)
    return ans

def add_hor_puzzle(puzzle1,puzzle2): #add piece 2 to existing piece 1
    if not puzzle1:
        return puzzle2
    else:
        ans = [puzzle1[row]+puzzle2[row] for row in range(len(puzzle2))]
        return ans

def add_vert_puzzle(puzzle1,puzzle2): # add piece 2 below piece 1
    if not puzzle1:
        return puzzle2
    else:
        ans = list(puzzle1)
        ans.extend(puzzle2)
        return ans