import re
test = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

f = open('input.txt','r')
input = f.readlines()
input = [line.strip() for line in input]
f.close()

def pass_parser(line):
    expr = '(\d+)-(\d+) ([a-z]): ([a-z]+)'
    n_min,n_max,test_char,passw = re.search(expr, line).groups()
    return [int(n_min),int(n_max),test_char,passw]

input = [pass_parser(line) for line in input]

valid_pass = 0
for password in input:
    n1, n2, testchar,passw = password
    #hits = passw.count(testchar)
    #hits >= n_min and hits <= n_max:
        #valid_pass += 1
    if passw[n1-1] == testchar or passw[n2-1] == testchar:
        if not (passw[n1-1] == testchar and passw[n2-1] == testchar):
            valid_pass += 1
print(f"Valid passwords: {valid_pass}")