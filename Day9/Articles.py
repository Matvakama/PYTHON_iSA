bike_types = {"cross": "Cross bike", "road": "Road bike", "mountain":"Mountain bike"}

class Bike(object):
    """defines new bike"""
    def __init__(self, color, type, frame, wheel, ):
        """
        :param color:
        :param type:
        :param frame:
        :param wheel:
        """
        self.handlebar = "fitness"
        self.seat = "stock seat"
        self.color = color
        self.type = type
        self.frame = frame
        self.wheel = wheel

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


