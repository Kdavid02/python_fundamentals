# horse Class

class horse:
    def __init__(self, hair_color, shoe_color, tail_length):
        self.hair_color = hair_color
        self.shoe_color = shoe_color
        self.tail_length = tail_length
    def leg_kick(self):
        print("Horse's legs have kicked back")
    @property
    def hair_color(self):
        return self.hair_color
    @hair_color.setter
    def hair_color(self):
        def hair_color(self, p_color):
            self.hair_color = p_color
    @property
    def shoe_color(self):
        return self.shoe_color
    @shoe_color.setter
    def shoe_color(self, shoe_color):
        self.shoe_color = shoe_color
    @property
    def tail_length(self):
        return self.tail_length
    @tail_length.setter
    def tail_length(self, tail_length):
        tail_length = tail_length

horse_1 = horse('black', 'white', 'short')