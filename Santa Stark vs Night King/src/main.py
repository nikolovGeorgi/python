from printer.printer import Printer
from data import Data

files = [
    '../fields/test.txt',
    '../fields/test2.txt',
    '../fields/FistOfTheFirstMen.txt',
    '../fields/Hardhome.txt',
    '../fields/CastleBlack.txt',
    '../fields/Winterfell.txt'
]
data = Data(files[1])
data._set_probability(2)
printer = Printer(data.data())
printer.print_form()
