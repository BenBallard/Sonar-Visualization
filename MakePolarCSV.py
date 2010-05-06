import sys
from numpy import *
import pylab
from  matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


fileInputname = sys.argv[1]
fileOutputName = sys.argv[2]
print "File name input = " + fileInputname
print "File name output  = " + fileOutputName

print "Converting...."


f = loadtxt(fileInputname, delimiter=',')	

x,y = f.shape
xmid = x/2
ymid = y/2
print f.shape

r = zeros((x*y,3))

print r.shape

PI = math.pi
for X in xrange(x):
	for Y in xrange(y):
		rX = mod(X,x)
		rY = mod(Y,y)
		loc = X*y + Y
		r[loc,0] = f[rX,rY] * sin((X*PI)/180)
		distance = f[rX,rY] * cos((X*PI)/180)
		r[loc,1] = distance * sin((Y*PI)/180)
		r[loc,2] = distance * cos((Y*PI)/180)

savetxt(fileOutputName,r.transpose(),fmt='%3.3f',delimiter=',')



