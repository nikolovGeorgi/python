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
        for index, line in enumerate(lines):
            if index != 0:
                self.grid.append(self.line_to_int(self.rs_line(line)))
            self.file_values.append(self.line_to_int(self.rs_line(line)))

    @staticmethod
    def line_to_int(line):
        return [int(k) for k in line]

    def rs_line(self, line):
        return line.rstrip().split(',')

    def data(self):
        self.read_file()

        return {
            'scenario': self.file_values,
            'variables': self.file_values[0],
            'grid': self.grid
        }
