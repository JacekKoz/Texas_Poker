import random

colors = ["♥️", "♦️", "♠️", "♣️"]
ranges = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.hand = []

    def add_cards(self, card):
        self.hand.append(card)

    def __str__(self):
        return f"Player: {self.name}, Bank: {self.bank}, Hand: {', '.join(self.hand)}"
        
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

# Tworzenie croupiera i graczy
croupier = Croupier(colors, ranges)
players = create_a_player(4, 1000)

# Rozdawanie dwóch kart
croupier.dealing_two_cards(players)

# Wyświetlenie graczy
for player in players:
    print(player)
