from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

from components.mesh import Mesh, rgb
from components.cuboid import Cuboid
from components.cylinder import Cylinder


def calculate_next_position(previous_position, current_position, distance):
    """
    Calculates the next position of a given 3D object, given the previous position,
    current position, and distance from the current position to the next position.

    Args:
        previous_position (tuple or list): The previous position of the object as a tuple or list of three coordinates (x, y, z).
        current_position (tuple or list): The current position of the object as a tuple or list of three coordinates (x, y, z).
        distance (float): The distance from the current position to the next position.

    Returns:
        tuple: The next position of the object as a tuple of three coordinates (x, y, z).
    """
    # Convert inputs to numpy arrays for vector operations
    previous_position = np.array(previous_position)
    current_position = np.array(current_position)

    # Calculate the direction vector from previous position to current position
    direction_vector = current_position - previous_position

    # Normalize the direction vector
    direction_vector_normalized = direction_vector / \
        np.linalg.norm(direction_vector)

    # Calculate the next position by adding the normalized direction vector scaled by the distance
    next_position = current_position + (direction_vector_normalized * distance)

    # Return the next position as a tuple
    print(current_position, "->", next_position)
    return tuple(next_position)


class Wheel():
    def __init__(self, initalPos=(0, 0, 0), initialRotation=(0, 0, 0)) -> None:
        self.w1 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w1.setAxis('z')
        self.w1.setOrigin(1,0.5, 1)

        self.w2 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w2.setAxis('z')
        self.w2.setOrigin(-1,0.5, 1)

        self.w3 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w3.setAxis('z')
        self.w3.setOrigin(1, 0.5,  -1)

        self.w4 = Cylinder(25, 0.5, 0.1, 4, rgb(86, 113, 137))
        self.w4.setAxis('z')
        self.w4.setOrigin(-1, 0.5, -1)

        self.rotate(math.radians(initialRotation[1]), 'y')
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


class Body():
    def __init__(self, bodyColor, initalPos=(0, 0, 0), initialRotation=(0, 0, 0)) -> None:
        self.buttomCuboid = Cuboid(2, 0.5, 1, bodyColor)
        self.buttomCuboid.rotate(math.radians(initialRotation[1]), 'y')
        self.buttomCuboid.translateXYZ(0, 1 , 0)

        self.upperCuboid = Cuboid(1, 0.5, 1, bodyColor)

        self.upperCuboid.rotate(math.radians(initialRotation[1]), 'y')
        self.upperCuboid.translateXYZ(0 , 2, 0)

        self.translateXYZ(initalPos)

    def draw(self):
        self.buttomCuboid.draw()
        self.upperCuboid.draw()

    def translateXYZ(self, position):
        self.buttomCuboid.translateXYZ(position[0], position[1], position[2])
        self.upperCuboid.translateXYZ(position[0], position[1], position[2])

    def rotate(self, angle, axis):
        self.buttomCuboid.rotate(angle, axis)
        self.upperCuboid.rotate(angle, axis)


class Car:
    def __init__(self, bodyColor: tuple, initialPosition: tuple = (0, 0, 0), initialRotation: tuple = (0, 0, 0)):
        self.wheel = Wheel(initialPosition, initialRotation)
        self.body = Body(bodyColor, initialPosition, initialRotation)

        self.position = initialPosition
        self.prevPosition = (
            initialPosition[0] - 1, initialPosition[1], initialPosition[2])
        self.distance = 0

    def draw(self):
        self.body.draw()
        self.wheel.draw()

    def moveForward(self, distance: float):
        _tmpPos = self.position
        # check if the self.distance and distance have same sign
        if (self.distance * distance) > 0:
            self.distance += distance
            self.position = calculate_next_position(
                self.prevPosition, self.position, self.distance)
        else:
            self.distance = distance
            self.position = calculate_next_position(
                self.prevPosition, self.position, self.distance)

        self.prevPosition = _tmpPos

        self.body.translateXYZ(self.position)
        self.wheel.translateXYZ(self.position)

    def rotate(self, angle, axis):
        self.body.rotate(angle, axis)
        self.wheel.rotate(angle, axis)

        # get the center of rotation
        # if direction == 0 : # left
        # center a point just left side of the car with radius amount of distance
