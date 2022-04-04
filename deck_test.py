from Deck import Deck

deck = Deck()

deck.deck_generator()


def test_length_deck():
    assert len(deck.deck) == 52
