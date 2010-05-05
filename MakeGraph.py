import sys
from numpy import *
import pylab
from  matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


fileInputname = sys.argv[1]

print "File name input = " + fileInputname
print "Graphing...."


f = loadtxt(fileInputname, delimiter=',')	

x,y = f.shape

fig = pylab.figure()
ax = Axes3D(fig)


xArray =arange(x).reshape(x,1)
for r in range(y-1):
	xArray = hstack((xArray,arange(x).reshape(x,1)))	

yArray = arange(y)
for r in range(x-1):
	yArray = vstack((yArray,arange(y)))	
ax.plot_surface(xArray,yArray,f,rstride=5,cstride=5,cmap=cm.jet)

#ax.plot_surface(xArray,yArray,f,cmap=cm.jet)

pylab.show()



