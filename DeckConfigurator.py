
class DeckConfigurator:
    def __init__(self):

        self._suits = ["Hearts", "Diamonds", "Clubs", "Spades", "Cats"]
        self._ranksValues = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10, "Ace": 1
        }

        self.build_card_dict()

    def build_card_dict(self):

        self._card_dict = {}
        for suit in self._suits:
            cardList = []
            for card in self._ranksValues:
                cardList.append(card)
            self._card_dict[suit] = cardList

    @property
    def suits(self):
        return self._suits

    @property
    def card_dict(self):
        return self._card_dict

    @property
    def ranksValues(self):
        return self._ranksValues

    @suits.setter
    def suits(self, suits):
        self._suits = suits
        self.build_card_dict()

    @ranksValues.setter
    def ranksValues(self, ranksValues):
        self._ranksValues = ranksValues
        self.build_card_dict()
