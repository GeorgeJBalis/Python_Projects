# This is an exercise on oop, we create a Deck of cards, with 52 combinations of suits and values

import random


class Card:
    valid_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    valid_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [
            Card(suit, value)
            for suit in Card.valid_suits
            for value in Card.valid_values
        ]

    def _deal(self, num):
        """Deals the amount of cards we specify as long that number is less or equal to the cards
        left on the deck, else it raises an error"""
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        count = min(len(self.cards), num)
        dealt_cards = self.cards[-count:]
        self.cards = self.cards[:-count]
        return dealt_cards

    def count(self):
        return len(self.cards)

    def shuffle(self):
        """rearranges the deck if no cards are mising"""
        if len(self.cards) != 52:
            raise ValueError("Only full decks can be shuffled")
        return random.shuffle(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def deal_card(self):
        return self._deal(1)[
            0
        ]  # indexing 0 because the method _deal returns a single item list that we want to retrieve

    def deal_hand(self, num):
        return self._deal(num)
