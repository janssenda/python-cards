

from random import shuffle
import Card
import copy


class Deck:

    def __init__(self, numDecks = 1):
        if numDecks <= 0 or not isinstance(numDecks, int):
            raise ValueError("Error - Deck size must be a positive integer")
        self._isShuffled = False
        self._cards = []
        self._numDecks = numDecks
        self._suits = ["Hearts","Diamonds","Clubs","Spades"]
        self.constructDeck()

    def setRank(self, x):
        return {
            0: "Ace",
            10: "Jack",
            11: "Queen",
            12: "King"
        }.get(x, str(x + 1))

    def constructDeck(self):
        self._cards.clear()

        for k in range(self._numDecks):
            for j in range(4):
                for i in range(13):
                    c = Card.Card()

                    if (i > 9):
                        c.value = 10
                    else:
                        c.value = i + 1

                    c.rank = self.setRank(i)
                    c.suit = self._suits[j]
                    self._cards.append(c)

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
        print("%s %s" % (c.rank, c.suit))

    def showCards(self, cardlist):
        for c in cardlist:
            self.showCard(c)

    def showAllCards(self):
        for index, c in enumerate(self._cards):
            self.showCard(self._cards[index])



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