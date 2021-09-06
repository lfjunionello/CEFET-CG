from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

r = 1
n = 50
halfpi = math.pi/2

def f(u, v):
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z

def desenhaEsfera():
   for i in range(0,n): 
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(0,n): 
            glColor3f(0.5+(random.random()*0.5),0.5+(random.random()*0.5),0.13+(random.random()*0.5))
            x,y,z = f(i,j)
            glVertex3f(x,y,z)
            x,y,z = f(i+1,j)
            glVertex3f(x,y,z)
        glEnd()
a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    desenhaEsfera()    
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-5)
glutTimerFunc(50,timer,1)
glutMainLoop()


