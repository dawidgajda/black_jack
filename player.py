"""Module with class Player"""


class Player:
    """Class Player"""

    def __init__(self, name, deck) -> None:
        self.name = name
        self.card_point = []
        self.deck = deck

    def clear_point(self):
        """Method to clear list with player points"""
        self.card_point = []

    def add_card_point(self, card_value):
        """Method to add player points to list"""
        self.card_point.append(card_value)

    def get_two_card(self):
        """Method to drawing two cards by player

        Returns:
            int: sum of points with drawn cards
        """
        self.get_card_to_hand()
        self.get_card_to_hand()
        return self.sum_points_in_game()

    def get_card_to_hand(self):
        """Method to drawing next card"""
        card = self.deck.get_card()
        card_repr = f'{card.get_figure_kind()} {card.get_color_sign()}'
        print(f'{self.name} draw card {card_repr}')
        self.add_card_point(card.get_figure_values())
        print(f'Sum points {self.name} {self.sum_points_in_game()}')
        if len(self.card_point) >= 2 and self.name != 'Croupier':
            self.next_card_to_hand()

    def next_card_to_hand(self):
        """question about draw next card"""
        next_card = input("Do you have next card? [Y]es or [N]o:")
        if next_card.upper() == 'Y':
            self.get_card_to_hand()
        elif next_card.upper() == 'N':
            print('Croupier turn')
        else:
            print('Wrong choice')
            self.next_card_to_hand()

    def sum_points_in_game(self):
        """Method to return sum of points with drawn cards

        Returns:
            int: sum of points with drawn cards
        """
        return sum(self.card_point)

    def croupier(self, points):
        player_points = points
        self.get_two_card()
