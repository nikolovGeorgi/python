class ConstructJSON:
    def __init__(self, field, current_field):
        self.field = field
        self.current_field = current_field

    def set_data(self):
        self.execute_data()
        self.current_field['N'] = self.current_field['variables'][0]
        self.current_field['W'] = self.current_field['variables'][1]
        self.current_field['k'] = self.current_field['variables'][2]

    def execute_data(self):
        self.current_field = self.field.data()

    def get_data(self):
        self.set_data()
        return self.current_field
