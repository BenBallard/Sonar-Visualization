import sys
from numpy import *
import pylab
from matplotlib import cm
import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from enthought.mayavi import mlab

fileInputname = sys.argv[1]

print "File name input = " + fileInputname
print "Graphing...."

fileInputnameX = fileInputname + "X.csv"
fileInputnameY = fileInputname + "Y.csv"
fileInputnameZ = fileInputname + "Z.csv"
#fileInputnameR = fileInputname + "R.csv"


X  = loadtxt(fileInputnameX, delimiter=',')	
Y  = loadtxt(fileInputnameY, delimiter=',')	
Z  = loadtxt(fileInputnameZ, delimiter=',')	
#R  = loadtxt(fileInputnameR, delimiter=',')	



#fig = plt.figure()

#ax = Axes3D(fig)

#ax.plot_surface(B,C,A,rstride=5,cstride=5,cmap=cm.jet)

#ax.plot_surface(Y,X,Z,rstride=5,cstride=5,cmap=cm.jet)
#ax.contourf(B.transpose(),C.transpose(),A.transpose(),cmap=cm.jet)
#ax.plot(X.ravel(),Y.ravel(),Z.ravel())

#pylab.show()

#l = mlab.points3d(X,Y,Z,line_width=1,resolution=3)
#x,y = mgrid[-500.:500.:1.,-500.:500.:1.]
l = mlab.surf(Z)

mlab.show()
