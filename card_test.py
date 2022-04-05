from card import Card

card = Card({'CLUBS': '♣'}, {'A': 10})


def test_color_name():
    assert card.get_color_name() == 'CLUBS'


def test_color_sign():
    assert card.get_color_sign() == '♣'


def test_figure_kind():
    assert card.get_figure_kind() == 'A'


def test_figure_value():
    assert card.get_figure_values() == 10
