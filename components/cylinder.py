from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

from components.mesh import rgb , Mesh

class Cylinder(Mesh):
    '''
    Use n>20 for using this as a cylinder
    '''
    def __init__(self, n,radius ,height,  linewidth: int = 5, color: tuple = (0, 0, 1)) -> None:
        super().__init__(linewidth, color)
        self.n = n
        self.r = radius
        self.h = height
        self.geneatePoly(self.n)
        self.generateEdges(self.n)

    def geneatePoly(self, n):
        angle = 360 / n
        for i in range(n):
            p,q = self.r*math.cos(math.radians(angle * i)), self.r*math.sin(math.radians(angle * i))
            self.vertices.append([p, q, self.h])
        for i in range(n):
            self.vertices.append([self.vertices[i][0], self.vertices[i][1], -self.h])

    def generateEdges(self, n):
        for i in range(n):
            self.edges.append((i, (i + 1) % n))
            self.edges.append((n+i, (i + 1) % n + n))
            self.edges.append((i, n+i))
    
    def elongate(self, scale):
        new_vertices = list(np.add(np.array(self.vertices[:self.n]), [0,0,scale]))
        new_vertices += list(np.add(np.array(self.vertices[self.n:]), [0,0,-scale]))
        self.vertices = new_vertices

    def setOrigin(self, x, y, z):
        new_vertices = list(np.add(np.array(self.vertices), [x, y, z]))
        self.vertices = new_vertices

    def setAxis(self, axis):
        if axis == 'x':
            self.rotateY(90)
        elif axis == 'y':
            self.rotateX(90)
        elif axis == 'z':
            self.rotateZ(90)

    