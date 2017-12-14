import numpy as np
N = 2
archers_range = 30

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


print('════════════════════ Testing Volleys ════════════════════')
volleys_tests =  [
        {'id': 0, 'inputs': [-5, 3, -1], 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 1, 'inputs': [.2], 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 2, 'inputs': [], 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 3, 'inputs': {}, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 4, 'inputs': {0:2}, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 5, 'inputs': {0:[2, 3]}, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 6, 'inputs': {'00':2}, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 7, 'inputs': {'00':2, 5: [123, 233]}, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 8, 'inputs': None, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 9, 'inputs': True, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
        {'id': 10, 'inputs': False, 'outputs': np.zeros((N, N), dtype=float), 'reason': 'Volley grid damage difference'},
    ]

for test in volleys_tests:
    attack = test['inputs']
    expected = test['outputs']

    result = volleys(attack)
    if not all(k in result for k in expected):
        print("Error in test #" + str(test['id']) + ":", test['reason'], '\n', attack, '\nyielded:\n', str(result) + ',\nbut expected:\n', expected)
        print()
    else:
        print("Volley test #" + str(test['id']), "has passed!!")
print()

##############################################################################
##############################################################################
##############################################################################

def find_nearest(array, value):
    try:
        return (np.abs(array - value)).argmin()
    except ValueError as error:
        print('Inappropriate Value ->', error)
    except TypeError as error:
        print('Type Mismatch -> ', error)



print('════════════════════ Testing find_nearest() ════════════════════')
find_nearest_tests =  [
        {'id': 0, 'inputs': np.array([-5, 3, 5, 6, 11, 20, -1]), 'target': 10, 'outputs': 4, 'reason': "Target value out of list value's range"},
        {'id': 1, 'inputs': np.array([.2]), 'target': 10, 'outputs': 0, 'reason': "Target value out of list value's range"},
        {'id': 2, 'inputs': np.array([]), 'target': 10, 'outputs': None, 'reason': "Empty List"},
        {'id': 3, 'inputs': {}, 'target': 10, 'outputs': None, 'reason': 'Type Mismatch'},
        {'id': 4, 'inputs': {0:2}, 'target': 10, 'outputs': None, 'reason': 'Type Mismatch'},
        {'id': 5, 'inputs': {0:[2, 3]}, 'target': 10, 'outputs': None, 'reason': 'Type Mismatch'},
        {'id': 6, 'inputs': {'00':2}, 'target': 10, 'outputs': None, 'reason': 'Type Mismatch'},
        {'id': 7, 'inputs': {'00':2, 5: [123, 233]}, 'target': 10, 'outputs': None, 'reason': 'Type Mismatch'},
        {'id': 8, 'inputs': None, 'target': 10, 'outputs': None, 'reason': 'Type Mismatch'},
        {'id': 9, 'inputs': np.array([1, 2, 3, 4, 5, 6]), 'target': 4, 'outputs': 3, 'reason': 'Type Mismatch'},
    ]

for test in find_nearest_tests:
    array_values = test['inputs']
    target_value = test['target']
    expected = test['outputs']

    result = find_nearest(array_values, target_value)
    if result != expected:
        print("Error in test #" + str(test['id']) + ":", test['reason'], '\n', attack, '\nyielded:\n', str(result) + ',\nbut expected:\n', expected)
        print()
    else:
        print("Find Nearest() test #" + str(test['id']), "has passed!!")
        print()

print()
