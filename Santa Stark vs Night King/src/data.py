# Field initialization
from field.convert_field import Field
from field.construct_json import ConstructJSON

# Units initialization
from units.archers import Archer
from units.wights import Wights

from battle import Battle
# battle = Battle(data).data()

class Data:
    def __init__(self, field):
        self.__data = {}
        self.field = field

    def data(self):
        self.__run()
        # print(self.__data)
        return self.__data

    def __run(self):
        # self.__data['location'] = self.field
        data = self.__data['field'] = self.__init_field()
        self.__data['enemies'] = Wights(data['N'], data['W']).data()
        self.__data['archers'] = Archer(data['grid']).data()
        self.__data.update(Battle(self.__data).data())

    def __init_field(self):
        return ConstructJSON(Field(self.field), {}).get_data()
