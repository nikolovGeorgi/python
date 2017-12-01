import copy
class Battle:
    def __init__(self, data):
        self.__data = {}
        self._t = {}
        self._enemies = copy.deepcopy(data['enemies']['grid'])
        self._volleys = copy.deepcopy(data['archers']['temp'])
        self._grid = self._convert_grid(copy.deepcopy(data['field']['grid']))

    def run(self):
        self.t_init_outcome()

    def _convert_grid(self, grid):
        out = {}
        for c, k in enumerate(grid):
            out[c] = k
        return out

    def t_init_outcome(self):
        survivors = 0
        for turn, row in self._grid.items():
            self.t_update_outcome(row, self._volleys[turn], turn)
            if turn == max(self._grid.keys()):
                print()
                print('Final')
                print(self._enemies)

                survivors = sum([k for k in self._enemies])
                print(survivors)

    def t_update_outcome(self, row, volley, turn):
        out = []
        for index, cell in enumerate(row):
            remains = self._enemies[index] - cell
            if volley[index] == 0:
                out.append(remains)
            else:
                out.append(remains - (remains * volley[index]/100))

        self.t_qq(out, turn)

    def t_qq(self, grid, turn):
        self._enemies = grid
        self._init_data(grid, turn)

    def _init_data(self, lst, turn):
        q = {}
        q[turn] = lst
        self._t.update(q)

    def _set_battle_records(self, data):
        self.__data['battle'] = data

    def data(self):
        self.run()
        # return self.__data
