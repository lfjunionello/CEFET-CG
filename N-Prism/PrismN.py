from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import math 

a = 0
n = 5
colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )



def draw_prism():
    height = 4

    angle = (2*math.pi)/n

    radius = 2
    bottom_vertices = []
    top_vertices = []

    glPushMatrix()
    glTranslatef(0,-1,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-60,1.0,0.0,0.0)
    glColor3fv(colors[0])

    # Bottom vertices
    glBegin(GL_POLYGON)
    for i in range(0,n):
        x = radius * math.cos(i*angle)
        y = radius * math.sin(i*angle)
        bottom_vertices += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    # Top vertices
    glBegin(GL_POLYGON)
    for i in range(0,n):
        x = radius * math.cos(i*angle)
        y = radius * math.sin(i*angle)
        top_vertices += [ (x,y) ]
        glVertex3f(x,y,height)
    glEnd()

    #Faces
    glBegin(GL_QUADS)
    for i in range(0,n):
        glColor3fv(colors[(i+1)%len(colors)])
        glVertex3f(bottom_vertices[i][0],bottom_vertices[i][1],0.0)
        glVertex3f(top_vertices[i][0],top_vertices[i][1],height)
        glVertex3f(top_vertices[(i+1)%n][0],top_vertices[(i+1)%n][1],height)
        glVertex3f(bottom_vertices[(i+1)%n][0],bottom_vertices[(i+1)%n][1],0.0)
    glEnd()

    glPopMatrix()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_prism()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# Main Routine
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("N-Prism")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()