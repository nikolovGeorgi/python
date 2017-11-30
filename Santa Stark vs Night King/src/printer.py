import json
class Printer:
    def __init__(self, data):
        self.data = data

    def print_json(self):
        print(json.dumps(self.data, indent=4, sort_keys=True))

    def print_obj(self):
        for k, v in self.data.items():
            print(k, v)

    def set_total_cell_defences(self):
        printer = {
            'printer': {
                    'static defences': [sum(i) for i in zip(*self.data['field']['grid'])]
                }
        }
        self.data.update(printer)

    def set_total_cell_defences_effect(self):
        ## TODO: doubling with battle calculations ? <- Fix
        self.data['printer']['static defences effect'] = [a - b for a, b in zip(self.data['enemy']['grid'], self.data['printer']['static defences'])]

    def run(self):
        self.set_total_cell_defences()
        self.set_total_cell_defences_effect()

    def print_total_cell_defences(self):
        print(self.data['printer']['static defences'])

    def print_total_static_defences_effect(self):
        print(self.data['printer']['static defences effect'])


