import random

class CardDeck:  # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()


    def __str__(self):
        return "CardDeck"


    def __init__(self, dealer):
        self._dealer = dealer
        self._build_deck()


    def _build_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards


    @property   # getter
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("dealer must be a string")