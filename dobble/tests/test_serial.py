from dobble.generator import generate_deck
from dobble.helper import get_matches, get_matching_cards, matching_items
from unittest2 import TestCase


class SerialGeneratorTest(TestCase):
    def test_should_return_a_deck_of_1_for_degree_1(self):
        deck = generate_deck(1)
        self.assertEqual(deck, ((0,),))

    def test_should_return_the_correct_number_of_cards(self):
        for d in range(4):
            n = d - 1
            self.assertEqual(len(generate_deck(d)), n * n + n + 1)

    def test_should_return_cards_with_degree_symbols(self):
        for d in range(4):
            for card in generate_deck(d):
                self.assertEqual(len(card), d)

    def test_should_have_each_card_connected_to_every_other(self):
        for d in range(4):
            deck = generate_deck(d)
            for card in deck:
                every_other_card = set(deck)
                every_other_card.remove(card)
                for other_card in every_other_card:
                    self.assertIn(card, get_matching_cards(other_card, deck))

    def test_should_have_each_card_connected_to_every_other_with_one_symbol_exactly(self):
        for d in range(4):
            deck = generate_deck(d)
            for card in deck:
                every_other_card = set(deck)
                every_other_card.remove(card)
                for other_card in every_other_card:
                    self.assertEqual(len(matching_items(card, other_card)), 1)

    def test_should_return_correct_deck_for_degree_2(self):
        deck = generate_deck(2)
        deck2 = (
            (0, 1),
            (0, 2),
            (1, 2)
        )
        self.assertEqual(deck, deck2)
