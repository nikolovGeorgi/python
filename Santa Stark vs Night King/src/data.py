import numpy as np
from field.convert_field import Field

class Data:
    """
        Data class:
            Receives text file with field information.
            Imports Numerical Python library & Field Class to process the given information.
            Only knows of the file name given to it. Reads it and converts the information to __grid or field values, which then get returned as a list.
            Private methods should only be used by Data class.
    """

    def __init__(self, field):
        ''' Private method. Data constructor. '''
        self.__field = field # Assigns passed in file to a private local variable for access within its scope.
        self.__data = self.__init_field() # Method call to initialize field and assigns its results to a local private variable

    def get_grid(self):
        ''' Public method. returns final grid information. '''
        return self.__set_grid() # Method call

    def get_variables(self):
        ''' Public method. returns final field variables (N, W, k) information. '''
        return self.__set_variables() # Method call

    # Numericalpy arrays consume less memory and provide availability to process full range operations without iterating each value.
    def __set_grid(self):
        ''' Private method. Accesses converted data from Field class and converts it to numerical python array of type float. '''
        return np.array(self.__data[0], dtype=float)

    def __set_variables(self):
        ''' Private method. Accesses converted data from Field class and converts it to numerical python array of type float. '''
        return np.array(self.__data[1][0], dtype=float)

    def __init_field(self):
        ''' Private method to initialize the field data. As result it returns List; index=0 == Grid data && index=1 == Field Variables'''
        return Field(self.__field).data()
