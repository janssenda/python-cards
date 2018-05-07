

import VariableDeck
import DeckConfigurator

def Main():

    print ("")
    myDeck = VariableDeck.Deck(DeckConfigurator.DeckConfigurator())

    #myDeck.showAllCards()


    myDeck.shuffleDeck()
    #
    # print(len(myDeck.cards))
    myDeck.showCards(myDeck.drawCards(7))


if __name__ == '__main__':
    print()
    Main()



