from printer.printer import Printer
from data import Data

# data = Data('../fields/test.txt').data()
data1 = Data('../fields/test2.txt').data()
# data2 = Data('../fields/FistOfTheFirstMen.txt').data()
# data3 = Data('../fields/Hardhome.txt').data()
# data4 = Data('../fields/CastleBlack.txt').data()
# data5 = Data('../fields/Winterfell.txt').data()

# printer = Printer(data)
printer = Printer(data1)
# printer = Printer(data2)
# printer = Printer(data3)
# printer = Printer(data4)
# printer = Printer(data5)

printer.print_form()
