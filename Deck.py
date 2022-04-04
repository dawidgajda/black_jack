from random import shuffle
from Card import Card


class Deck():
    def __init__(self) -> None:
        self.colors = [{'CLUBS': '♣'}, {'DIAMONDS': '♦'},
                       {'HEARTS': '♥'}, {'SPADES': '♠'}]
        self.figures = [{'A': 10}, {'K': 10}, {'Q': 10}, {'J': 10}, {'10': 10},
                        {'9': 9}, {'8': 8}, {'7': 7}, {'6': 6}, {'5': 5}, {'4': 4}, {'3': 3}, {'2': 2}]

        self.deck = []

    def deck_generator(self):
        for color in self.colors:
            for figure in self.figures:
                self.deck.append(Card(color, figure))

    def deck_shuffle(self):
        return shuffle(self.deck)


deck = Deck()
deck.deck_generator()
deck.deck_shuffle()
