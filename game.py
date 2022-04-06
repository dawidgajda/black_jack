from deck import Deck
from player import Player


class Game():
    def __init__(self) -> None:
        self.deck = Deck()
        self.player1 = Player()
        self.player2 = Player()

    def start(self):
        self.deck.generator()
        self.deck.shuffle()

    def get_card_to_hand(self):
        card = self.deck.get_card()
        card_repr = f'{card.get_figure_kind()} {card.get_color_sign()}'
        print(f'Your card {card_repr}')
        self.player1.add_card_point(card.get_figure_values())
        return card_repr
