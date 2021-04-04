import hashlib

key = 'ckczppom'
stop_arg1 = False
stop_arg2 = False
counter = 0
while stop_arg1 == False or stop_arg2 == False:
    enc_inp = (key+str(counter)).encode()
    hash_object = hashlib.md5(enc_inp)
    md5_hash = hash_object.hexdigest()
    if md5_hash[0:5] == '00000' and stop_arg1 == False:
        stop_arg1 = True
        print(f"Part 1: {counter}")
    elif md5_hash[0:6] == '000000':
        stop_arg2 = True
        print(f"Part 2: {counter}")
    counter += 1
