# guitar Class

class guitar:
    def __init__(self, wood_type, string_type, hole_size):
        self.wood_type = wood_type
        self.string_type = string_type
        self.hole_size = hole_size
    def pluck_strings(self):
        print("A sound has rung out from the plucked strings")
    @property
    def wood_type(self):
        return self.wood_type
    @wood_type.setter
    def wood_type(self):
        def wood_type(self, p_color):
            self.wood_type = p_color
    @property
    def string_type(self):
        return self.string_type
    @string_type.setter
    def string_type(self, string_type):
        self.string_type = string_type
    @property
    def hole_size(self):
        return self.hole_size
    @hole_size.setter
    def hole_size(self, hole_size):
        hole_size = hole_size

guitar_1 = guitar('maple', 'nylon', 'large')