from deck import Deck
from player import Player


class Game():
    def __init__(self) -> None:
        self.deck = Deck()
        self.player = Player(self.deck)
        self.croupier = Player(self.deck)

    def start(self):
        self.deck.generator()
        self.deck.shuffle()
        self.player.get_card_to_hand()


game = Game()
game.start()
