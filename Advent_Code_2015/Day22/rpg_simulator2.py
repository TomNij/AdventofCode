from itertools import combinations

shop = {
    'Weapons':{
    'Dagger':        [8,4,0],
    'Shortsword':   [10,5,0],
    'Warhammer'  :  [25,     6,       0],
    'Longsword'  :  [40 ,    7,      0],
    'Greataxe'   :  [74  ,   8,       0],
            },
    'Armor': {
    'Null'     : [0,     0,       0],
    'Leather'     : [13,     0,       1],
    'Chainmail'  :  [31,     0,       2],
    'Splintmail'  : [53,     0,       3],
    'Bandedmail' :  [75,     0,       4],
    'Platemail' :  [102,     0,       5]
            },
    'Rings': {
    'Null'     : [0,     0,       0],
    'Null2'     : [0,     0,       0],
    'Damage +1':   [25,     1,       0],
    'Damage +2' :  [50,      2,       0],
    'Damage +3'  : [100,     3,       0],
    'Defense +1'  : [20,     0,       1],
    'Defense +2'  : [40,     0,       2],
    'Defense +3'  : [80,     0,       3]}
}

boss = {'Health': 103,
'Damage': 9,
'Armor': 2}

player = {'Health': 100,
'Damage': 0,
'Armor': 0}

# requirements: 1 weapon, 0-1 armor, 0-2 rings
# try bossfight with increased spending
# for weapon in weapons
# for armor in armor
# for ring in rings + combination(rings,2)

def battle_win(boss,player):
    while True:
        #start with player attacks boss
        boss['Health'] -= max(1,player['Damage']-boss['Armor'])
        if boss['Health'] <= 0:
            return True #player wins
        # boss attacks player
        player['Health'] -= max(1, boss['Damage'] - player['Armor'])
        if player['Health'] <= 0:
            return False  # boss wins

min_cost = 99999999
max_cost = 0
for weapon in shop['Weapons']:
    weapon_price,weapon_dmg,_ = shop['Weapons'][weapon]
    for armor in shop['Armor']:
        armor_price,_, armor_armor = shop['Armor'][armor]
        for ring_combo in combinations(shop['Rings'],2):
            ring_price = sum([shop['Rings'][ring][0] for ring in ring_combo])
            ring_dmg = sum([shop['Rings'][ring][1] for ring in ring_combo])
            ring_armor = sum([shop['Rings'][ring][2] for ring in ring_combo])
            player['Damage'] = weapon_dmg + ring_dmg
            player['Armor'] = armor_armor + ring_armor
            total_cost = weapon_price + armor_price + ring_price
            player_battle = dict(player)
            boss_battle = dict(boss)
            if battle_win(boss_battle, player_battle):
                if total_cost < min_cost:
                    min_cost = total_cost
            else:
                if total_cost > max_cost:
                    max_cost = total_cost


print(f"Part 1: {min_cost}")
print(f"Part 2: {max_cost}")