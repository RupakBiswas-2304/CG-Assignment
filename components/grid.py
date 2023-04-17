from OpenGL.GL import *
from OpenGL.GLU import *
import numpy
import math

from components.mesh import Mesh, rgb


class Grid(Mesh):
    def __init__(self ) -> None:
        super().__init__(1, rgb(0, 200, 0))

        self.length = 50
        self.width = 50

        self.generateGrid()
        self.generateEdges()

    def generateGrid(self):
        for i in range(self.length):
            self.vertices.append([i, 0, self.width])
            self.vertices.append([i, 0, -self.width])

            self.vertices.append([-i, 0, self.width])
            self.vertices.append([-i, 0, -self.width])
        
        for i in range(self.width):
            self.vertices.append([self.length, 0, i])
            self.vertices.append([-self.length, 0, i])

            self.vertices.append([self.length, 0, -i])
            self.vertices.append([-self.length, 0, -i])

    def generateEdges(self):
        for i in range(len(self.vertices)//2):
            self.edges.append((i*2, i*2+1))
        
class NoiseLandscape(Grid):
    def __init__(self) -> None:
        super().__init__()
    
    def addNoise(self):
        pass
    