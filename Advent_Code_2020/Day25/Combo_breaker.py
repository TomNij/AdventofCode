#my input
card_publ = 9789649
door_publ  = 3647239

div_val = 20201227

#examples
#card_publ = 5764801
#door_publ = 17807724
card = 1
subj_num = 7
card_loop = 0
while card != card_publ: #after a certain loop the card value equals card_publ
    card_loop += 1
    card = (card * subj_num) % div_val

encr = 1
for _ in range(card_loop):
    encr = (encr * door_publ) % div_val

print(f"Part 1: {encr}")
