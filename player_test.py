from player import Player

player = Player()


def test_clear_point():
    player.card_point = [10, 8, 3]
    player.clear_point()
    assert len(player.card_point) == 0


def test_add_point():
    player.add_card_point(10)
    assert player.card_point[0] == 10
    assert len(player.card_point) == 1
