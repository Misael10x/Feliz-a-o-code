import tkinter as tk
import random
from math import sin, cos, radians

class FireworkAnimation:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.particles = []
        self.create_particles()
