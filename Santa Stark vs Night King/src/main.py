from data import Data
data = Data('../fields/test.txt').data()
for k, v in data.items():
    print(k, v)
    print()

from battle import Battle
battle = Battle(data).data()
