# Library for timing code execution.
# Although "It avoids a number of common traps for measuring execution times.", it is still highly influenced by machine and system capabilities.
#
# Uncomment line 9 and last line prior to running to get processing time value.
import timeit
# print(timeit.timeit("""

from data import Data   ## Imports Data class to convert file data.
import numpy as np  ## Numerical python is essential to optimizing processing time.

files = [
    '../fields/FistOfTheFirstMen.txt',
    '../fields/Hardhome.txt',
    '../fields/CastleBlack.txt',
    '../fields/Winterfell.txt'
]

## Select which file to use.
# Main need for error handling is in convert_field,
#   because everything else depends on the results from reading the file.

data = Data(files[3])

## Set Grid & Variables.
grid = data.get_grid()  ## Acess public Data class method to grab grid data.
variables = data.get_variables()    ## Acess public Data class method to grab field variables data.

## Set Global Variables.
N = int(variables[0])   # Grid size.
W = variables[1]    # Amount of Wights. (ENEMIES!!!)
_k = variables[2]   # More than this amount of survivos is simply allowed!

archers_range = 30  # Archer's attack range.
enemies = [W / N] * len(grid)   # Convert enemies to fit grid.

## Create Clones for faster processing.
# Data clones allow us to not override our original data when running thousands of simulations.
# Once processed, reassigning the clones takes thousands of a second, compared to re-initializing the data, which may take for example 0.20 seconds.
grid_clone = grid[:]
enemy_clone = enemies[:]
enemy_updates = enemy_clone

## Create Volleys depending on grid size and archer's range.

def volleys(attack):
    try:
        volley = np.random.uniform(low=0.0, high=float(attack), size=(N,N))
        if N > archers_range:
            zeros = np.zeros((N - archers_range, N), dtype=float)
            volley_damage_variation = volley[N - archers_range:]
            return np.concatenate((zeros, volley_damage_variation))
        else:
            return volley
    except:
        ValueError
        return np.zeros((N, N), dtype=float)

## Stats
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('No more than (' +  str(_k) + ' - a fingernail) are allowed to live!!!!!!!!!')
print()

## Methods
def find_nearest(array, value):
    '''
        Receives an array of survivors and a particular value.
        Then it finds the closest index to that value from the array and returns it.
    '''
    try:
        return (np.abs(array - value)).argmin()
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)

def refine_search(attack, *args):
    '''
        Method that receives attack % and a value in the form of arguments.
        This allows us to call the method with a particular percent and do various amounts of iterrations on that percent.
            * Arguments are received in the form of a list.
                ** However we should only ever be passing a single value of how many simulations we would like to do. Thus we can simply call it's first index.
    '''
    try:
        enemy_updates = enemy_clone # Reassigns the clone to a variable that will be used for updating the approaching enemies.
        survivors_sum = []  # List that adds all survivors per simulation.
        iterator = 0    # Variable to count simulations until it reaches the given amount of simulations to be made.
        while iterator < args[0]:
            volley_percents = 1 - volleys(attack) / (100) # Reformat the Volleys grid to percentages to simplify calculations.
            for row in range(N):    ## for every row in the grid.
                tmp = enemy_updates - grid_clone[row]   ## Temp temporarily holds the enemies data after they have received static defence's damage.
                ## Through the beauty of Numerical Python, we can instantly check if any value is under zero.
                tmp[tmp < 0] = 0    ## Thus if any enemy is killed by a trap, we can simply update its data with zero.
                enemy_updates = np.array(tmp * volley_percents[row]) ## We then update the enemies by applying the respective volley's % damage for that row.
                enemy_updates[enemy_updates < 0] = 0 ## Checking again if all enemies are killed per cell of that current row, and setting them to zero if so.
            survivors_sum.append(enemy_updates) # At the end we add the survivors of the current battle simulation to our list of all survivors.
            enemy_updates = enemy_clone # Resetting enemies for the next simulation.
            iterator += 1   # Increasing battle simulation value
        return sum(sum(survivors_sum)/len(survivors_sum))   # Returning the average amount of survivors for all simulations.
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)

def quick_search():
    ''' Method that we use for finding the closest percent value for p that we can start working with. '''
    try:
        check_attack = 0 # we start with no archers and do a quick search for of their capabilities until we get a rough idea how strong they need to be in order to get less than the amount of survivors we need.
        # However to get a bit better understanding of that value than just a number, we do 10 battle simulations per percent.
        for check_attack in range(100):
            first_search_survivors = refine_search(check_attack, 10)
            if first_search_survivors < _k: # If we have found the value for p that we need. We return the attack % that has reached it.
                return check_attack
        return check_attack
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)

def look_deeper(new_search_range):
    ''' Once we do a quick search and get approximate attack value, We do another search of specific range around that value. '''
    try:
        survivors_book = {} ## We return a dictionary that holds survivors values per attack percent within the specific search range.
        for check_attack in new_search_range:
            survivors = refine_search(check_attack, 100)    ## We do 100 battle simulations per value of the given search range.
            survivors_book[check_attack] = (survivors)
        return survivors_book
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)

def unpack_survivors(search):
    ''' Method to unpack the survivors values from the survivors_book '''
    try:
        return np.array([k for k in search.values()])
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)

