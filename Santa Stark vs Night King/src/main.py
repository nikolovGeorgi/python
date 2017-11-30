# Field initialization
from convert_field import Field
from construct_json import ConstructJSON
f1 = ConstructJSON(Field('../fields/test.txt'), {}).get_data()
f2 = ConstructJSON(Field('../fields/CastleBlack.txt'), {}).get_data()
f3 = ConstructJSON(Field('../fields/Hardhome.txt'), {}).get_data()
f4 = ConstructJSON(Field('../fields/Winterfell.txt'), {}).get_data()
f5 = ConstructJSON(Field('../fields/FirstOfTheFirstMen.txt'), {}).get_data()


# Units initialization
from archers import Archer
archers = Archer()
archers.set_attack_range(30)
archers.set_current_damage(20)

from wights import Wights
wights = Wights()
wights.set_army_size(f1['W'])
wights.set_starting_locations(f1['N'])


# Uncertainties initialization
from uncertainties import Uncertainties
un = Uncertainties()


# Battle initialization
from battle import Battle
battle = Battle()
battle.set_field(f1)
battle.set_enemy(wights)
battle.set_archers(archers)
b = battle.data()


# Printer initialization
from printer import Printer
printer = Printer()
printer.print_json(b)




