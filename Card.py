class Card:

    def __init__(self, color, figure) -> None:
        self.color = color
        self.figure = figure

    def __repr__(self) -> str:
        return f'{self.color} {self.figure}'

    def get_color_name(self):
        color_name = list(self.color.keys())
        return color_name[0]

    def get_color_sign(self):
        color_sign = list(self.color.values())
        return color_sign[0]

    def get_figure_name(self):
        figure_name = list(self.figure.keys())
        return figure_name[0]

    def get_figure_values(self):
        figure_value = list(self.figure.values())
        return figure_value[0]
