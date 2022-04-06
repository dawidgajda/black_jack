from deck import Deck

deck = Deck()

deck.generator()


def test_length_deck():
    assert len(deck.deck) == 52


def test_length_deck_get_card():
    deck.get_card()
    assert len(deck.deck) == 51
