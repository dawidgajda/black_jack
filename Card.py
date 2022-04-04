class Card():
    def __init__(self, color, figure) -> None:
        self.color = color
        self.figure = figure

    def __repr__(self) -> str:
        return f'{self.color} {self.figure}'
