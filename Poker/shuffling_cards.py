import random

colors = ["♥️", "♦️", "♠️", "♣️"]

ranges = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

croupier = []

def number_of_people(people):
    list_of_persons = []
    for i in range(people):
        list_of_persons.append([])
    return list_of_persons


def deck_maker(croupier):
    for color in colors:
        for rang in ranges:
            card = f"{rang} {color}"
            croupier.append(card)
    return random.shuffle(croupier)