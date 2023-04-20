from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

from components.mesh import Mesh, rgb
from components.cuboid import Cuboid
from components.cylinder import Cylinder


class Wheel:
    def __init__(self, initalPos=(0, 0, 0), initialRotation=(0, 0, 0)) -> None:
        self.w1 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w1.setAxis("z")
        self.w1.setOrigin(1, 0.5, 1)

        self.w2 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w2.setAxis("z")
        self.w2.setOrigin(-1, 0.5, 1)

        self.w3 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w3.setAxis("z")
        self.w3.setOrigin(1, 0.5, -1)

        self.w4 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w4.setAxis("z")
        self.w4.setOrigin(-1, 0.5, -1)

        self.rotate(math.radians(initialRotation[1]), "y")
        self.translateXYZ(initalPos)

    def draw(self):
        self.w1.draw()
        self.w2.draw()
        self.w3.draw()
        self.w4.draw()

    def translateXYZ(self, position):
        self.w1.setOrigin(*position)
        self.w2.setOrigin(*position)
        self.w3.setOrigin(*position)
        self.w4.setOrigin(*position)

    def rotate(self, angle, axis):
        self.w1.rotateY(angle)
        self.w2.rotateY(angle)
        self.w3.rotateY(angle)
        self.w4.rotateY(angle)

    def rotatePivot(self, angle, pivotpoint):
        self.w1.rotateP(angle, pivotpoint)
        self.w2.rotateP(angle, pivotpoint)
        self.w3.rotateP(angle, pivotpoint)
        self.w4.rotateP(angle, pivotpoint)


class Body:
    def __init__(
        self, edgeColor, bodyColor, initalPos=(0, 0, 0), initialRotation=(0, 0, 0)
    ) -> None:
        self.buttomCuboid = Cuboid(2, 0.5, 1, edgeColor, bodyColor)
        self.buttomCuboid.rotateY(math.radians(initialRotation[1]))
        self.buttomCuboid.translateXYZ((0, 1, 0))

        self.upperCuboid = Cuboid(1, 0.5, 1, edgeColor, bodyColor)

        self.upperCuboid.rotateY(math.radians(initialRotation[1]))
        self.upperCuboid.translateXYZ((0, 2, 0))

        self.translateXYZ(initalPos)

    def draw(self):
        self.buttomCuboid.draw()
        self.upperCuboid.draw()

    def translateXYZ(self, position):
        self.buttomCuboid.translateXYZ(position)
        self.upperCuboid.translateXYZ(position)

    def rotate(self, angle, axis):
        if axis == "y":
            self.buttomCuboid.rotateY(angle)
            self.upperCuboid.rotateY(angle)
        else:
            pass

    def rotatePivot(self, angle, pivotpoint):
        self.buttomCuboid.rotateP(angle, pivotpoint)
        self.upperCuboid.rotateP(angle, pivotpoint)


class Car:
    def __init__(
        self,
        edgeColor: tuple,
        bodyColor: tuple,
        initialPosition: tuple = (0, 0, 0),
        initialRotation: tuple = (0, 0, 0),
    ):
        self.wheel = Wheel(initialPosition, initialRotation)
        self.body = Body(edgeColor, bodyColor, initialPosition, initialRotation)

        self.position = initialPosition
        self.prevPosition = (
            initialPosition[0] - 1,
            initialPosition[1],
            initialPosition[2],
        )
        self.distance = 0

    def draw(self):
        self.body.draw()
        self.wheel.draw()

    def calculateNextPoint(self, distance, isForward):
        _directionVector = np.subtract(self.position, self.prevPosition)
        _directionVector = _directionVector / np.linalg.norm(_directionVector)

        # print(_directionVector)

        self.prevPosition = self.position
        if isForward:
            self.position = np.add(self.position, _directionVector * distance)
        else:
            self.position = np.subtract(self.position, _directionVector * distance)

    def moveForward(self, distance, isForward=True):
        self.calculateNextPoint(distance, isForward)
        self.translateXYZ()

    def calculateRotationCenter(self, isLeft=True):
        return (0, 0, 0)

    def turnCar(self, angle, isLeft=True):
        pivotpoint = self.calculateRotationCenter(isLeft)
        print("Turn Car :", pivotpoint, angle)
        self.wheel.rotatePivot(angle, pivotpoint)
        self.body.rotatePivot(angle, pivotpoint)

    def rotate(self, angle, axis):
        self.body.rotate(angle, axis)
        self.wheel.rotate(angle, axis)

    def translateXYZ(self):
        self.body.translateXYZ(self.position)
        self.wheel.translateXYZ(self.position)
