import random

# Tworzymy talię kart
def stworz_talie():
    kolory = ['♥', '♦', '♣', '♠']
    wartosci = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    talia = [(wartosc, kolor) for wartosc in wartosci for kolor in kolory]
    random.shuffle(talia)
    return talia

# Rozdanie kart graczom
def rozdanie_kart(talia):
    gracz1 = [talia.pop() for _ in range(2)]
    gracz2 = [talia.pop() for _ in range(2)]
    return gracz1, gracz2

# Flop - wyłożenie 3 kart wspólnych
def flop(talia):
    karty_wspolne = [talia.pop() for _ in range(3)]
    return karty_wspolne

# Turn - wyłożenie 4 karty wspólnej
def turn(talia, karty_wspolne):
    karty_wspolne.append(talia.pop())
    return karty_wspolne

# River - wyłożenie 5 karty wspólnej
def river(talia, karty_wspolne):
    karty_wspolne.append(talia.pop())
    return karty_wspolne

# Symulacja jednej rundy
def runda_poker():
    talia = stworz_talie()
    gracz1, gracz2 = rozdanie_kart(talia)
    
    print("Karty gracza 1:", gracz1)
    print("Karty gracza 2:", gracz2)
    
    karty_wspolne = flop(talia)
    print("\nFlop:", karty_wspolne)
    
    karty_wspolne = turn(talia, karty_wspolne)
    print("Turn:", karty_wspolne)
    
    karty_wspolne = river(talia, karty_wspolne)
    print("River:", karty_wspolne)

# Symulacja kilku rund
def symuluj_rundy(ilosc_rund):
    for runda in range(1, ilosc_rund + 1):
        print(f"\nRunda {runda}:")
        runda_poker()

# Przykład użycia: symulacja 3 rund
symuluj_rundy(3)

