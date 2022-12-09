def calc_magnitude(input):
    #base case, assumption inputs or sub lists consist of only 2 elements
    if not isinstance(input[0],list) and not isinstance(input[1],list):
        return 3*input[0] + 2*input[1]
    elif isinstance(input[0],list) and not isinstance(input[1],list):
        return calc_magnitude([calc_magnitude(input[0]),input[1]])
    elif not isinstance(input[0],list) and isinstance(input[1],list):
        return calc_magnitude([input[0],calc_magnitude(input[1])])
    else:
        return calc_magnitude([calc_magnitude(input[0]), calc_magnitude(input[1])])
