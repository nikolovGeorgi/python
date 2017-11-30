# Georgi Nikolov

# Module Imports:
import sys

# Program Methods:
def create_mapping(keys, values):
    '''
    :param keys: list, the purpose of which is to be the keys of the resulting structure
    :param values: list, the purpose of which is to be the values of the keys for the resulting structure
    :return: returns a dictionary created by the keys and values
    '''
    # result -> variable for the returning dictionary
    result = {}
    for index in range(0, len(keys)):
        # if possible (same length lists) -> create combining dictionary
        try:
            result[keys[index]] = values[index]
        # else -> return empty
        except:
            result = {}
    return result

def index_district(votes, candidates, parties):
    '''
    :param votes: a list of vote counts for an electoral district
    :param candidates: a list of the candidates for the district
    :param parties: a list of all the political party names for this election
    :return: a record created from combining the three input lists
    '''
    vots = {}   # Variable to hold the generated mapping for votes
    cands = {}  # Variable to hold the generated mapping for candidates

    # Create maps for votes & candidates
    vots = create_mapping(parties, votes[1:])
    cands = create_mapping(parties, candidates[1:])

    # result -> variable holding the structure for specific district
    result = {
        'Name': votes[0],
        'Candidates': cands,
        'Votes': vots
    }
    return result

def index_all_districts(votes, candidates, parties):
    '''
    :param votes: a list of vote counts for each electoral district
    :param candidates: a list of the candidates for each of the districts
    :param parties: a list of all the political party names for this election
    :return: database combining the three input lists
    '''
    result = {} # variable holding the database structure
    temp_votes = [] # temporary variable for iteration of districts

    # Create database structure
    for index in range(0, len(votes)):
        temp_votes.append(votes[index][0])
        temp_votes.extend(votes[index][1:])
        result[votes[index][0]] = index_district(temp_votes, candidates[index], parties)

        # dump all temporary information before next iteration
        temp_votes = []

    return result

def find_winner(voted_names):
    '''
    :param voted_names: a list of vote counts for each electoral district
    :return: database combining the three input lists
    '''
    # If voted_names is valid return winner else return empty
    try:
        return ''.join([letter for letter in str(max(voted_names.items(), key=lambda k: k[1])) if letter.isupper()])
    except:
        return {}

def find_all_winners(database):
    '''
    :param database: database containing every electoral district record
    :return: the same database with added new key-value pair to each district’s record: the new key will be ’Winner’, and its value will be the name of the winning party
    '''
    temp = [] # temporary variable for holding winner per district record
    for district_record in database.values():
        temp.append(find_winner(district_record['Votes']))
    for winning_party_name, district in enumerate(database.keys()):
        database[district]['Winner'] = temp[winning_party_name]

def read_party_names(vote_count_file):
    '''
    :param vote_count_file: a string with the name of a vote count file
    :return: a list of the party names that appear on the first line of the file
    '''
    # Attempt to open the text file, if invalid -> report error; else return participants
    try:
        return open(vote_count_file).readline().rstrip().split(',')[1:]
    except OSError as err:
        return "OS error: {}".format(err)

def str_or_int(value):
    '''
    :param value -> index from a list to be converted
    :return converted value as either string or integer
    '''
    # If value cannot be converted to integer, then convert to string; else return integer
    try:
        return int(value)
    except ValueError:
        return str(value)
def read_election_files(candidates_file, vote_counts_file):
    '''
    :param candidates_file -> text file with candidates
    :param vote_counts_file -> text file with vote countes
    :return tuple with two lists; First holding all candidates, Second holding all votes
    '''
    # res is a varialbe to hold the tuple construction
    res = ([], [])

    # Structure:
    '''
        Candidates:
            - read each line after first line & convert to list
            - for each line -> strip return & split by commas
                * extend existing list of candidates in the resulting structure by passing the formated line
        Votes:
            - Same as Candidates, however: once each line is stripped from return & split
                * call str_or_int() method to convert its index value to either string or integer
            - extend existing list of votes in the resulting structure by passing the formated & edited line
    '''
    res[0].extend([line.rstrip().split(',') for line in list(open(candidates_file, 'r'))[1:]])
    res[1].extend([[str_or_int(index) for index in line.rstrip().split(',')] for line in list(open(vote_counts_file, 'r'))[1:]])
    return res

def write_election_results(write_to_file, district_database):
    '''
    :param write_to_file -> name of desired file to be written to, in the form of a string
    :param district_database -> edited elections database # includes party winners
    :return -> has no return; writes to file instead
    '''
    # fo -> variable to open a new file with written permissions only
    fo = open(write_to_file, 'w')
    for district_name, district_record in district_database.items():
        for record_type, record_type_data in district_record.items():
            if record_type == 'Winner':
                fo.write(
                    district_name + ',' +
                    str(district_record['Votes'][record_type_data]) + ',' +
                    record_type_data + ',' +
                    str(district_record['Candidates'][record_type_data]) +
                    '\n'
                )
    # close file once it's complete
    fo.close()

def summary_report(participants, districts_won_by_party):
    '''
    :param participants -> participating parties
    :param districts_won_by_party -> dictionary with the election winners and the number of districts they have won
    :return -> prints to the console
    '''

    # winner holds the name of the winning party with most districts won
    winner = (max(districts_won_by_party, key=districts_won_by_party.get))

    print()
    print('*****Election summary*****')
    print('Participating parties:', participants)
    print('Districts won by each party:', districts_won_by_party)
    print('{0} won the election with {1} districts'.format(winner, districts_won_by_party[winner]))
    print()

def main():
    '''
    :method -> executes the program structurally and reports the results a file 'sk_elections_results_2016.scv' as well as to the console
    '''
    # Read the provided text files - import & format the information
    parties = read_party_names('sk_election_candidates_2016.csv')
    (candidates, votes) = read_election_files('sk_election_candidates_2016.csv','sk_election_votecounts_2016.csv')

    # Create Database from the compiled information
    database = index_all_districts(votes, candidates, parties)
    find_all_winners(database)

    # Write a new file with the outcomes of the elections
    write_election_results('sk_elections_results_2016.csv', database)

    # Create temporary variable for storing all winning parties
    temp = []
    for k in database.keys():
        temp.append(database[k]['Winner'])

    # Sum up all winnings by participating party
    results = dict(zip(temp, [temp.count(i) for i in temp]))

    # Pass the needed information for the final report
    summary_report(parties, dict(sorted(results.items(), key=lambda x:x[1])))

# Execute program
main()
