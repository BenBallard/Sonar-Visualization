import sys
from numpy import *
import pylab
from  matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from enthought.mayavi import mlab

fileInputname = sys.argv[1]

print "File name input = " + fileInputname
print "Graphing...."


f = loadtxt(fileInputname, delimiter=',')	

x,y = f.shape
print f.shape
A,B,C = vsplit(f,3)
print A.shape
print B.shape
print C.shape
print A
print B
print C

A = A.ravel()
B = B.ravel()
C = C.ravel()


print A.shape
print B.shape
print C.shape
print A
print B
print C


#fig = pylab.figure()
#ax = Axes3D(fig)

#ax.plot_surface(B,C,A,rstride=5,cstride=5,cmap=cm.jet)

#ax.plot_surface(B,C,A,rstride=5,cstride=5,cmap=cm.jet)
#ax.contourf(B.transpose(),C.transpose(),A.transpose(),cmap=cm.jet)
#ax.plot_surface(xArray,yArray,f,cmap=cm.jet)

#pylab.show()

l = mlab.points3d(B,C,A,line_width=1,resolution=3)
mlab.show()

