"""Module with class Deck

    Returns:
        list: shuffle deck
    """
from random import shuffle
from card import Card


class Deck:
    """Class Deck with all colors and figure cards"""

    def __init__(self) -> None:
        self.colors = [{'CLUBS': '♣'}, {'DIAMONDS': '♦'},
                       {'HEARTS': '♥'}, {'SPADES': '♠'}]
        self.figures = [{'A': 1}, {'K': 10}, {'Q': 10}, {'J': 10},
                        {'10': 10}, {'9': 9}, {'8': 8}, {'7': 7},
                        {'6': 6}, {'5': 5}, {'4': 4}, {'3': 3}, {'2': 2}]

        self.deck = []

    def generator(self):
        """Method to generate deck with all card"""

        for color in self.colors:
            for figure in self.figures:
                temp_list = []
                temp_list.append(Card(color, figure))
                self.deck.append(temp_list)

    def shuffle(self):
        """Method to shuffle deck

        Returns:
            list: card objects instance
        """
        return shuffle(self.deck)

    def get_card(self):
        """Method to get and remove one card in deck

        Returns:
            Object: One object card
        """
        try:
            card = self.deck.pop(-1)
        except IndexError:
            print('Deck is empty')
        return card[0]
