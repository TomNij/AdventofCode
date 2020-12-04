f = open("input.txt", "r")
polymer =  f.read().strip()
test = 'bBCRGgrwgKknNGWnNWUuwHoeEtTOvEeVhYZz'
f.close()

polymer_in = polymer
print(len(polymer_in))
poly_mod = polymer_in
for char in list(set(polymer.lower())):
    print(char)
    polymer_in = polymer.replace(char,'').replace(char.upper(),'')
    poly_mod = polymer_in
    while True:
        polymer_in = poly_mod
        for ind in range(len(poly_mod)-1): #go over letters from left to right
            #check if letters do not match but do match when lowered
            if ((poly_mod[ind] != poly_mod[ind+1]) & (poly_mod[ind].lower() == poly_mod[ind+1].lower())):
                poly_mod = poly_mod[0:ind]+poly_mod[ind+2:] #remove current value and matching char to the right
                break
        if len(poly_mod) == len(polymer_in):
            print(f"{char},{len(poly_mod)}")
            break #break out of while loop