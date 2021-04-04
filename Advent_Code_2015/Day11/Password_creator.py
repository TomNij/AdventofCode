import numpy as np
from collections import Counter
old_pass = 'cqjxjnds'
old_pass_test  = 'ghjaaaaa' #ghijklmn is testcase

#requirements: 3 letter straight, not contain i o l, 2 different pairs (no overlap)

# quick approach after ixxxx move to jaaaa, same for o and l
# sets and doubles: big jumps are needed: move in straits if there are two doubles, move in doubles if there is a strait
def pass_to_num(password):
    return [ord(char)-97 for char in password] #a = 0, z = 25

def update_left(num_pass):
    if num_pass[-1] == 25:
        out = update_left(num_pass[0:-1])
        out.append(0)
        return out
    else:
        num_pass[-1] += 1
        return num_pass

def strait_detec(password):
    deltas = np.diff(pass_to_num(password))
    streak = [deltas[n] == 1 and deltas[n+1] == 1 for n in range(len(deltas)-1)]
    return any(streak)

def double_double_detec(password):
    #generate T/F of double entries in a password
    doubles = [password[n:n+2] for n in range(len(password)-1) if password[n] == password[n+1]]
    unique_doubles = list(set(doubles))
    return len(unique_doubles) >= 2

def iol_detec(password):
    return bool({'i', 'o', 'l'}.intersection(set(password)))

def valid_pass(password):
    return bool(strait_detec(password) and double_double_detec(password) and not iol_detec(password))

def next_iter(password):
    #return the next password to try after current password
    #mvp just return the next password incremented by one
    num_pass = pass_to_num(password)
    num_pass = update_left(num_pass)
    return ''.join([chr(el+97) for el in num_pass])


password = old_pass
while not valid_pass(password):
    password = next_iter(password)
print(f"Valid password 1 is: {password}")

#enter the found password into the machine again to get invalid pass to start next iteration
new_num = update_left(pass_to_num(password))
new_pass = ''.join([chr(el+97) for el in new_num])
password = new_pass
while not valid_pass(password):
    password = next_iter(password)

print(f"Valid password 2 is: {password}")