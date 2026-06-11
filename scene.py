from tkinter import Canvas
import numpy as np

class Scene(Canvas):

    def __init__(self, master, width = 1000, height = 1000):

        super().__init__(master, width = width, height = height)


    def render(camera : Camera):
        pass


    


class Camera:

    def __init__(self, position = np.array([-10, 0, 0]), orientation = np.array([[1.0, 0.0, 0.0],
                                                                                    [0.0, 1.0, 0.0],
                                                                                    [0.0, 0.0, 1.0]])):
        self.position = position
        self.orientation = orientation

