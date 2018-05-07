

from random import shuffle
import Card
import copy
class Deck:

    def __init__(self, deckConfig, numDecks = 1):
        if numDecks <= 0 or not isinstance(numDecks, int):
            raise ValueError("Error - Deck size must be a positive integer")

        self._isShuffled = False
        self._cards = []
        self._numDecks = numDecks
        self._card_dict = deckConfig.card_dict
        self._ranksValues = deckConfig.ranksValues

        self.constructDeck()


    def constructDeck(self):
        self._cards.clear()
        for k in range(self._numDecks):
            for suit in self.card_dict:
                for card in self._card_dict[suit]:
                    self._cards.append(Card.Card(
                            self._ranksValues[card], card, suit
                    ))

    def shuffleDeck(self):
        shuffle(self._cards)
        self._isShuffled = True

    def drawCards(self, num = 1):
        if num <= 0 or not isinstance(num, int):
            raise ValueError("Error - Number must be a positive integer")

        draw = []
        if len(self._cards) >= num:
            for i in range(num):
                draw.append(self._cards.pop())
            return draw
        else:
            raise EmptyDeckException("Not cards remaining...")

    def peek(self, num):
        return copy.deepcopy(self._cards[:num])

    def showCard(self, c):
        print("%s %s, value: %s" % (c.rank, c.suit, c.value))

    def showCards(self, cardlist):
        for c in cardlist:
            self.showCard(c)

    def showAllCards(self):
        for index, c in enumerate(self._cards):
            self.showCard(self._cards[index])

    @property
    def card_dict(self):
        return self._card_dict
    @property
    def cards(self):
        return self._cards

    @property
    def isShuffled(self):
        return self._isShuffled

    @isShuffled.setter
    def isShuffled(self, isShuffled):
        self._isShuffled = isShuffled

    @property
    def cardsRemaining(self):
        return len(self._cards)

    @property
    def numDecks(self):
        return self._numDecks

    @numDecks.setter
    def numDecks(self, numDecks):
        self._numDecks = numDecks
        self.constructDeck()

class EmptyDeckException(Exception):
    pass