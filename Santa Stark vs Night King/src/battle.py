class Battle:
    def __init__(self):
        self.__data = { 'turns': {} }

    def __init_game_start__(self):
        pass

    def run(self):
        temp_obj = {}
        for turn, row in enumerate(self.__data['field']['grid']):
            temp_arr = []
            self.__update_enemies(row, self.__data['enemy']['grid'])
            temp_arr.extend(self.__data['enemy']['grid'])
            temp_obj[turn] = temp_arr

        self.__set_turns_data__(temp_obj)
        print(self.__data)

    def __update_enemies(self, row, enemies):
        self.__data['enemy']['grid'][:] = [a - b for a, b in zip(enemies, row)]

    def __set_turns_data__(self, temp_data):
        self.__data['turns'].update(temp_data)

    def set_field(self, field):
        self.__data['field'] = field

    def set_archers(self, archers):
        self.__data['archers'] = archers.data()

    def set_enemy(self, enemy):
        self.__data['enemy'] = enemy.data()

    def data(self):
        return self.__data
