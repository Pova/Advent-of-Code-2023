import pygame
import numpy as np
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_plane():
    glColor3f(0.4, 0.4, 0.4)  # Grey color for the plane
    glBegin(GL_QUADS)
    glVertex3f(-200, -200, 0.5)
    glVertex3f(-200, 200, 0.5)
    glVertex3f(200, 200, 0.5)
    glVertex3f(200, -200, 0.5)
    glEnd()

def draw_grid():
    glColor3f(.8, .8, .8)  # White color for the grid lines
    for x in range(-50, 51, 1):  # Adjust range and step for your grid size and spacing
        glBegin(GL_LINES)
        # Horizontal lines
        glVertex3f(x+0.5, -50+0.5, 0.5)  
        glVertex3f(x+0.5, 50+0.5, 0.5)
        # Vertical lines
        glVertex3f(-50+0.5, x+0.5, 0.5)  
        glVertex3f(50+0.5, x+0.5, 0.5)
        glEnd()

def draw_axes():
    glBegin(GL_LINES)
    # X axis in red
    glColor3f(1, 0, 0)  # Red
    glVertex3f(0, 0, 0)
    glVertex3f(50, 0, 0)

    # Y axis in green
    glColor3f(0, 1, 0)  # Green
    glVertex3f(0, 0, 0)
    glVertex3f(0, 50, 0)

    # Z axis in blue
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 50)
    glEnd()


def Cube(position, cube_colour = (0.5, 0.5, 0.5), alpha=1.0):
    x, y, z = position
    vertices = (
        (x + 0.5, y - 0.5, z - 0.5),
        (x + 0.5, y + 0.5, z - 0.5),
        (x - 0.5, y + 0.5, z - 0.5),
        (x - 0.5, y - 0.5, z - 0.5),
        (x + 0.5, y - 0.5, z + 0.5),
        (x + 0.5, y + 0.5, z + 0.5),
        (x - 0.5, y - 0.5, z + 0.5),
        (x - 0.5, y + 0.5, z + 0.5)
    )
    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    )
    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glColor3f(cube_colour[0], cube_colour[1], cube_colour[2]) 
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3f(.1, .1, .1)  # Dark grey for the edges

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    # Read the file and print each line
    try:
        # Open and read the file
        with open('../test.txt', 'r') as file:
            lines = file.read().strip().split('\n')

    except FileNotFoundError:
        # Specific exception for a clearer error message
        print('Input file not found.')

    except Exception as e:
        # Catch other exceptions and print the error
        print(f'An error occurred: {e}')

    # Initialize pygame and OpenGL
    pygame.init()

    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Set up the perspective
    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)

    # Adjust the camera position and orientation
    gluLookAt(20.1, 20.1, 3.1,  # Camera position (x, y, z)
              0, 0, 2,     # Look-at point (center)
              0, 0, 1)     # Up vector (usually Y-axis)

    # Set the background color to dark blue

    glClearColor(135./255, 211./255, 248./255, 1.0)

    # glEnable(GL_DEPTH_TEST) # Enable depth testing for z-culling

    cube_colours = []

    for line in lines:

        rand_r = random.random()
        rand_g = random.random()
        rand_b = random.random()

        cube_colours.append((rand_r, rand_g, rand_b))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # Clear the screen and depth buffer

        draw_plane()
        draw_grid()

        for j, line in enumerate(lines):
            # Split the input line into start and end coordinates
            start_coords, end_coords = line.split('~')
            start_coords = [int(coord) for coord in start_coords.split(',')]
            end_coords = [int(coord) for coord in end_coords.split(',')]

            # Identify the dimension that changes and calculate the range
            diff_idx = -1
            for idx in range(len(start_coords)):
                if start_coords[idx] != end_coords[idx]:
                    diff_idx = idx
                    # Calculate the length of the path along the changing dimension
                    length = abs(start_coords[idx] - end_coords[idx]) + 1
                    break

            # Draw cubes along the path
            if diff_idx == -1:
                Cube(tuple(start_coords), cube_colours[j], 0.5)
            for i in range(length):
                # Calculate the position for the current cube
                current_pos = start_coords.copy()
                current_pos[diff_idx] += (i if start_coords[diff_idx] < end_coords[diff_idx] else -i)
                
                Cube(tuple(current_pos), cube_colours[j], 0.5)
                #Cube(tuple(current_pos), (90./255, 77./255, 65./255), 0.5)

        draw_axes()

        pygame.display.flip()
        pygame.time.wait(10)

main()