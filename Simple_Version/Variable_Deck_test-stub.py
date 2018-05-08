import pytest
import unittest
import VariableDeck
import copy
import DeckConfigurator
import mock

@pytest.fixture()
def deckConfig():
    config = DeckConfigurator.DeckConfigurator()
    config.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    config.ranksValues = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10, "Ace": 1
        }
    return config

class VariableDeck_test(unittest.TestCase):

    # @pytest.mark.usefixtures("deckConfig")
    def test_deck_size(self):

        # Test single deck size
        myDeck = VariableDeck.Deck(deckConfig())
        assert myDeck.cardsRemaining == 52

        # Test multiple deck size
        myDeck = VariableDeck.Deck(deckConfig(),3)
        assert myDeck.cardsRemaining == 156

        # Try to use a zero deck size
        try:
            VariableDeck.Deck(deckConfig(),0)
            pytest.fail()
        except ValueError:
            pass

        # Try to use a negative deck size
        try:
            VariableDeck.Deck(deckConfig(),-1)
            pytest.fail()
        except ValueError:
            pass

        # Try to use a non-integer deck size
        try:
            VariableDeck.Deck(deckConfig(),3.5)
            pytest.fail()
        except ValueError:
            pass


    def test_construct_deck(self):

        # If the deck is valid, it should have 4 suites, each with a full range of ranks
        # We will construct a deck and compare its contents to a dictionary that defines
        # what it should look like

        myDeck = VariableDeck.Deck(deckConfig())
        card_dict = myDeck.card_dict

        myDeck.shuffleDeck()

        # Make sure the deck starts with 52 cards
        assert myDeck.cardsRemaining == 52

        # Test for duplicate cards
        count = dict((i, myDeck.cards.count(i)) for i in myDeck.cards)
        for counts in count:
            if count[counts] > 1:
                pytest.fail("Duplicate cards detected")

        # Compare each card to the dictionary, and remove the entry there is a match
        for card in myDeck.cards:
            if card.rank in card_dict[card.suit]:
                card_dict[card.suit].remove(card.rank)

        # The dictionary should shink to zero when all cards have been tested
        remainder = 0
        for suit in card_dict:
            remainder += len(card_dict[suit])

        assert  remainder == 0

    def test_shuffle_deck(self):

        myDeck = VariableDeck.Deck(deckConfig())

        # Shuffle once
        cardsInitial = copy.deepcopy(myDeck.cards)
        myDeck.shuffleDeck()
        assert cardsInitial != myDeck.cards

        # Shuffle again
        cardsInitial = copy.deepcopy(myDeck.cards)
        myDeck.shuffleDeck()
        assert cardsInitial != myDeck.cards


    def test_draw_cards(self):

        myDeck = VariableDeck.Deck(deckConfig())

        testHand = myDeck.drawCards(5)

        assert len(testHand) == 5
        assert myDeck.cardsRemaining == 47

        # Exhaust the deck
        try:
            myDeck.drawCards(50)
            pytest.fail("Cards should have run out")
        except VariableDeck.EmptyDeckException:
            pass







