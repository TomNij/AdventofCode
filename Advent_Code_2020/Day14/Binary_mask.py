import re

f = open('../Input_files/14.txt')
lines = f.readlines()
lines = [line.strip() for line in lines]
f.close()

def memory_parser(line):
    expr = 'mem\[(\d+)\] = (\d+)'
    adres,val = re.search(expr,line).groups()
    return (int(adres),int(val))

def apply_mask_val(mask,val):
    val_bin = list('{0:036b}'.format(val))
    for ind,char in enumerate(mask):
        if char != 'X':
            val_bin[ind] = char
    val_bin = ''.join(val_bin)
    val_dec = sum([int(char) * 2**(35-ind) for ind,char in enumerate(val_bin)])
    return val_dec

def apply_mask_adres(mask,adres):
    adres_bin = list('{0:036b}'.format(adres))
    for ind,char in enumerate(mask):
        if char != '0': #values unequal to 0 are overwritten
            adres_bin[ind] = char
    adres_bin = ''.join(adres_bin)
    return adres_bin

def recursive_x_resolving(output,adress_bin):
    if adress_bin.count('X') == 0: #no more X's
        output.append(adress_bin)
    else:
        # replace list element with 2 elements that have one x less
        lower = list(adress_bin)
        upper = list(adress_bin)
        for ind, char in enumerate(adress_bin):
            if char == 'X':
                lower[ind] = '0'
                upper[ind] = '1'
                break
        recursive_x_resolving(output,''.join(lower))
        recursive_x_resolving(output, ''.join(upper))



mem_dict = {}
for line in lines:
    if line[0:4] == 'mask':
        mask = line.replace('mask = ','')
    else:
        adres,val = memory_parser(line)
        val_dec = apply_mask_val(mask,val)
        mem_dict[adres] = val_dec

print(f"Part 1: {sum(mem_dict.values())}")

#Part 2: mask applies to memory value and X's need to be treated as both 0 and 1
mem_dict = {}
for line in lines:
    if line[0:4] == 'mask':
        mask = line.replace('mask = ','')
    else:
        adres,val = memory_parser(line)
        adres_bin = apply_mask_adres(mask,adres)
        adresses = []
        recursive_x_resolving(adresses, adres_bin)
        #now we need to get a list of adresses based on the mask and the adres
        for adres in adresses:
            adres_dec = sum([int(char) * 2**(35-ind) for ind,char in enumerate(adres)])
            mem_dict[adres_dec] = val

print(f"Part 2: {sum(mem_dict.values())}")