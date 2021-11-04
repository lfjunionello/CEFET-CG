from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import png

N = 7 #Lados do prisma



def drawCylinder():
	quad = gluNewQuadric()
	gluQuadricOrientation(quad,GLU_OUTSIDE)
	gluQuadricNormals(quad,GLU_FLAT)
	gluCylinder(quad,1,1,2,N,20)
	glRotatef(0.5,0,0,2)


def display():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	drawCylinder()
	glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,float(w)/float(h),0.1,50.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,8,2,0,0,0,0,0,1)

def init():
	mat_ambient = (0.4, 0.0, 0.0, 1.0)
	mat_diffuse = (1.0, 0.0, 0.0, 1.0)
	mat_specular = (1.0, 1.0, 1.0, 1.0)
	mat_shininess = (60,)
	light_position = (5.0, 5.0, 5.0, 0.0)
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_FLAT)

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_MULTISAMPLE)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow("Prism")
	init()
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutTimerFunc(50,timer,1)
	glutMainLoop()

main()