def unpack_attacks(search):
    ''' Method to unpack the attack percent values from the survivors_book '''
    try:
        return np.array([k for k in search.keys()])
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)

## Quick Search
# Get rough estimate at which attack percent to start refining our calculations. Like zooming slightly onto a photo.
quick_search_results = quick_search()
print("After a quick search of our archer's capabilities,")
print(('\twe found that '+ str(quick_search_results) +'% will approximately be our target for training!').expandtabs(2))
print(('\tHowever we will continue refining our search to find a better estimate!').expandtabs(2))
print()

## Second search
# Once we get initial attack value, we expand a search range around it (Example: 40 -> [38, 39, 40, 41, 42]).
# Then we search again for a more accurate estimate with 100 battle simulations and once we receive the results ->
# We find the attack and survivors rate at which we are under the amount of survivors needed to win in hand-to-hand with minimal archer's strength.
second_search_range = np.arange(quick_search_results-2, quick_search_results+3, 1)
second_search_results = look_deeper(second_search_range)
second_search_survivors = unpack_survivors(second_search_results)
second_search_attacks = unpack_attacks(second_search_results)
second_search_indx = find_nearest(second_search_survivors, _k)

print("For our second search we used range of attacks closest to our approximations!")
print(('\tWe used'+ str(second_search_range) +' and found that,').expandtabs(2))
print(('\tthe closer strength we should aim for is '+ str(second_search_attacks[second_search_indx]) +'%').expandtabs(2))
print(('\tWhich gave us rough estimates of '+ str(second_search_survivors[second_search_indx]) +' survivors').expandtabs(2))
print(('\tHowever we are not yet fully satisfied and we will continue refining our search to find a better estimate!').expandtabs(2))
print()

## After our report to Sansa, we create another search of a more indepth range of values.
## Third search
# We narrow the value range, but expand the depth of it to the thousands of a percent and repeat the previous process.
third_search_range = np.arange(second_search_attacks[second_search_indx]-.5, second_search_attacks[second_search_indx]+.5, .025)
third_search_results = look_deeper(third_search_range)
third_search_survivors = unpack_survivors(third_search_results)
third_search_atcks = unpack_attacks(third_search_results)

## Sort the survivors values from the third search
third_search_sorted_values = sorted(third_search_results.values())

## find the index of value corresponding to the nearest number of survivors that guarantee victory
trd_srch_index = find_nearest(third_search_survivors, _k)

print("For our third search we used the following range of attacks:")
print(('\t'+ str(third_search_range)).expandtabs(2))
print()
print(('\tWhich allows us to proudly say, in order to guarantee 95% defence success rate is,').expandtabs(2))
print(('\twe will need to train our archers to '+ str(third_search_atcks[trd_srch_index]) +'% of their maximum capabilities').expandtabs(2))
print(('\tWhich gave us rough estimates of '+ str(third_search_survivors[trd_srch_index]) +' survivors').expandtabs(2))
print(('\tHowever we are not yet fully satisfied and we will continue refining our search to find a better estimate!').expandtabs(2))
print()

## find previous surviros value in case current results are over the mark of _k
third_search_previous_survivors_value = third_search_sorted_values[third_search_sorted_values.index(third_search_survivors[trd_srch_index])-1]

# This is used in case we are slightly over the desired number, then we will for sure know that the previous one will guarantee us 95% rate.
## Assign the previous values for attack and survivors results from the third search after finding the closest survivors value to _k
temp_third_search_atck_surv_pair = [(key, value) for key, value in third_search_results.items() if value == third_search_previous_survivors_value]

def print_third_search_results(archers_atck, survivors_rate):
    ''' Method to pring final results to Sansa '''
    try:
        print('We have come up with a plan your highness!!')
        print('  We have discovered that we only need ' + str(archers_atck) + '% to achieve the minimal of ' + str(survivors_rate) + ' survivors')
        print(('\tAnd if we use our exceptional hand-to-hand combatants,').expandtabs(2))
        print(('we can assure our victory at minimal archer training!').expandtabs(2))
        print()
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)

## Once we have the final attack rate value, we verify one last time to make sure that it'll work, by running 1000 battle simulations on it.
final_archer_attack = str(temp_third_search_atck_surv_pair[0][0])
final_survival_rate = str(temp_third_search_atck_surv_pair[0][1])

final_srv = 0

if third_search_survivors[trd_srch_index] > 100.0:
    print_third_search_results(final_archer_attack, final_survival_rate)
    final_srv = refine_search(final_archer_attack, 1000)
else:
    print_third_search_results(third_search_atcks[trd_srch_index], third_search_survivors[trd_srch_index])
    final_srv = refine_search(third_search_atcks[trd_srch_index], 1000)

## Final report to Sansa.
print('However, our hearts tremble at the thought of losing to the wights, thus we decided to simulate a thousand battles with that training rate!!')
print('  What we found is that we may still succeed with an average of', final_srv, 'survivors')
print(('\tUnfortunatelly there are battle and nature uncertainties that could still cause to lose at an unfortunate 5% rate.').expandtabs(2))
print(('\tSo please be ware and keep that at mind when finilizing your decision!').expandtabs(2))
print()
print('Time needed to Execute:')

# """, number=1))
