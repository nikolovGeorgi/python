## Check the validity of Sudoku grid.

import sys
class Data:
    '''
        Data class:
            Receives text file with field information.
            Imports Numerical Python library & Field Class to process the given information.
            Only knows of the file name given to it. Reads it and converts the information to __grid or field values, which then get returned as a list.
            Private methods should only be used by Data class.
    '''
    def __init__(self, file):
        ''' Class constructor: Assigns passed in information to local variables. Sets local variables '''
        self.file = self.__check_file_type(file)    # Text file with field information
        self.__grid = []  # Private Grid values

    def __check_file_type(self, file):
        ''' Private Method. Checks if file type is string. '''
        try:
            if isinstance(file, str):
                return file
            else:
                raise TypeError
        except ValueError as error:
            print('Inappropriate Value', error)
        except TypeError as error:
            print('Type Mismatch', error)

    def __read_file(self):
        ''' Private method. Reads text file.'''
        file = open(self.file,"r")
        self.__get_line_values(file)  ## method call
        file.close()

    def __convert_line_values(self, line):
        '''
            :method: Private method. removes new line character and commas.
            :param line: Current line read from file to be formated.
            :return: Does not return, just updates the existing list passed in as param.
        '''
        try:
            return [int(value) for value in line.split(' ') if value]
        except ValueError as error:
            print('Inappropriate Value: ', error)
        except TypeError as error:
            print('Type Mismatch: ', error)

    def __generate_lines(self, lines):
        '''
            :method: Private - creates a generator from all file lines after stripping them from a new line character.
            :param lines: list of all lines in the file given.
            :return: generator of all lines, converted to strings.
        '''
        return (line.rstrip() for line in lines)

    def __get_line_values(self, lines):
        '''
            :method: Private method. Converts each line into __grid values
            :param lines: list of all lines from the file.
            :return: Only updates class variable self.__grid
        '''
        try:
            self.__grid = [self.__convert_line_values(k[0]) for k in (list(line.split(',') for line in self.__generate_lines(lines) if line))]
        except ValueError as error:
            print('Inappropriate Value: ', error)
        except TypeError as error:
            print('Type Mismatch: ', error)

    def __run_data(self):
        '''
            Public method.
                Once called it beings a sequence to read the text file given.
                Converts the lines and removes all new line characters and commas.
            :return: List of two lists: Containing string data respectively to Grid information and Field Variables.
        '''
        self.__read_file()

    def get_grid(self):
        ''' Public Method. Returns the grid when called. '''
        self.__run_data() # Method Call to format file data
        return self.__grid

def check_duplicates(lst):
        '''
            :method: Private Method. Verifies duplicates - if any -> returns False - else True
            :param lst: accepts a list of integer values in range 1-9.
            :return: True if there is no duplicates, False if there is.
        '''
        for k in lst:
            if k <= 0 or k > 9: return False
            if lst.count(k) > 1: return False
        return True

def check_rows(grid):
    '''
        :method: calls check_duplicate() to verify if there are any duplicates in a given row.
        :param grid: List of all rows and the values they reference.
        :return: True if there is no duplicates, False if there is.
    '''
    for row in grid:
        if not check_duplicates(row): return False
    return True

def check_columns(grid, grid_size):
    '''
        :method: Columns can never be duplicate as a whole, because that would mean we have duplicate values in the rows -> which is what this method checks.
        :param grid: column list of values representing the integers stored in it.
        :param grid_size: size of the column
        :return if there's no duplicates return True, else False
    '''
    for k in range(grid_size):
        if not check_duplicates([row[k] for row in grid]): return False
    return True

def verify_sudoku(grid):
    '''
        :method: Once file data is read and converted - verify_sudoku checks if the sequences are valid.
        :param grid: List of all 9 cubes and their sequences.
        :return: Prints to the console if the cube is valid or not.
    '''
    if check_rows(grid) and check_columns(grid, len(grid)): return print('yes')
    else: return print('no')

# # ignores variable names that wont be used more than once, leaving global stack empty upon complete execution.
verify_sudoku(Data(sys.argv[1]).get_grid())
