class Field:
    """
        Field class:
            Only knows of the file name given to it. Reads it and converts the information to __grid or field values, which then get returned as a list.
            Private methods should only be used by Field class.
    """
    def __init__(self, file):
        ''' Class constructor: Assigns passed in information to local variables. Sets local variables '''
        self.file = self.__check_file_type(file)    # Text file with field information
        self.__file_values = []   # Private Variable holder for Field variables (N, W, k)
        self.__grid = []  # Private Grid values

    def __check_file_type(self, file):
        ''' Private Method. Checks if file type is string. '''
        try:
            if isinstance(file, str):
                return file
            else:
                raise TypeError
        except ValueError as error:
            print('Inappropriate Value ->', error)
        except TypeError as error:
            print('Type Mismatch -> ', error)

    def __read_file(self):
        ''' Private method. Reads text file.'''
        try:
            file = open(self.file,"r")
            self.__get_line_values(file)  ## method call
            file.close()
        except TypeError as error:
            print('Type Mismatch -> ', error)


    def __get_line_values(self, lines):
        ''' Private method. Converts each line into __grid values, or field variables (N, W, k). '''
        # :param lines: field text file lines
        try:
            for index, line in enumerate(lines):
                if index != 0:
                    self.__grid.append(line)
                else:
                    self.__file_values.append(line)
        except ValueError as error:
            print('Inappropriate Value ->', error)
        except TypeError as error:
            print('Type Mismatch -> ', error)

    def __rs_line(self, line):
        ''' Private method. removes new line character and commas. '''
        try:
            return line.rstrip().split(',')
        except ValueError as error:
            print('Inappropriate Value ->', error)
        except TypeError as error:
            print('Type Mismatch -> ', error)

    def __clean_up_lines(self, lst):
        ''' Private method. Calls __rs_line() to remove uneeded infromation from the data. '''
        # :param lst: list of strings to be cleaned up -> grid / field variables
        try:
            for index, row in enumerate(lst):
                lst[index] = self.__rs_line(row)
        except ValueError as error:
            print('Inappropriate Value ->', error)
        except TypeError as error:
            print('Type Mismatch -> ', error)

    def data(self):
        '''
            Public method.
                Once called it beings a sequence to read the text file given.
                Converts the lines and removes all new line characters and commas.
            :return: List of two lists: Containing string data respectively to Grid information and Field Variables.
        '''
        self.__read_file()
        self.__clean_up_lines(self.__grid)
        self.__clean_up_lines(self.__file_values)
        return [self.__grid, self.__file_values]
