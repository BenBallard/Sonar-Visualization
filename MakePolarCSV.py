import sys
from numpy import *
import pylab
from  matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


fileInputname = sys.argv[1]
fileOutputName = sys.argv[2]
print "File name input = " + fileInputname
print "File name output  = " + fileOutputName

fileOutputNameX=fileOutputName+"X.csv"
fileOutputNameZ=fileOutputName+"Z.csv"
fileOutputNameY=fileOutputName+"Y.csv"
fileOutputNameR=fileOutputName+"R.csv"




print "Converting...."


f = loadtxt(fileInputname, delimiter=',')	

x,y = f.shape
xmid = x/2
ymid = y/2
print f.shape

ZMat = zeros((x,y))
XMat = zeros((x,y))
YMat = zeros((x,y))

RMat = zeros((512,512))

XStart = 60
YStart = 60

PI = math.pi
for X in xrange(x):
	for Y in xrange(y):
		rX = mod(X,x)
		rY = mod(Y,y)
		Yangle = Y+YStart
		Xangle = X+XStart
		ZMat[X,Y] = f[rX,rY] * sin(((Xangle)*PI)/180)
		Zr = f[rX,rY] * sin(((Xangle)*PI)/180)
		distance = f[rX,rY] * cos(((Xangle)*PI)/180)
		XMat[X,Y] = distance * sin(((Yangle)*PI)/180)
		YMat[X,Y] = distance * cos(((Yangle)*PI)/180)
		Xr = distance * sin(((Yangle)*PI)/180)
		Yr = distance * cos(((Yangle)*PI)/180)
		RMat[int(Xr),int(Yr)] = Zr

savetxt(fileOutputNameZ,ZMat,fmt='%5.5f',delimiter=',')
savetxt(fileOutputNameX,XMat,fmt='%5.5f',delimiter=',')
savetxt(fileOutputNameY,YMat,fmt='%5.5f',delimiter=',')
savetxt(fileOutputNameR,RMat,fmt='%5.5f',delimiter=',')


