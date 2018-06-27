import unittest

from card import Card
from deck import Deck, Hand


class TestCardGame(unittest.TestCase):
    def test_card(self):
        # Create a ace of clubs
        card = Card(card_rank='two', card_suite='clubs')

        # Ensure that this is an ace of clubs
        # Examples of other cards are:
        # two of diamonds
        # king of spades
        card_name = card.get_name()
        expected_card_name = 'two of clubs'
        self.assertEqual(card_name, expected_card_name)

    def test_ace_card(self):
        # Create a ace of clubs
        card = Card(card_rank='ace', card_suite='diamonds')

        card_name = card.get_name()
        expected_card_name = 'ace of diamonds'
        self.assertEqual(card_name, expected_card_name)

    def test_face_card(self):
        # Create a ace of clubs
        card = Card(card_rank='king', card_suite='hearts')

        card_name = card.get_name()
        expected_card_name = 'king of hearts'
        self.assertEqual(card_name, expected_card_name)

    def test_deck(self):
        # Create a deck of cards
        deck = Deck()

        # Ensure the deck contains 52 cards
        self.assertEqual(deck.get_number_of_cards(), 52)

    def test_deck_pick(self):
        # Create a deck of cards
        deck = Deck()

        # Ensure the deck contains 52 cards
        self.assertEqual(deck.get_number_of_cards(), 52)

        # Pick 5 card from the deck
        deck.pick(1)

        # Check that 47 cards are remaining in the deck
        self.assertEqual(deck.get_number_of_cards(), 51)

    def test_pick_hand(self):
        # Create a deck of cards
        deck = Deck()

        # Create a hand by picking 5 cards from the deck
        hand = Hand(deck.pick(5))

        # Ensure the deck contains 47 cards
        self.assertEqual(deck.get_number_of_cards(), 47)

        # Ensure the hand contains 5 cards
        self.assertEqual(hand.get_number_of_cards(), 5)

    def test_hand_rank(self):
        # Create a flush hand, where 5 cards are of the same suite
        hand = Hand(cards=[
            Card(card_rank='two', card_suite='spades'),
            Card(card_rank='five', card_suite='spades'),
            Card(card_rank='seven', card_suite='spades'),
            Card(card_rank='king', card_suite='spades'),
            Card(card_rank='queen', card_suite='spades'),
        ])

        hand_rank = hand.get_rank()
        self.assertEqual(hand_rank, 'flush')

        # Create a 3 of a kind hand
        hand = Hand(cards=[
            Card(card_rank='five', card_suite='spades'),
            Card(card_rank='five', card_suite='hearts'),
            Card(card_rank='king', card_suite='diamonds'),
            Card(card_rank='five', card_suite='clubs'),
            Card(card_rank='queen', card_suite='spades'),
        ])
        hand_rank = hand.get_rank()
        self.assertEqual(hand_rank, '3 of a kind')

        # Create a straight hand
        hand = Hand(cards=[
            Card(card_rank='five', card_suite='spades'),
            Card(card_rank='six', card_suite='hearts'),
            Card(card_rank='seven', card_suite='diamonds'),
            Card(card_rank='eight', card_suite='clubs'),
            Card(card_rank='nine', card_suite='spades'),
        ])
        hand_rank = hand.get_rank()
        self.assertEqual(hand_rank, 'straight')

        # Create a full house
        hand = Hand(cards=[
            Card(card_rank='king', card_suite='spades'),
            Card(card_rank='king', card_suite='hearts'),
            Card(card_rank='king', card_suite='diamonds'),
            Card(card_rank='five', card_suite='clubs'),
            Card(card_rank='five', card_suite='spades'),
        ])
        hand_rank = hand.get_rank()
        self.assertEqual(hand_rank, 'full house')
        # Create a straight flush
        hand = Hand(cards=[
            Card(card_rank='five', card_suite='clubs'),
            Card(card_rank='six', card_suite='clubs'),
            Card(card_rank='seven', card_suite='clubs'),
            Card(card_rank='eight', card_suite='clubs'),
            Card(card_rank='nine', card_suite='clubs'),
        ])
        hand_rank = hand.get_rank()
        self.assertEqual(hand_rank, 'straight flush')

        # Create a royal flush
        hand = Hand(cards=[
            Card(card_rank='ace', card_suite='clubs'),
            Card(card_rank='king', card_suite='clubs'),
            Card(card_rank='queen', card_suite='clubs'),
            Card(card_rank='jack', card_suite='clubs'),
            Card(card_rank='ten', card_suite='clubs'),
        ])
        hand_rank = hand.get_rank()
        self.assertEqual(hand_rank, 'royal flush')

        # Create a royal 1 pair hand
        hand = Hand(cards=[
            Card(card_rank='ace', card_suite='clubs'),
            Card(card_rank='ace', card_suite='spades'),
            Card(card_rank='queen', card_suite='hearts'),
            Card(card_rank='jack', card_suite='spades'),
            Card(card_rank='ten', card_suite='clubs'),
        ])
        hand_rank = hand.get_rank()
        self.assertEqual(hand_rank, '1 pair')

    def test_compare_hand_ranks(self):
        flush = Hand(cards=[
            Card(card_rank='two', card_suite='spades'),
            Card(card_rank='five', card_suite='spades'),
            Card(card_rank='seven', card_suite='spades'),
            Card(card_rank='king', card_suite='spades'),
            Card(card_rank='queen', card_suite='spades'),
        ])

        two_pair = Hand(cards=[
            Card(card_rank='five', card_suite='spades'),
            Card(card_rank='five', card_suite='hearts'),
            Card(card_rank='seven', card_suite='spades'),
            Card(card_rank='seven', card_suite='diamonds'),
            Card(card_rank='queen', card_suite='spades'),
        ])
        # Using < or > should allow for hands to be compared based on rank
        self.assertEqual(two_pair < flush, True)





if __name__ == '__main__':
    unittest.main()
