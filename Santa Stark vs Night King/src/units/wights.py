class Wights:
    def __init__(self):
        self.__data = {}

    def set_starting_locations(self, squares):
        self.__data['grid'] = [self.__data['size']/squares]*squares

    def set_army_size(self, amount):
        self.__data['size'] = amount

    def data(self):
        return self.__data
