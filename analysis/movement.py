import numpy


class MovementData:
    def __init__(self, trial_name, trial_number, trial_time, x, y, rotation):
        self.y = y
        self.x = x
        self.trial_time = trial_time
        self.trial_name = trial_name
        self.trial_number = trial_number
        self.rotation = rotation

    def get_vector(self):
        return numpy.array([float(self.x), float(self.y)])

    @staticmethod
    def from_str(s=""):
        elements = [element.strip() for element in s.split(",")]
        if len(elements) < 6:
            return None
        return MovementData(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5])

