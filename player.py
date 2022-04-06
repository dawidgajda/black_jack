"""Module with class Player"""


class Player:
    """Class Player"""

    def __init__(self) -> None:
        self.card_point = []

    def clear_point(self):
        """Function to clear list with player points"""
        self.card_point = []

    def add_card_point(self, card_value):
        """Function to add player points to list"""
        self.card_point.append(card_value)
