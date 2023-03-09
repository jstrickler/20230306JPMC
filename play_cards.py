from carddeck import CardDeck

d1 = CardDeck("Wanda")
#  CardDeck d1 = new CardDeck();
d2 = CardDeck("Vision")

print(f"d1: {d1}")

print(f"d1.dealer: {d1.dealer}")
print(f"d2.dealer: {d2.dealer}")

d1.shuffle()
print(f"d1.cards: {d1.cards}")
print()

d2.dealer = "Amy"

for i in range(5):
    card = d1.draw()
    print(f"card: {card}")

