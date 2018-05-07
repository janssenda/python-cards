
import yaml

class DeckConfigurator:
    def __init__(self):
        self._ranksValues = {}
        self._card_dict = {}
       # self.read_yml("card_config.yml")


    def read_yml(self, filename):
        with open(filename, 'r') as stream:
            try:
                card_data = yaml.load(stream)

                for d in card_data['Card_Layout']:
                    card_row = [x.strip() for x in card_data['Card_Layout'][d].split(',')]
                    self._card_dict[str(d).strip()] = card_row

                for v in card_data['Card_Values']:
                    self._ranksValues[str(v).strip()] = int(card_data['Card_Values'][v])

            except yaml.YAMLError as exc:
                print(exc)


    @property
    def card_dict(self):
        return self._card_dict

    @property
    def ranksValues(self):
        return self._ranksValues

    @ranksValues.setter
    def ranksValues(self, ranksValues):
        self._ranksValues = ranksValues

    @card_dict.setter
    def card_dict(self, card_dict):
        self._card_dict = card_dict