#my Id ends with 8

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def iterate():
    glViewport(0, 0, 1500, 1500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, 500, -500, 500, 0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def zoneZero(x, y, xc, yc):
    a = y
    b = x
    glBegin(GL_POINTS)
    glVertex2f(a+xc,b+yc)
    zoneOne(a, b, xc, yc)
    zoneTwo(a, b, xc, yc)
    zoneThree(a, b, xc, yc)
    zoneFour(a, b, xc, yc)
    zoneFive(a, b, xc, yc)
    zoneSix(a, b, xc, yc)
    zoneSeven(a, b, xc, yc)

    glEnd()
def zoneOne(x, y, xc, yc):
    a = y
    b = x
    glVertex2f(a + xc, b + yc)

def zoneTwo(x, y, xc, yc):
    a = -y
    b = x
    glVertex2f(a+xc, b+yc)


def zoneThree(x, y, xc, yc):
    a = -x
    b = y
    glVertex2f(a+xc,b+yc)

def zoneFour(x, y, xc, yc):
    a = -x
    b = -y
    glVertex2f(a+xc,b+yc)


def zoneFive(x, y, xc, yc):
    a = -y
    b = -x
    glVertex2f(a+xc,b+yc)

def zoneSix(x, y, xc, yc):
    a = y
    b = -x
    glVertex2f(a+xc,b+yc)

def zoneSeven(x, y, xc, yc):
    a = x
    b = -y
    glVertex2f(a+xc,b+yc)

def midpointCircle(radius, xc, yc):
    d = 1 - radius
    x = 0
    y = radius
    while (y > x):
        if(d < 0):
            d = d + (2*x) + 3
            x = x + 1
            zoneZero(x, y, xc, yc)

        else:
            d = d + (2*x) - (2*y) + 5
            x = x + 1
            y = y - 1
            zoneZero(x, y, xc, yc)




def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)



    midpointCircle(10,-200,100)
    midpointCircle(10,-190,100)
    midpointCircle(10,-180,100)
    midpointCircle(10,-170,100)
    midpointCircle(10,-160,100)
    midpointCircle(10,-150,100)
    midpointCircle(10,-140,100)
    midpointCircle(10,-130,100)
    midpointCircle(10,-120,100)
    midpointCircle(10,-110,100)
    midpointCircle(10,-100,100)

    midpointCircle(10,-100,90)
    midpointCircle(10,-100,80)
    midpointCircle(10,-100,70)
    midpointCircle(10,-100,60)
    midpointCircle(10,-100,50)
    midpointCircle(10,-100,40)
    midpointCircle(10,-100,30)
    midpointCircle(10,-100,20)
    midpointCircle(10,-100,10)
    midpointCircle(10,-100,0)

    midpointCircle(10,-110,0)
    midpointCircle(10,-120,0)
    midpointCircle(10,-130,0)
    midpointCircle(10,-140,0)
    midpointCircle(10,-150,0)
    midpointCircle(10,-160,0)
    midpointCircle(10,-170,0)
    midpointCircle(10,-180,0)
    midpointCircle(10,-190,0)
    midpointCircle(10,-200,0)

    midpointCircle(10, -200, -10)
    midpointCircle(10, -200, -20)
    midpointCircle(10, -200, -30)
    midpointCircle(10, -200, -40)
    midpointCircle(10, -200, -50)
    midpointCircle(10, -200, -60)
    midpointCircle(10, -200, -70)
    midpointCircle(10, -200, -80)
    midpointCircle(10, -200, -90)
    midpointCircle(10, -200, -100)


    midpointCircle(10, -190, -100)
    midpointCircle(10, -180, -100)
    midpointCircle(10, -170, -100)
    midpointCircle(10, -160, -100)
    midpointCircle(10, -150, -100)
    midpointCircle(10, -140, -100)
    midpointCircle(10, -130, -100)
    midpointCircle(10, -120, -100)
    midpointCircle(10, -110, -100)
    midpointCircle(10, -100, -100)

    midpointCircle(10, -100, -90)
    midpointCircle(10, -100, -80)
    midpointCircle(10, -100, -70)
    midpointCircle(10, -100, -60)
    midpointCircle(10, -100, -50)
    midpointCircle(10, -100, -40)
    midpointCircle(10, -100, -30)
    midpointCircle(10, -100, -20)
    midpointCircle(10, -100, -10)
    midpointCircle(10, -100, -0)



    midpointCircle(10,-200,90)
    midpointCircle(10,-200,80)
    midpointCircle(10,-200,70)
    midpointCircle(10,-200,60)
    midpointCircle(10,-200,50)
    midpointCircle(10,-200,40)
    midpointCircle(10,-200,30)
    midpointCircle(10,-200,20)
    midpointCircle(10,-200,10)
    midpointCircle(10,-200,0)



    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab03") #window name
glutDisplayFunc(showScreen)

glutMainLoop()