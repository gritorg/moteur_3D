from tkinter import Canvas
import numpy as np
from stuff import AStuff, Line

class Scene(Canvas):

    def __init__(self, master, width = 1000, height = 1000):

        super().__init__(master, width = width, height = height)

    def project(self, camera : Camera, pt : np.array):
        new_pt = camera.R.dot(pt - camera.position)
        x, y, z = new_pt[0], new_pt[1], new_pt[2]
        k = camera.zoom
        return (2*y/(x+k), 2*z/(x+k))
    
    def show_line(self, line : Line, camera):
        x, y = self.project(camera, line.direction)
        self.create_line(0, 0, x, y, width=3)

    def add_stuff(stuff: AStuff):
        pass


class Camera:

    def __init__(self, 
                 position = np.array([-10, 0, 0]), 
                 orientation = np.array([[1.0, 0.0, 0.0],
                                         [0.0, 1.0, 0.0],
                                         [0.0, 0.0, 1.0]]),
                 zoom =1):
        
        self.position = position
        self.orientation = orientation
        self.zoom = zoom

    @property
    def R(self):
        return self.orientation
        
