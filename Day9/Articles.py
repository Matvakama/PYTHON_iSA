bike_types = {"cross": "Cross bike", "road": "Road bike", "mountain":"Mountain bike"}

class Bike(object):
    """defines new bike"""
    def __init__(self, color, type, frame, wheel, handlebar = "fitness", seat = "stock seat"):
        """
        :param color:
        :param type:
        :param frame:
        :param wheel:
        """
        self.handlebar = handlebar
        self.seat = seat
        self.color = color
        self.type = type
        self.frame = frame
        self.wheel = wheel

    def ride(self):
        """Ride on the bike"""
        print(f"I'm riding on a {self.color}, bike.")

    def bell(self):
        """Ring the bell."""
        return "RRRRRIIIIINNNG!!"
class ElectricBike(Bike)

class Wheel(object):
    """ Define bike wheel """
    def __init__(self, spokes, diameter, width):
        """
        :param spokes:
        :param diameter:
        :param width:
        """
        self.spokes = spokes
        self.diameter = diameter
        self.width = width


