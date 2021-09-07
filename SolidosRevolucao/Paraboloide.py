from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import math 
import random

res = 50
r = 2

a = 0 
def f1(i,j):
    theta = (math.pi*i/(res-1))-(math.pi/2)
    phi = 2*math.pi*j/(res-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x,y**2,z

def paraboloid_mesh():
    glPushMatrix()
    glTranslate(0,-1,0)
    glRotatef(a,0,0.3,0.1)

    glBegin(GL_TRIANGLE_STRIP)
    
    for i in range(0,round(res/2)): 
        for j in range(0,res): 
            glColor3fv(((1.0*(i+1)/(res-1)) * 0.9,(random.random()/5),1 - (1.0*(i+1)/(res-1)) * 0.87 ))
            x,y,z = f1(i,j)
            glVertex3f(x,y,z)
            x,y,z = f1(i+1,j)
            glVertex3f(x,y,z)

    glEnd()
    glPopMatrix()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global a 
    a+=1
    paraboloid_mesh()
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Paraboloide")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()
