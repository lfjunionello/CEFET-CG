from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import png
import time


def LoadTextures(texname):
    global tex
    tex = [ glGenTextures(1) ]

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, tex[0])
    reader = png.Reader(filename=texname)
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	
    ################################################################################

def drawSphere(r):
	global tex
	#LoadTextures('textura.png')
	quad = gluNewQuadric()
	gluQuadricOrientation(quad,GLU_OUTSIDE)
	gluQuadricDrawStyle(quad,GLU_FILL)
	gluQuadricTexture(quad,GL_TRUE)
	gluQuadricNormals(quad,GLU_FLAT)
	gluSphere(quad,r,50,50)


def display():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	global tex
	
	glColor4f (1.0, 1.0, 0, 1)		#yellow
	glRotatef(5,0,0,1)
	LoadTextures('textura.png')
	drawSphere(3)

	glPushMatrix()
	glColor4f (0, 1.0, 0, 1)		#green
	glRotatef(11,0,0,0)
	glTranslatef(8,0,0)
	LoadTextures('mapa.png')
	drawSphere(2)
	

	
	glColor4f (1.0, 0, 0, 1)		#red
	glRotatef(22,0,1,1)
	glTranslatef(3,0,0.1)
	glRotatef(11,0,0,1)

	
	LoadTextures('moon1.png')
	drawSphere(1)
	glPopMatrix()
	

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
	gluLookAt(0,40,2,0,0,0,0,1,1)

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_FLAT)
	glEnable(GL_TEXTURE_2D)


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow("Sistema")
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutTimerFunc(50,timer,1)
	init()
	glutMainLoop()

main()


