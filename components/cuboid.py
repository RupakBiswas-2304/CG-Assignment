from OpenGL.GL import *
from OpenGL.GLU import *
import numpy
import math

from components.mesh import Mesh


class Cuboid(Mesh):
    def __init__(self, x, y, z, color = (0,0,1)) -> None:
        super().__init__(4, color)
        self.generateCuboid(x,y,z)
        self.generateEdges()

    def generateCuboid(self, x, y, z):
        self.vertices.append([x, y, z])
        self.vertices.append([x, -y, z])
        self.vertices.append([-x, -y, z])
        self.vertices.append([-x, y, z])
        self.vertices.append([x, y, -z])
        self.vertices.append([x, -y, -z])
        self.vertices.append([-x, -y, -z])
        self.vertices.append([-x, y, -z])

    def generateEdges(self):
        self.edges.append((0, 1))
        self.edges.append((1, 2))
        self.edges.append((2, 3))
        self.edges.append((3, 0))
        self.edges.append((4, 5))
        self.edges.append((5, 6))
        self.edges.append((6, 7))
        self.edges.append((7, 4))
        self.edges.append((0, 4))
        self.edges.append((1, 5))
        self.edges.append((2, 6))
        self.edges.append((3, 7))

    def scaleEdges(self, scale):
        new_vertices = list(numpy.multiply(numpy.array(self.vertices), scale))
        self.vertices = new_vertices

    def translateXYZ(self, x, y, z):
        new_vertices = list(numpy.add(numpy.array(self.vertices), [x, y, z]))
        self.vertices = new_vertices

    def rotate(self, angle, axis):
        new_vertices = list(numpy.dot(numpy.array(self.vertices), numpy.array([[math.cos(angle), 0, -math.sin(angle)], [0, 1, 0], [ math.sin(angle), 0, math.cos(angle)]])))
        self.vertices = new_vertices

    