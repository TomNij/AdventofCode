import re
from collections import deque


#1 parse puzzle pieces
with open('../Input_files/22.txt') as file:
    input = file.read().split('\n\n')

game_dict = {}
player_expr = 'Player (\d+):'
for player in input:
    input = player.split('\n')
    cards = deque()
    for line in input:
        if line[0:6] == 'Player':
            id = re.search(player_expr,line).group(1)
        else:
            cards.append(int(line))
    game_dict[id] = cards

def combat_player(cards1,cards2): #cards1 and 2 are the player deques
    while cards1 and cards2:
        val1 = cards1.popleft()
        val2 = cards2.popleft()
        if val1 > val2:
            cards1.append(val1)
            cards1.append(val2)
        else: #val2 higher than val1
            cards2.append(val2)
            cards2.append(val1)
        if not cards1: #no more cards in cards1
            return (2,cards2)
        elif not cards2:
            return (1,cards1)

def recursive_combat_player(cards1, cards2):  # cards1 and 2 are the player deques
    game_config = []
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    while cards1 and cards2:
        if [list(cards1),list(cards2)] in game_config:
            return (1,cards1) #player 1 wins
        #add config to main configs
        game_config.append([list(cards1),list(cards2)]) #add game config[cards1,cards2] = [[2,3,5],[4,6,9]]
        #draw cards for both players
        val1 = cards1.popleft()
        val2 = cards2.popleft()
        if len(cards1) >= val1 and len(cards2) >= val2: #condition to play recursive combat
            #recursive combat should return a winner to determine if cards1 get appended or cards2
            #start game with number of cards equal to card drawn
            rec1 = list(cards1)[0:val1]
            rec2 = list(cards2)[0:val2]
            winner,_ = recursive_combat_player(rec1,rec2)
            if winner == 1:
                cards1.append(val1)
                cards1.append(val2)
            else:
                cards2.append(val2)
                cards2.append(val1)
        else:
            if val1 > val2:
                cards1.append(val1)
                cards1.append(val2)
            else:  # val2 higher than val1
                cards2.append(val2)
                cards2.append(val1)
        if not cards1:  # no more cards in cards1
            return (2, cards2)
        elif not cards2:
            return (1, cards1)

def score_calc(cards):
    ans = 0
    n_cards = len(cards)
    for ind,val in enumerate(cards):
        ans += (n_cards - ind) * val
    return ans

#Part 1
cards1 = deque(game_dict['1'])
cards2 = deque(game_dict['2'])
_,winning_cards = combat_player(cards1,cards2)
final_score = score_calc(winning_cards)
print(f"Part 1: {final_score}")

#Part 2
cards1 = deque(game_dict['1'])
cards2 = deque(game_dict['2'])
_,winning_cards = recursive_combat_player(cards1,cards2)
final_score = score_calc(winning_cards)
print(f"Part 2: {final_score}")