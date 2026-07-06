import numpy as np

from numpy import array

class AStuff:
    def __init__(self):
        pass


class Line:

    def __init__(self, direction):
        super().__init__()

        if direction == "Z":
            self.direction = array([0.0, 0.0, 1.0])
        if direction == "Y":
            self.direction = array([0.0, 1.0, 0.0])
        if direction == "X":
            self.direction = array([1.0, 0.0, 0.0])