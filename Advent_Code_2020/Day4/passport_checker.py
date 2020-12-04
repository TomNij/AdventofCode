import re

f = open('input.txt','r')
input = f.read().split('\n\n')
#input = [line.strip() for line in input]
f.close()

def passport_parser(line):
    expr_dict = {'byr' : 'byr:(\d+)',
                 'iyr': 'iyr:(\d+)',
                 'eyr' : 'eyr:(\d+)',
                 'hgt' : 'hgt:(\d+)([in|cm]{2})',
                 'hcl' : 'hcl:#([0-9a-f]+)',
                 'ecl' : 'ecl:(\w+)',
                 'pid': 'pid:(\d+)'} #'cid:' optional
    match = 0
    ecl_list = ('amb',  'blu' , 'brn' , 'gry' , 'grn' , 'hzl' , 'oth')
    for key,expr in expr_dict.items():
        hit = re.search(expr, line)
        if not hit is None:
            if key == 'byr' and len(hit.group(1)) == 4:
                byr = int(hit.group(1))
                if byr >= 1920 and byr <= 2002:
                    match += 1
            if key == 'iyr' and len(hit.group(1)) == 4:
                iyr = int(hit.group(1))
                if iyr >= 2010 and iyr <= 2020:
                    match += 1
            if key == 'eyr' and len(hit.group(1)) == 4:
                eyr = int(hit.group(1))
                if eyr >= 2020 and eyr <= 2030:
                    match += 1
            if key == 'hgt':
                unit = hit.group(2)
                hgt = int(hit.group(1))
                if unit == 'cm' and (hgt >= 150 and hgt <= 193):
                    match += 1
                elif unit == 'in' and (hgt >= 59 and hgt <= 76):
                    match += 1
            if key == 'hcl':
                try:
                    if len(hit.group(1)) == 6:
                        match += 1
                except(AttributeError):
                    pass
            if key == 'ecl':
                ecl = hit.group(1)
                if ecl in ecl_list:
                    match+=1
            if key == 'pid':
                try:
                    if len(hit.group(1)) == 9:
                        match += 1
                except(AttributeError):
                    pass
    return match == 7

input = [passport_parser(line) for line in input]
print(sum(input))
