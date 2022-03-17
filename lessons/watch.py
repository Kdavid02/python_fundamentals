# watch Class

class watch:
    def __init__(self, crown_style, casing_material, gear_size):
        self.crown_style = crown_style
        self.casing_material = casing_material
        self.gear_size = gear_size
    def turn_crown(self):
        print("hand adjustment knob turned clockwise")
    @property
    def crown_style(self):
        return self.crown_style
    @crown_style.setter
    def crown_style(self):
        def crown_style(self, crown_style):
            self.crown_style = crown_style
    @property
    def casing_material(self):
        return self.casing_material
    @casing_material.setter
    def casing_material(self, casing_material):
        self.casing_material = casing_material
    @property
    def gear_size(self):
        return self.gear_size
    @gear_size.setter
    def gear_size(self, gear_size):
        gear_size = gear_size


watch_1 = watch('silver', 'gold', 'small')
