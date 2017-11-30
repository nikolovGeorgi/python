import numpy as np

class Nature():
    def __init__(self):
        self.__data = {}

    def get_night_hours(self, prompt, retries=4, reminder='Please try again!'):
        hours = [k for k in list(np.arange(0., 24., .01))]
        while True:
            night = float(input(prompt))
            print(night)
            if night in hours:
                self.__data['night'] = night
                return True
            retries = retries - 1
            if retries < 0:
                raise ValueError('Invalid user response')
            print(reminder)

    def night_day_ratio(self):
        if not self.__data:
            self.get_night_hours('How long is the night in hours value?')
        self.__data['day'] = 24 - self.__data['night']

    def run(self):
        self.night_day_ratio()

    def data(self):
        self.run()
        return self.__data










