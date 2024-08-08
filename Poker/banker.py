

def raise_bet(table_bank, bank, money):
    if money <= bank:
        table_bank += money
        bank -= money
    else:
        print(f"You Can't do that! Your balance is {bank}")

    return table_bank, bank

def all_in(table_bank, bank):
    table_bank += bank
    
    return table_bank

def ante(table_bank, bank):
    if bank != 0 and bank > 50:
        table_bank += 5
        bank -= 5
    elif bank != 0 and bank < 50:
        table_bank += 1
        bank -= 1
    else:
        print("You poor bastard, make some money and then play with us!")

