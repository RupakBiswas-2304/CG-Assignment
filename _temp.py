import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

# Initialize Pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Camera Rotation Example")

# Initial camera parameters
camera_yaw = 0.0
camera_pitch = 0.0

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse movement
    mouse_dx, mouse_dy = pygame.mouse.get_rel()

    # Update camera rotation based on mouse movement
    camera_yaw += mouse_dx * 0.1
    camera_pitch += mouse_dy * 0.1

    # Clamp camera pitch to avoid over-rotating
    camera_pitch = max(min(camera_pitch, 90.0), -90.0)

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Set up the modelview matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotatef(camera_pitch, 1, 0, 0)
    glRotatef(camera_yaw, 0, 1, 0)

    # Render your scene here

    # Draw a cube as an example
    glBegin(GL_QUADS)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glEnd()

    # Update the display
    pygame.display.flip()
