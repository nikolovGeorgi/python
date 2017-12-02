import copy

class Battle:
    def __init__(self, data):
        self.__data = {}
        self._temp = { 'turns': {}, 'survivors': 0 }
        self._enemies = copy.copy(data['enemies']['grid'])
        self._volleys = copy.copy(data['archers']['volleys'])
        self._grid = self._convert_grid(copy.copy(data['field']['grid']))
        self._success_rate = data['field']['k']

    # creating copy before simulation begins, to bypass overriding original grid
    def _convert_grid(self, grid):
        out = {}
        for index, cell in enumerate(grid): out[index] = cell
        return out

    # Once simulation has started -> initialize outcome and create records
    def __run(self):
        self._init_outcome()
        self._set_battle_records(self._temp)

    def _init_outcome(self):
        survivors = 0
        for turn, row in self._grid.items():
            self._update_outcome(row, self._volleys[turn], turn)

            if turn == max(self._grid.keys()):
                survivors = sum([k for k in self._enemies])
                self._temp['survivors'] = survivors

        if survivors < self._success_rate: self._temp['success'] = True
        else: self._temp['success'] = False

    def _update_outcome(self, row, volley, turn):
        new_grid = []
        for index, cell in enumerate(row):
            remains = self._enemies[index] - cell

            # if static defences kill all enemies return 0
            if remains <= 0: new_grid.append(0)

            # else archers shoot a volley of flaming arrows
            else:
                # if volley damage == 0% then remaining wights advance undamaged by the archers

                if volley[index] == 0: new_grid.append(remains)

                # else apply volley damage to the remains
                else:
                    remains_of_all_damage_applied = remains - (remains * volley[index]/100)

                    # if the volley kills all remaining enemies then return 0
                    if remains_of_all_damage_applied <= 0: new_grid.append(0)

                    # else return the final remains of wights
                    else: new_grid.append(remains_of_all_damage_applied)
        self._update_grid(new_grid, turn)

    def _update_grid(self, grid, turn):
        self._enemies = grid
        self._init_data(grid, turn)

    def _init_data(self, grid, turn):
        res = {}
        res[turn] = grid
        self._temp['turns'].update(res)

    # Create battle records after simulation is complete
    def _set_battle_records(self, data):
        self.__data['battle'] = data

    # Once battle data is requested -> run simulation
    def data(self):
        self.__run()
        return self.__data
