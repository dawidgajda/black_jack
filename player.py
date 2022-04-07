"""Module with class Player"""


class Player:
    """Class Player"""

    def __init__(self, deck) -> None:
        self.card_point = []
        self.deck = deck

    def clear_point(self):
        """Function to clear list with player points"""
        self.card_point = []

    def add_card_point(self, card_value):
        """Function to add player points to list"""
        self.card_point.append(card_value)

    def get_card_to_hand(self):
        card = self.deck.get_card()
        card_repr = f'{card.get_figure_kind()} {card.get_color_sign()}'
        print(f'Your draw card {card_repr}')
        self.add_card_point(card.get_figure_values())
        print(f'Sum points {sum(self.card_point)}')
        self.next_card_to_hand()

    def next_card_to_hand(self):
        next_card = input("Do you have next card? [Y]es or [N]o:")
        # while next_card.upper() != 'N':
        if next_card.upper() == 'Y':
            self.get_card_to_hand()
        elif next_card.upper() == 'N':
            self.croupier()
        else:
            print('Wrong choice')
            self.next_card_to_hand()

    def croupier(self):
        print('Croupier')
