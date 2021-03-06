from operator import add

with open('../Input_files/18.txt') as file:
    input = file.readlines()

test_input = ['2 * (3 + (4 * 5) + 6)'] # = 2* (3 + 20 + 6) = 58
#input = [line.split(' ') for line in test_input]

def int_product(a,b):
    return a*b

def solve_no_par(exersize): #exersize is a list of integers and operators
    ans = int(exersize[0]) #start with first number
    for ind in range(1,len(exersize)):
        element = exersize[ind]
        if element in operator_dict.keys():
            func = operator_dict[element]
        else:
            ans = func(ans,int(element))
    return ans
operator_dict = {'+': add,
                 '*': int_product}

tot_ans = 0
for exersize in input:
    while exersize.count('(') > 0:
        par_open_ind = [ind for ind,char in enumerate(exersize) if char == '(']
        right_par_open = max(par_open_ind)
        par_close_ind = [ind for ind,char in enumerate(exersize) if char == ')' and ind > right_par_open]
        right_par_close = par_close_ind[0]
        sub_ex = exersize[right_par_open+1:right_par_close]
        sub_ans = solve_no_par(sub_ex.split(' '))
        exersize = exersize[0:right_par_open]+str(sub_ans)+ exersize[right_par_close+1:]

    exersize = exersize.split(' ')
    tot_ans += solve_no_par(exersize)
print(tot_ans)