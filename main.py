import shuffling_cards
import deal_cards
import banker

def main():
  table_bank = 0

  bank = 0
  people = 0
  while people <= 1:
      people = int(input("How many players are playing?(at least 2)\n"))
  while bank <= 9:
      bank = int(input("What is the starting money pool? (it cannot be less than 10$):\n"))

  list_of_persons = shuffling_cards.number_of_people(people)
  shuffling_cards.deck_maker(shuffling_cards.croupier)
  deal_cards.dealing_cars(shuffling_cards.croupier, list_of_persons)
  deal_cards.flop(shuffling_cards.croupier)

  while True:

      print(f"""
 ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
      Cards on table: 
      {deal_cards.table}
      Your hand:
      {list_of_persons[0]}
      Your balance: 
      {bank}$
      Table bank:
      {table_bank}$
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

      """)

      print("""
  ➖➖➖➖➖➖➖➖➖➖
          1. Raise
          2. Call
          3. All in baby!
          3. Fold
  ➖➖➖➖➖➖➖➖➖➖
          """)

      user_choice = int(input("Choose what do you want to do:\n"))

      if user_choice == 1:
          money = int(input(f"How much money do you want to raise?\nYou currently have: {bank}$\n"))
          table_bank, bank = banker.raise_bet(table_bank, bank, money)
      # TODO: Przetestować opcje "Call" 
      if user_choice == 2:
          try:
            if money > bank:
                x = int(input("Yo dont't have enough money! Do you want to go all in?\n1. Yes\n2. No"))
                if x == 1:
                  banker.all_in()
                else:
                    print(f"You tried hard but you lost! \nYou have {bank}$")
                    break
            else:
                table_bank, bank = banker.raise_bet(table_bank, bank, money)
                deal_cards.turn_river(shuffling_cards.croupier)
          except:
              print("Nie możesz sprawdzić kiedy m")

      if user_choice == 3:
          banker.all_in(table_bank, bank)

if __name__ == "__main__":
    main()
