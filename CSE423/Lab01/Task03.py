from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#My id is 18201058

def ddaLineGen(x0, y0, x1, y1):
    linePoints = []
    x, y = x0, y0
    linePoints.append([x, y])
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    steps = max(dx, dy)
    xIncrement = dx/steps
    yIncrement = dy/steps
    for i in range(steps):
        x = x + xIncrement
        y = y + yIncrement
        linePoints.append([x, y])
    return linePoints

def ddaDashedLineGen(x0, y0, x1, y1):
    linePoints = []
    x, y = x0, y0
    linePoints.append([x, y])
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    steps = max(dx, dy)
    xIncrement = dx/steps
    yIncrement = dy/steps
    for i in range(steps):
        x = x + xIncrement
        y = y + yIncrement
        if i%5!=0:
            linePoints.append([x, y])
    return linePoints

def linePrinter(lines):
    #glPointSize(2)
    glBegin(GL_POINTS)
    for i in lines:
        glVertex2f(round(i[0]), round(i[1]))
    glEnd()

horizontalLine = ddaDashedLineGen(125, 400, 375, 400)
verticalLine = ddaLineGen(250, 100, 250, 400)

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
    glColor3f(1.0, 0.0, 3.0)
    #call the draw methods here
    linePrinter(horizontalLine)
    linePrinter(verticalLine)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab01 Task03")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()