class Field:

    def __init__(self, file):
        self.file = file
        self.file_values = []
        self.grid = []

    def read_file(self):
        f = open(self.file,"r")
        self.get_line_values(f)
        f.close()

    def get_line_values(self, lines):
        for c, line in enumerate(lines):
            if c != 0:
                self.grid.append(self.line_to_int(line.rstrip().split(',')))
            self.file_values.append(self.line_to_int(line.rstrip().split(',')))

    '''
        < handle grid rotation here >
    '''

    @staticmethod
    def line_to_int(line):
        tmp = []
        for k in line:
            tmp.append(int(k))
        return tmp

    def data(self):
        self.read_file()

        return {
            'scenario': self.file_values,
            'variables': self.file_values[0],
            'grid': self.grid
        }

