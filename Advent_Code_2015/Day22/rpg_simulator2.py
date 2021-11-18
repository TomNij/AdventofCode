from itertools import combinations

spells = {
    'Magic Missile':{
        'Damage':   4,
        'Cost'  :  53,
        'Healing' : 0,
        'Turns': 0,
        'Armor': 0},
    'Drain':{
        'Damage':   4,
        'Cost'  :  53,
        'Healing' : 2},
        'Turns': 0,
        'Armor': 0},
    'Shield':{
        'Damage':   4,
        'Cost'  :  113,
        'Healing' : 0,
        'Turns': 0,
        'Armor': 7},
    'Recharge':{
        'Damage':   0,
        'Cost'  :  229,
        'Healing' : 0,
        'Turns': 5,
        'Mana_regen':101},
    'Poison':{
        'Damage': 3,
        'Cost': 173,
        'Healing': 0,
        'Turns': 6,
        'Armor': 0}
            }

}

boss = {'Health': 51,
'Damage': 9}

player = {'Health': 50,
'Mana': 500,
'Armor':0}



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