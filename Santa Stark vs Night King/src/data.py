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
        self._p = 20

    def _set_p(self, archers):
        archers._set_p(self._p)

    def _set_probability(self, *args):
        for i in args:
            if i == None: self._p = 20
            else: self._p = i

    def data(self):
        self.__run()
        return self.__data

    def __run(self):
        # self.__data['location'] = self.field
        data = self.__data['field'] = self.__init_field()
        self.__data['enemies'] = Wights(data['N'], data['W']).data()

        self.archers(data)
        self.__data.update(Battle(self.__data).data())

    def archers(self, data):
        archers = Archer(data['grid'])
        self._set_p(archers)
        self.__data['archers'] = archers.data()

    def __init_field(self):
        return ConstructJSON(Field(self.field), {}).get_data()
