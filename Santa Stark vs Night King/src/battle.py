class Battle:
    def __init__(self):
        # self.__field = {}
        self.__data = {}

    def __init_game_start__(self):
        pass

    def __turn__(self):
        pass

    def set_field(self, field):
        self.__data['field'] = field

    def set_archers(self, archers):
        self.__data['archers'] = archers.data()

    def set_enemy(self, enemy):
        self.__data['enemy'] = enemy.data()

    def data(self):
        # print(self.__data)
        return self.__data
