import random as rnd
import copy
class Archer:

    def __init__(self, grid):
        self.__data = {} # private variable
        self.__range = 30
        self._p = 20
        self._grid = copy.deepcopy(grid)

    def _set_attack_range(self):
        self.__data['ATR'] = self.__range

        #protected method
    def _set_attack_skill(self):
        self.__data['skill'] = 'flaming arrow'

        #protected method
    def _set_attack_power(self):
        self.__data['ATP'] = { 'min': 0., 'max': 100. }

        #protected method
    def _set_current_damage(self):
        ## value == p # Using default set value at the moment <- change
        self.__data['DMG'] = { 'min': 0., 'max': float(self._p) }

    def __run(self):
        self._set_attack_skill()
        self._set_attack_range()
        self._set_attack_power()
        self._set_current_damage()
        self.__init_archers_dmg_distribution()

    def data(self):
        self.__run()
        return self.__data

    def __init_archers_dmg_distribution(self):
        temp_obj = {}
        for turn, row in enumerate(self._grid):
            temp_arr = []
            temp_arr.extend(self.__update_archers_dmg_distribution(row, self.__data['DMG']))
            temp_obj[turn] = temp_arr
        self.__set_archers_dmg_distribution(temp_obj)

    def __update_archers_dmg_distribution(self, row, dmg):
        temp_grid = row
        temp_grid[:] = [rnd.uniform(0., dmg['max']) for i in row]
        return temp_grid

    def __set_archers_dmg_distribution(self, temp_data):
        self.__data['volleys'] = temp_data
        self.__data['temp'] = {0:[10, 5, 15], 1:[20, 15, 5], 2:[5, 20, 20]}
