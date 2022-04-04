"""Module with class Card

    Returns:
        str/int: info about card
    """


class Card:
    """Class Card with color and figure"""

    def __init__(self, color, figure) -> None:
        self.color = color
        self.figure = figure

    def __repr__(self) -> str:
        return f'{self.color} {self.figure}'

    def get_color_name(self):
        """Method to get color name

        Returns:
            str: color name
        """
        color_name = list(self.color.keys())
        return color_name[0]

    def get_color_sign(self):
        """Method to get color sign

        Returns:
            str: color sign
        """
        color_sign = list(self.color.values())
        return color_sign[0]

    def get_figure_kind(self):
        """Method to get figure kind

        Returns:
            str: figure kind
        """
        figure_name = list(self.figure.keys())
        return figure_name[0]

    def get_figure_values(self):
        """Method to get figure value

        Returns:
            int: figure value
        """
        figure_value = list(self.figure.values())
        return figure_value[0]
