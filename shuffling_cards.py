import random
import main

colors = ["♥️", "♦️", "♠️", "♣️"]

ranges = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

croupier = []

def number_of_people(people):
    list_of_persons = []
    for _ in range(people):
        list_of_persons.append([])
    return list_of_persons

def number_of_banks(people, bank):
    list_of_banks = []
    for _ in range(people):
        list_of_banks.append(bank)
    return list_of_banks


def deck_maker(croupier):
    for color in colors:
        for rang in ranges:
            card = f"{rang} {color}"
            croupier.append(card)
    return random.shuffle(croupier)