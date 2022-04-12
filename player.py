"""Module with class Player"""


class Player:
    """Class Player"""

    def __init__(self, name, deck) -> None:
        self.name = name
        self.draw_cards = []
        self.deck = deck

    def clear_draw_cards(self):
        """Method to clear list with player points"""
        self.draw_cards = []

    def card_repr(self, card):
        """_summary_

        Args:
            card object: object class Card

        Returns:
            str: repr card
        """
        return f'{card.get_figure_kind()} {card.get_color_sign()}'

    def get_two_card(self):
        """Method to drawing two cards by player

        Returns:
            tuple in list: draw cards
        """
        num = 0
        while num < 2:
            self.get_card_to_hand()
            num += 1
        return self.draw_cards

    def get_card_to_hand(self):
        """Method to drawing next card

        Returns:
            tuple: draw card - kind adn value
        """
        card = self.deck.get_card()
        draw_card = (card.get_figure_kind(), card.get_figure_values())
        self.draw_cards.append(
            (card.get_figure_kind(), card.get_figure_values()))
        print(f'{self.name} draw card {self.card_repr(card)}')
        return draw_card

    def next_card_to_hand(self):
        """Method to draw next card

        Returns:
            str: who have 21 points
        """
        print(f'{self.name} {self.sum_points_in_game()} points')
        next_card = input("Do you have next card? [Y]es or [N]o:")
        if next_card.upper() == 'Y':
            self.get_card_to_hand()
            if self.sum_points_in_game() > 21:
                return print(f'{self.name} lost!')
            elif self.sum_points_in_game() == 21:
                return print(f'{self.name} win!')
            self.next_card_to_hand()
        elif next_card.upper() == 'N':
            print('Croupier turn')
        else:
            print('Wrong choice')
            self.next_card_to_hand()

    def sum_points_in_game(self):
        """_summary_

        Returns:
            int: scored points in game
        """
        points_in_game = 0
        for _, point in self.draw_cards:
            points_in_game += point
        return points_in_game
