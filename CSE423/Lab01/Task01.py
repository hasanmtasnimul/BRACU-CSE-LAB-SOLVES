from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

randomPoint = []
for i in range(50):
    randomPoint.append([random.randint(0, 500), random.randint(0, 500)])

def randomPointGenerator():
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in randomPoint:
        glVertex2f(i[0], i[1])
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)
    #call the draw methods here
    randomPointGenerator()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab01 Task01")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()