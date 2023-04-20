import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

from components.car import Car
from components.grid import Grid, rgb


# settings
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 920


def main():
    pygame.init()
    display = (SCREEN_WIDTH, SCREEN_HEIGHT)
    # set pygame up for 3d graphics
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # pygame.mouse.set_visible(False)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    # Settup camera
    t_x, t_y, t_z = -5, -5, -15
    glTranslatef(t_x, t_y, t_z)
    # now apply rottation so that it looks at the center
    glRotatef(0, 0, 0, 0)

    # draw pyramid as a solid object
    glEnable(GL_DEPTH_TEST)

    c1 = Car(rgb(200, 200, 1), (0, 0, 0), (0, 0, 0))
    # c1.rotate(math.radians(45), 'y')
    c2 = Car(rgb(255, 255, 255), (10, 0, 10), (0, 45, 0))
    c3 = Car(rgb(178, 164, 255), (0, 0, 10), (0, 45, 0))
    c4 = Car(rgb(255, 180, 180), (20, 0, 0), (0, 90, 0))
    g1 = Grid()

    velocity = 0.1

    clock = pygame.time.Clock()

    # camera settings

    while True:
        clock.tick(60)
        # continually rotate pyramid
        glRotatef(velocity * 1.1, 0, 1, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_w] and keys[pygame.K_d]:
        #     c1.turnCar((0,0.1,0), True)
        #     # c1.rotate(0.01, 'y')

        # elif keys[pygame.K_w]:
        #     c1.moveForward(.005, True)
        # elif keys[pygame.K_s]:
        #     c1.moveForward(.005, False)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        c1.draw()
        c2.draw()
        c2.rotate(0.01, 'y')
        c3.draw()
        c3.rotate(0.03, 'y')
        c4.draw()
        c4.rotate(0.02, 'y')
        g1.draw()

        # p.draw()
        # p2.draw()
        pygame.display.flip()


if __name__ == '__main__':
    main()
