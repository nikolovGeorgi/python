## Georgi Nikolov
## 11082966

class Input:
    """
        Input class:
            Only knows of the file name given to it. Reads it and converts the information to __grid or field values, which then get returned as a list.
            Private methods should only be used by Field class.
    """
    def __init__(self):
        ''' Class constructor: Assigns passed in information to local variables. Sets local variables '''
        self._input = []    # Local protected variable.

    def run_input(self):
        ''' Public method. Gets user input, verifies it and returns it if correct. '''
        duplicate = self.__get_input() # receives True or False depending if duplicates were found or not.
        while not duplicate:    # if there are duplicates, continue asking for input untill there are no duplicates.
            duplicate = self.__get_input()

        print()
        print("Accepted Input: ", self._input)  # if the input is correct, inform the user and return it.
        return self._input

    def __get_input(self):
        '''
            :method: Private Method. Receives user input and converts it to integer values. Then it updates its class variable "self._input" and verifies it.
            :return: Method call to check user input. returns True or False.
        '''
        self._input = self.__reformat_input(self.__receive_input())
        return self.__check_input(self._input)

    def __receive_input(self):
        ''' Private Method. Prints to the console and returns user input.'''
        print("Please enter a sequence of unique integers,")
        return input("\tbetween 1-9 inclusive, separated by spaces: ".expandtabs(2))

    def __reformat_input(self, lst):
        '''
            :method: Private Method. Receives user input as a list with one string. Formats each value as integer and returns a new list.
            :param lst: List containing one string of values.
            :return: Converts the string of values to a list of integer values instead. Returns a new list.
        '''
        return [int(k) for k in lst.split()]

    def __check_input(self, lst):
        '''
            :method: Private Method. Verifies if the formated integer list contains the correct amount of numbers.
            :param lst: list of integer values.
            :return: True if there is no input errors. False if there is not enough numbers or if there is duplicates.
        '''
        if len(lst) != 9:
            return False
        for k in lst:
            if lst.count(k) > 1:
                print('Duplicateup found!')
                print()
                return False
        return True

def verify_magic(lst):
    '''
        :method: Method to verify if received sequence of integers is a magic square.
        :param lst: list of nine integer values.
        :return: prints to the console if the sequence given by the user is a magic square or not.
    '''
    if lst[4] != 5:
        return print("The Sequence Is Not A Magic Square!\n")

    for k in [lst[c] for c, i in enumerate(lst) if c % 2 == 0 and c != 4]:
        if k % 2 == 0:
            return print("The Sequence Is A Magic Square!\n")
        else:
            return print("The Sequence Is Not A Magic Square!\n")

verify_magic(Input().run_input())   # calls Input class to initiate input request sequence. Then verifies that input and decides if it's a magic square.

