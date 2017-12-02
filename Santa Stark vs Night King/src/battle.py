import copy
class Battle:
    def __init__(self, data):
        self.__data = {}
        self._temp = { 'turns': {}, 'survivors': 0 }
        self._enemies = copy.deepcopy(data['enemies']['grid'])
        self._volleys = copy.deepcopy(data['archers']['volleys'])
        self._grid = self._convert_grid(copy.deepcopy(data['field']['grid']))

    def __run(self):
        self._init_outcome()
        self._set_battle_records(self._temp)

    def _convert_grid(self, grid):
        out = {}
        for index, cell in enumerate(grid): out[index] = cell
        return out

    def _init_outcome(self):
        survivors = 0
        for turn, row in self._grid.items():
            self._update_outcome(row, self._volleys[turn], turn)
            if turn == max(self._grid.keys()):
                survivors = sum([k for k in self._enemies])
                self._temp['survivors'] = survivors

    def _update_outcome(self, row, volley, turn):
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
        res = {}
        res[turn] = lst
        self._temp['turns'].update(res)

    def _set_battle_records(self, data):
        self.__data['battle'] = data

    def data(self):
        self.__run()
        return self.__data
