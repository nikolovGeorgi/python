# Field initialization
from convert_field import Field
from construct_json import ConstructJSON

# # Units initialization
from archers import Archer
from wights import Wights

class Data:
    def __init__(self, field):
        self.__data = {}
        self.field = field

    def data(self):
        self.__run()
        return self.__data

    def __run(self):
        data = self.__data['field'] = self.__init_field()
        self.__data['enemies'] = Wights(data['N'], data['W']).data()
        self.__data['archers'] = Archer(data['grid']).data()

    def __init_field(self):
        return ConstructJSON(Field(self.field), {}).get_data()
