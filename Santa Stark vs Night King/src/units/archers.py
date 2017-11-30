class Archer:

    def __init__(self):
        self.__data = {} # private variable

    def set_attack_range(self, value):
        self.__data['ATR'] = value

        #protected method
    def _set_attack_skill(self):
        self.__data['skill'] = 'flaming arrow'

        #protected method
    def _set_attack_power(self):
        self.__data['ATP'] = { 'min': 0, 'max': 100 }

        #protected method
    def set_current_damage(self, value):
        self.__data['DMG'] = { 'min': 0, 'max': value }

    def __init_data__(self):
        self._set_attack_skill()
        self._set_attack_power()

    def data(self):
        self.__init_data__()
        return self.__data

