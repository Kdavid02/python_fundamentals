# Boat Class

class Boat:
    def __init__(self, paint_color, engine_type, rudder_type):
        self.paint_color = paint_color
        self.engine_type = engine_type
        self.rudder_type = rudder_type
    def spin_rudder(self):
        print("The rudder has spinned clockwise.")
    @property
    def paint_color(self):
        return self.paint_color
    @paint_color.setter
    def paint_color(self):
        def paint_color(self, p_color):
            self.paint_color = p_color
    @property
    def engine_type(self):
        return self.engine_type
    @engine_type.setter
    def engine_type(self, engine_type):
        self.engine_type = engine_type
    @property
    def rudder_type(self):
        return self.rudder_type
    @rudder_type.setter
    def rudder_type(self, rudder_type):
        rudder_type = rudder_type

boat_1 = Boat('red', 'small', 'large')


