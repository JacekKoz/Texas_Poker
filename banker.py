
pot: int = 0

def pot_f(table_bank, pot):
    pot += table_bank
    table_bank = 0
    
    return pot

def raise_bet(table_bank, bank, money, user_bet):
    if money <= bank:
        table_bank += money
        user_bet += money
        bank -= money
    else:
        print(f"You Can't do that! Your balance is {bank}")

    return table_bank, bank, user_bet

def big_blind(table_bank, bank):
    if bank >= 50:
        user_bet: int = 10    
        table_bank += user_bet
        bank -= user_bet
    elif bank >= 5:
        user_bet: int = 5
        table_bank += user_bet
        bank -= user_bet
    else:
        user_bet = 0
        print("You poor bastard, make some money and then play with us! Get lost!")

    return table_bank, bank, user_bet

def small_blind(table_bank, bank, user_bet):
    if bank >= 50:
        table_bank += (user_bet / 2)
        bank -= (user_bet / 2)
    elif bank < 50 and bank > 0:
        table_bank += 2
        bank -= 2
    else:
        print("You poor bastard, make some money and then play with us! Get lost!")
    
    return table_bank, bank, user_bet


def all_in(table_bank, bank):
    table_bank += bank
    bank = 0 
    
    return table_bank, bank

def fold(user_bet):
    #MOŻE COŚ WYMYŚLE
    print(f"You lost {user_bet}")

def start(list_of_banks, people, table_bank, user_bet):
    for i in range(people):
        print(f"\nPlayer {i} is the big blind this round.")

        table_bank, list_of_banks[i], user_bet = big_blind(table_bank, list_of_banks[i])

        other_player = (i + 1) % 2
        table_bank, list_of_banks[other_player], user_bet = small_blind(table_bank, list_of_banks[other_player])
        print(f"Player {other_player} bank after small blind: {list_of_banks[other_player]}")