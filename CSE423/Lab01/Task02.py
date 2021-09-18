from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def drawHouseBuilding():

    #roof part
    glBegin(GL_TRIANGLES)
    glVertex2f(300, 250)
    glVertex2f(250, 300)
    glVertex2f(200, 250)
    glEnd()


    glBegin(GL_LINES)
    #body part
    glVertex2f(200, 250)
    glVertex2f(200, 150)

    glVertex2f(200, 150)
    glVertex2f(300, 150)

    glVertex2f(300, 150)
    glVertex2f(300, 250)

    #door part
    glVertex2f(235, 150)
    glVertex2f(235, 190)

    glVertex2f(235, 190)
    glVertex2f(265, 190)

    glVertex2f(265, 190)
    glVertex2f(265, 150)

    #left window
    glVertex2f(235, 200)
    glVertex2f(210, 200)

    glVertex2f(210, 200)
    glVertex2f(210, 230)

    glVertex2f(210, 230)
    glVertex2f(235, 230)

    glVertex2f(235, 230)
    glVertex2f(235, 200)

    # right window
    glVertex2f(290, 200)
    glVertex2f(265, 200)

    glVertex2f(265, 200)
    glVertex2f(265, 230)

    glVertex2f(265, 230)
    glVertex2f(290, 230)

    glVertex2f(290, 230)
    glVertex2f(290, 200)
    glEnd()

    #door dot
    glBegin(GL_POINTS)
    glVertex2f(260, 175)
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
    glColor3f(1.0, 0.0, 0.0)
    #call the draw methods here
    drawHouseBuilding()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab01 Task02")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()