from printer.printer import Printer
from data import Data

# data = Data('../fields/test.txt').data()
# data2 = Data('../fields/CastleBlack.txt').data()
data3 = Data('../fields/FistOfTheFirstMen.txt').data()
# data4 = Data('../fields/Hardhome.txt').data()
# data5 = Data('../fields/Winterfell.txt').data()
printer = Printer(data3)
printer.print_form()
