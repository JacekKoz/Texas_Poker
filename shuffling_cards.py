import random
import main

colors = ["♥️", "♦️", "♠️", "♣️"]

ranges = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.hand = []

    def add_cards(self, card):
        self.hand.append(card)

    def __str__(self) -> str:
        return f"Player: {self.name}, Bank: {self.bank}, Hand: {','.join(self.hand)}"
        

class Croupier:
    def __init__(self, colors, ranges):
        self.deck = [f"{range} {color}" for color in colors for range in ranges]
        random.shuffle(self.deck)

    def deal_the_card(self, player):
        if self.deck:
            player.add_cards(self.deck.pop())

    def dealing_two_cards(self, players):
        print("START")
        for player in players:
            self.deal_the_card(player)
            self.deal_the_card(player)
        print("STOP")

    
def create_a_player(people, bank):
    return [Player(f"Player {i + 1}", bank) for i in range(people)]

croupier = Croupier(colors, ranges)
players = create_a_player(4, 1000)

croupier.dealing_two_cards(players)

for player in players:
    print(player)

    
    


























# croupier = []

# def number_of_people(people):
#     list_of_persons = []
#     for _ in range(people):
#         list_of_persons.append([])
#     return list_of_persons

# def number_of_banks(people, bank):
#     list_of_banks = []
#     for _ in range(people):
#         list_of_banks.append(bank)
#     return list_of_banks


# def deck_maker(croupier):
#     for color in colors:
#         for rang in ranges:
#             card = f"{rang} {color}"
#             croupier.append(card)
#     return random.shuffle(croupier)