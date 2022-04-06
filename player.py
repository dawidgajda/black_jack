class Player:
    def __init__(self) -> None:
        self.card_point = []

    def clear_point(self):
        self.card_point = []

    def add_card_point(self, card_value):
        self.card_point.append(card_value)
