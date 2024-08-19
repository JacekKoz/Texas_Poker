
user_bet = 0

def raise_bet(table_bank, bank, money, user_bet):
    if money <= bank:
        table_bank += money
        user_bet += money
        bank -= money
    else:
        print(f"You Can't do that! Your balance is {bank}")

    return table_bank, bank, user_bet

def big_blind(table_bank, bank):
    if bank >= 50 and bank != 0:
        table_bank += 10
        bank -= 10
    elif bank < 50 and bank != 0:
        table_bank += 5
        bank -= 5
    else:
        print("You poor bastard, make some money and then play with us! Get lost!")

def small_blind(table_bank, bank):
    if bank >= 50 and bank != 0:
        table_bank += 5
        bank -= 5
    elif bank < 50 and bank != 0:
        table_bank += 2
        bank -= 2
    else:
        print("You poor bastard, make some money and then play with us! Get lost!")

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