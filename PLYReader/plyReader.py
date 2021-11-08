from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from plyfile import PlyData, PlyElement
import sys
def drawBunny():
	plydata = PlyData.read('bunny.ply')
	glBegin(GL_POINTS)

	for i in range(8171):

		glVertex3f(plydata.elements[0].data['x'][i].item(),
				   plydata.elements[0].data['y'][i].item(),
				   plydata.elements[0].data['z'][i].item()	)
	glEnd()


def display():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glRotate(5,0,1,0)
	drawBunny()
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
	gluLookAt(0,0.2,0.3,-0.02,0.1,0,0,1,0)

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_FLAT)
	glEnable(GL_TEXTURE_2D)


def main():
	#plydata = PlyData.read('bunny.ply')

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow("PLY Bunny Model")
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutTimerFunc(50,timer,1)
	init()
	glutMainLoop()

main()


