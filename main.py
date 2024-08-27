import shuffling_cards
import deal_cards
import banker

def main():
  
  table_bank: int = 0
  bank: int = 0
  people: int = 0

  while people <= 1:
    people = int(input("How many players are playing?(at least 2)\n"))
  while bank <= 9:
    bank = int(input("What is the starting money pool? (it cannot be less than 10$):\n")) 
  list_of_persons = shuffling_cards.number_of_people(people)
  list_of_banks = shuffling_cards.number_of_banks(people, bank)
  print(list_of_banks[i])
  shuffling_cards.deck_maker(shuffling_cards.croupier)
  deal_cards.dealing_cars(shuffling_cards.croupier, list_of_persons)
  deal_cards.flop(shuffling_cards.croupier)
  table_bank, bank, user_bet = banker.big_blind(table_bank, list_of_banks[i])
  table_bank, bank, user_bet = banker.small_blind(table_bank, list_of_banks[i], user_bet)

      #TODO W sumie nic nie zrobiłem ;c
  while True:
    for i in range(people):

      print(f"""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
      Cards on table: 
      {deal_cards.table}
      Your hand:
      {list_of_persons[i]}
      Your balance: 
      {list_of_banks[i]}$
      Table bank:
      {table_bank}$
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

      """)

      print("""
  ➖➖➖➖➖➖➖➖➖➖
          1. Raise
          2. Check
          3. All in baby!
          3. Fold
  ➖➖➖➖➖➖➖➖➖➖
          """)
      user_choice = int(input("Choose what do you want to do:\n"))

      if user_choice == 1:
          question_1 = input(f"Do you want raise more than {2 * banker.big_blind(user_bet, list_of_banks[i])} Y/N\n")

          if question_1 == "Y":
            money = int(input(f"How much money do you want to raise?\nYou currently have: {list_of_banks[i]}$\n"))
            table_bank, bank, user_bet = banker.raise_bet(table_bank, bank, money, user_bet)

          if question_1 == "N":
            money = 2 * banker.big_blind(user_bet)
            table_bank, bank, user_bet = banker.raise_bet(table_bank, bank, money, user_bet)
          else:
              print("You must select 'Y' or 'N'\n")

      elif user_choice == 2:
          break
    
      elif user_choice == 3:
          banker.all_in(table_bank, bank)

if __name__ == "__main__":
    main()
