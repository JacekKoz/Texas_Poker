
table = []

def dealing_cars(croupier, list_of_persons):
    for person in list_of_persons:
        for i in range(2):
            person.append(croupier.pop())


def flop(croupier):
    for i in range(3):
        table.append(croupier.pop())


def turn_river(croupier):
    table.append(croupier.pop())