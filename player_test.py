from player import Player

player = Player('Player', [])


def test_clear_point():
    player.draw_cards = [('A', 1), ('K', 10), ('2', 2)]
    player.clear_draw_cards()
    assert len(player.draw_cards) == 0


def test_add_point():
    player.draw_cards = [('A', 1), ('K', 10), ('2', 2)]
    assert player.sum_points_in_game() == 13
