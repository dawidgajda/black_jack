"""Module with class Deck

    Returns:
        list: shuffle deck
    """
from random import shuffle
from Card import Card


class Deck:
    """Class Deck with all colors and figure cards"""

    def __init__(self) -> None:
        self.colors = [{'CLUBS': '♣'}, {'DIAMONDS': '♦'},
                       {'HEARTS': '♥'}, {'SPADES': '♠'}]
        self.figures = [{'A': 10}, {'K': 10}, {'Q': 10}, {'J': 10},
                        {'10': 10}, {'9': 9}, {'8': 8}, {'7': 7},
                        {'6': 6}, {'5': 5}, {'4': 4}, {'3': 3}, {'2': 2}]

        self.deck = []

    def deck_generator(self):
        """Method to generate deck with all card"""
        for color in self.colors:
            for figure in self.figures:
                self.deck.append(Card(color, figure))

    def deck_shuffle(self):
        """Method to shuffle deck

        Returns:
            list: card objects instance
        """
        return shuffle(self.deck)
