from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math


def rgb(r: int, g: int, b: int) -> tuple:
    return (r/255, g/255, b/255)


class Mesh:
    def __init__(self, linewidth: int = 5, color: tuple = (0, 0, 1)) -> None:
        self.vertices = []
        self.edges = []
        self.surfaces = []

        self.linewidth = linewidth
        self.color = color

    def draw(self):
        self.fill_sides()
        glLineWidth(self.linewidth)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(*self.color)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def fill_sides(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(0.45, 0.482, 0)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def translateXYZ(self, position: tuple):
        self.vertices =  list(np.array(self.vertices) + np.array(position))

    def rotateY(self, angle):
        self.vertices = list(np.dot(np.array(self.vertices), np.array([[math.cos(angle), 0, -math.sin(angle)], [0, 1, 0], [math.sin(angle), 0, math.cos(angle)]])))

    def rotateX(self, angle):
        self.vertices = list(np.dot(np.array(self.vertices), np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])))

    def rotateZ(self, angle):
        self.vertices = list(np.dot(np.array(self.vertices), np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])))

    def rotate(self, angle: tuple):
        self.vertices = self.rotateZ(self.rotateY(self.rotateX(self.vertices, angle[0]), angle[1]), angle[2])

    def routateP(self, angle: tuple, point: tuple):
        self.vertices = self.translateXYZ(
            self.vertices, (-point[0], -point[1], -point[2]))
        self.vertices = self.rotate(self.vertices, angle)
        self.vertices = self.translateXYZ(self.vertices, (point[0], point[1], point[2]))
        
