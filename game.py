from deck import Deck
from player import Player


class Game():
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.generator()
        self.deck.shuffle()
        self.player = Player('Player', self.deck)
        self.croupier = Player('Croupier', self.deck)
        self.player_draw_cards = []
        self.croupier_draw_cards = []
        self.player_win = 0
        self.croupier_win = 0
        self.start()

    def start(self):

        self.player_draw_cards = self.player.get_two_card()
        self.player_win = self.check_cards('Player', self.player_draw_cards)
        self.croupier_win = self.croupier_start()
        self.next_game()

    def next_game(self):
        next_game = input('Next game? [Y]es or [N]o: ')
        print('----------'*10)
        if next_game.upper() == 'Y':
            self.player.clear_draw_cards()
            self.croupier.clear_draw_cards()
            self.player_win = 0
            self.croupier_win = 0
            self.start()
        elif next_game.upper() == 'N':
            print('Game finished!')
        else:
            print('Wrong choice')
            self.next_game()

    def check_cards(self, who, who_points):
        cards = 0
        for card, _ in who_points:
            if card in ['A', 'K', 'Q', 'J']:
                cards += 1
        if cards == 2:
            print(f'{who} win!')
            return 1
        elif who == self.player.name:
            self.player.next_card_to_hand()

        return 0

    def scored_points(self, who_points):
        points = 0
        for _, point in who_points:
            points += point
        return points

    def croupier_start(self):
        if self.player_win == 0:
            if self.scored_points(self.player_draw_cards) < 21:
                self.croupier_draw_cards = self.croupier.get_two_card()
                self.check_cards('Croupier', self.croupier_draw_cards)

        while self.croupier_win == 0 and self.player_win == 0 and self.scored_points(self.player_draw_cards) < 21:
            if self.scored_points(self.croupier_draw_cards) > self.scored_points(self.player_draw_cards) and self.scored_points(self.croupier_draw_cards) <= 21:
                print('Croupier win!')
                self.croupier_win = 1
                return 1
            elif self.scored_points(self.croupier_draw_cards) > 21:
                print('Player win!')
                self.croupier_win = -1
                return -1
            elif self.scored_points(self.croupier_draw_cards) == self.scored_points(self.player_draw_cards):
                print('Draw!')
                self.croupier_win = 1
                return 1
            elif self.scored_points(self.croupier_draw_cards) < self.scored_points(self.player_draw_cards):
                self.croupier.get_card_to_hand()


game = Game()
