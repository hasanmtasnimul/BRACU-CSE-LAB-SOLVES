from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midPointLineDrawingAlgo(x1, y1, x2, y2):
    slope = 0

    if x2-x1==0:
        slope = y2 - y1
    else:
        slope = (y2 - y1)/(x2 - x1)

    if abs(slope)<1:
        if x1>x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = abs(x2-x1)
        dy = abs(y2-y1)
        d = 2*dy - dx

        x = x1
        y = y1

        while x<=x2:
            glVertex2f(x, y)
            x+=1

            if d>=1:
                if slope<1:
                    y+=1
                else:
                    y-=1
                d+=2*dy-2*dx
            else:
                d+=2*dy

    if abs(slope)>=1:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        d = 2 * dy - dx

        x = x1
        y = y1

        while y <= y2:
            glVertex2f(x, y)
            y += 1

            if d >= 0:
                if slope >= 1:
                    x += 1
                else:
                    x -= 1
                d += (2 * dx) - (2 * dy)
            else:
                d += 2 * dx



def draw_line(x1, y1, x2, y2):
    glPointSize(1)
    glBegin(GL_POINTS)
    midPointLineDrawingAlgo(x1, y1, x2, y2)
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
    glColor3f(1.0, 1.0, 0.0)
    #call the draw methods here
    #drawing for 5
    draw_line(50,400, 100, 400)
    draw_line(50,400, 50, 350)
    draw_line(50,350, 100, 350)
    draw_line(100, 350, 100, 300)
    draw_line(100, 300, 50, 300)

    #drawing for 8
    draw_line(120, 400, 170, 400)
    draw_line(170, 400, 170, 350)
    draw_line(170, 350, 120, 350)
    draw_line(120, 350, 120, 400)

    draw_line(170, 400, 170, 300)
    draw_line(170, 300, 120, 300)
    draw_line(120, 300, 120, 350)

    #house

    #roof part
    draw_line(300, 400, 250, 350)
    draw_line(300, 400, 350, 350)
    draw_line(250, 350, 350, 350)

    #body part
    draw_line(350, 350, 350, 300)
    draw_line(350, 300, 250, 300)
    draw_line(250, 300, 250, 350)

    #door part
    draw_line(280, 335, 320, 335)
    draw_line(280, 335, 280, 300)
    draw_line(320, 335, 320, 300)







    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab02") #window name
glutDisplayFunc(showScreen)

glutMainLoop()