## Draw Histogram - Asterix for every repeated value in a sequence
def get_data(n):
    '''
    :param n: referes to the size of list of integers the user needs to input.
    :return : list of integers.
    '''
    data = []   # list to store the inputed integers
    for i in range(n):  # i is only used as an iterator.
        data.append(verify_input('Enter one integer only: ')) # for each inputed integer - verify if its valid & if so add it to the data.
    return data

def counting(data):
    '''
    :param data: list of integers to check uniqueness and frequency of.
    :retrun : dictionary containing unique values and their frequency as a key-value pair.
    '''
    frequency = {}  # dictionary to store unique and re-appearing integers in the data, & to be returned

    seen = False    # variable to confirm if an integer is unique or re-appearing
    for item in data:
        if item not in frequency.keys(): seen = False   # if the current integer in the data has not been seen before, then it is unique.
        if not seen:
            frequency[item] = data.count(item)  # if the current integer is unique then add it to our collection and count how many of it are in the data.
            seen = True # mark the integer as accounted for.
    return frequency    # return collection

def draw_histogram(frequency):
    '''
    :param frequency: collection of unique integers and their re-appearance in a key-value pair.
    :return: Has no return. Only functionality is to print results.
    '''
    print("\n\n\n----------- Histogram ----------------\n")

    for f in sorted(frequency.keys()):  # sort the values in our data - to be printed in order
        print(f, '*'*frequency[f])  # add a star for each unique integer's appearance in the original data

def verify_input(message):
    '''
    :param message: accept a message to be printed to the console.
    :return value:  inputed single positive integer value. If value type is correct - return it.
    '''
    while True: # While no value errors try to get user input of type int.
        try:
            value = int(input(message)) # forcefully convert the input to int - if possible - if not return ValueError.
            if value < 0: raise ValueError # if inputed value is negative - raise a ValueError.
        except ValueError:  # if there is a ValueError inform the user of it.
            print("Invalid Input. Please enter an integer value!")
            print()
            continue    # Repeat the loop and ask the user for another value. Until a valid integer is inputed.
        else:
            return value    # Once a valid integer is inputed -> break out by returning it to the requesting method.

## To keep the heap and global frame clean and effective: chain methods to bypass the need for storing unnecessary names.
draw_histogram(counting(get_data(verify_input('How many data values? '))))

