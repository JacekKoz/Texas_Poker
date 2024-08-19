
user_bet = 0

def raise_bet(table_bank, bank, money, user_bet):
    if money <= bank:
        table_bank += money
        user_bet += money
        bank -= money
        print(f"NALICZANIE ILE POSTAWIŁ UŻYTKOENIK = {table_bank}")
    else:
        print(f"You Can't do that! Your balance is {bank}")

    return table_bank, bank, user_bet


