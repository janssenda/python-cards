



class Card:

    def __init__(self):
        self._value = None
        self._suit = None
        self._rank = None



    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank



    @value.setter
    def value(self, value):
        self._value = value

    @suit.setter
    def suit(self, suit):
        self._suit = suit

    @rank.setter
    def rank(self, rank):
        self._rank = rank