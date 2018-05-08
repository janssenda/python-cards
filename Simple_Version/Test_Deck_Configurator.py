
import unittest
import DeckConfigurator
import mock
from mock.mock import patch



class Test_Deck_Configurator(unittest.TestCase):

    @patch('six.moves.builtins.open')
    @patch('yaml.load')
    @patch('os.path.isfile')
    def test_read_yml(self, mock_isfile, mock_yaml, mock_open):
        control_card_dict = {
            "Hearts": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
            "Diamonds": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
            "Spades": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
            "Clubs": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        }

        control_ranksValues = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10, "Ace": 1
        }

        cfg = DeckConfigurator.DeckConfigurator()

        # Test read_yml's ability to correctly read in and construct the card_dict and ranksValues fields
        # We return mock data from yaml.load, and compare the resulting fields to the controls, which
        # define what they should look like.
        mock_isfile.return_value = True
        mocked_open = mock_open('test')
        mocked_open_name = '%s.open' % __name__
        with patch(mocked_open_name, mocked_open, create=True):
            mock_yaml.return_value = {'Card_Layout':
                                          {'Hearts': 'Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King',
                                           'Diamonds': 'Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King',
                                           'Spades': 'Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King',
                                           'Clubs': 'Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King'},
                                      'Card_Values': {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                                                      '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}}

            cfg.read_yml("test")

        assert cfg.card_dict == control_card_dict
        assert cfg.ranksValues == control_ranksValues



