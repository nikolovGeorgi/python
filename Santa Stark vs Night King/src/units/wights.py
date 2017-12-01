class Wights:
    def __init__(self, row_size, army_size):
        self.__data = {}
        self.row_size = row_size
        self.army_size = army_size

    def __run(self):
        self.__set_army_size(self.army_size)
        self.__set_starting_locations(self.row_size)

    def __set_starting_locations(self, row_size):
        self.__data['grid'] = [self.__data['size']/row_size]*row_size

    def __set_army_size(self, amount):
        self.__data['size'] = amount

    def data(self):
        self.__run()
        return self.__data
