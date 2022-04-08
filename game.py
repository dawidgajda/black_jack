from deck import Deck
from player import Player


class Game():
    def __init__(self) -> None:
        self.deck = Deck()
        self.player = Player('Player', self.deck)
        self.croupier = Player('Croupier', self.deck)
        self.player_points = 0
        self.start()

    def start(self):
        self.deck.generator()
        self.deck.shuffle()
        self.player_points = self.player.get_two_card()
        self.croupier.croupier(self.player_points)


game = Game()
