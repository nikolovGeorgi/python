import json
class Printer:
    def __init__(self):
        pass

    def print_json(self, data):
        print(json.dumps(data, indent=4, sort_keys=True))





