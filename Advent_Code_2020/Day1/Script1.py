f = open('input.txt','r')
input = f.readlines()
input = [int(line.strip()) for line in input]
f.close()

for n1 in range(len(input)):
    for n2 in range(len(input)):
        for n3 in range(len(input)):
            if n1 < n2 and n1 < n3 and n2 < n3:
                val1 = input[n1]
                val2 = input[n2]
                val3 = input[n3]
                if val1+val2+val3 == 2020:
                    print(f"{val1},{val2},{val3} ={val1+val2+val3},Answer {val1*val2*val3}")