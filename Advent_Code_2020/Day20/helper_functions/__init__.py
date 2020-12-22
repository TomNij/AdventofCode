def add_hor_puzzle(puzzle1,puzzle2): #add piece 2 to existing piece 1
    if not puzzle1:
        return puzzle2
    else:
        ans = [puzzle1[col]+puzzle2[col] for col in range(len(puzzle2))]
        return ans

def add_vert_puzzle(puzzle1,puzzle2): # add piece 2 below piece 1
    if not puzzle1:
        return puzzle2
    else:
        ans = list(puzzle1)
        ans.extend(puzzle2)
        return ans