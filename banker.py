
pot: int = 0

def pot_f(table_bank, pot):
    pot += table_bank
    table_bank = 0
    

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
    elif bank > 0:
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
    elif bank < 50:
        table_bank += 2
        bank -= 2
    else:
        print("You poor bastard, make some money and then play with us! Get lost!")
    
    return table_bank, bank, user_bet


def all_in(table_bank, bank):
    table_bank += bank
    bank = 0 
    
    return table_bank

# def ante(table_bank, bank, people):
#     if bank != 0 and bank > 50:
#         table_bank += (5 * people)
#         bank -= 5
#     elif bank != 0 and bank < 50:
#         table_bank += people
#         bank -= 1
#     else:
#         print("You poor bastard, make some money and then play with us!")

    return table_bank, bank

def fold(user_bet):
    #MOŻE COŚ WYMYŚLE
    print(f"You lost {user_bet}")