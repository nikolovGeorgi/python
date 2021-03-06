## Check if a square is Latin. Latin Square is a square in which the values in every row and column appear only once
def get_grid_size():
    '''
    :method: Receives user input for the size of the square. If
        it's not a positive integer -> 1) inform the user 2) request another value
    :return: integer value representing the size of the square
    '''
    while True:
        try:
            grid_size = int(input("Please enter size of the square: ")) # try to convert the value to integer, if it can't be - raise value error
            if grid_size <= 0: raise ValueError # if value is negative raise an error
        except ValueError:
            print("Invalid input. Please Enter a positive integer!")
            print()
            continue  # if input value is not valid - continue the truthy state
        else:
            print("Thank you!")
            print()
            return grid_size # if input value is valid - return it (return breaks the truthy state of the loop)

def get_rows_data(row, grid_size):
    '''
    :method: Receives user input for the data in the current row of the square. If
        it's not of positive integers -> 1) inform the user 2) request another input
    :param row: used to reference the number of the current row in the square.
    :param grid_size: references the value that is the square size.
    :return: integer values representing the data in the current row of the square
    '''
    while True:
        try:
            data = reformat_input(input("Enter data for row #" + str(row) + ": "))
            if len(data) != grid_size: raise ValueError # if the input does not contain enough elements raise an error
            for k in data:
                if k > grid_size: raise ValueError # if the inputed element is greater than the needed value, raise an error
        except ValueError:
            print("Invalid input.")
            print("Please Enter a range of", grid_size, "positive integers (from 1 to", str(grid_size) + " inclusive) separated by space!")
            print()
            continue
        else:
            return data

def data_init(grid_size):
    '''
    :method: Asks the user to input integer values for each row in the square.
    :param grid_size: Holds the size of the square.
    :return: List of lists, each of which holds integers per row
    '''
    return [get_rows_data(row, grid_size) for row in range(1, grid_size + 1)]

def reformat_input(string_data):
    '''
    :method: Receives a list of values, separated by space, as a string. Splits and converts to integer each value.
    :param string_data: list of stringed data to be converted to integer values before returning.
    :return: List of integer values - data of current row in the square.
    '''
    return [int(k) for k in string_data.split()]

def check_duplicates(lst):
    '''
    :method: receives a list of integers values & checks for duplicates in it.
    :param lst: list of integer values ( current row of the square )
    :return: False if the list contains duplicates, else returns the original list.
    '''
    # Faster to keep it split, than in list comprehension -> allows to terminate sooner than later, if duplicate found.
    for k in lst:
        if lst.count(k) > 1: return False
    return lst

def check_columns(grid, grid_size):
    '''
    :method: For columns to be duplicate as a whole, they would create duplicate values in the rows, which is previously checked. Thus this method checks for duplicated values in the columns only.
    :param grid: column list of values representing the integers stored in it.
    :param grid_size: size of the column
    :return if there's no duplicates return True, else False
    '''
    for k in range(grid_size):
        if not check_duplicates([row[k] for row in grid]): return False
    return True

def check_rows(grid_data):
    '''
    :method: receives a list of lists of integers, representing the rows. First checks
        if there's duplicated rows, then checks for duplicated values in each row.
    :param lst: list of lists of integers in the rows of the square.
    :return: True if no duplicates are found, or else - False
    '''
    # Faster to keep it split, than in list comprehension -> allows to terminate sooner than later, if duplicate found.
    for row in grid_data:
        if not check_duplicates(row): return False ## Check for duplicate values in a row
    return True

def check_latin():
    '''
    :method: receives a list of lists - the inputed row positive integers, and the size of the square
    :param lst: list of lists of inputed row positive integers
    :param grid: size of the square as a positive integer value
    :return: 'no' if the square is not Latin, and 'yes' if it is.
    '''
    grid_size = get_grid_size() # variable name to reference the size of the square
    grid_data = data_init(grid_size) # list to hold all integers in the square, by rows
    try:
        if not check_rows(grid_data): raise ValueError
        if not check_columns(grid_data, grid_size): raise ValueError
    except ValueError:
        print('no')
    else:
        print('yes')

check_latin()
