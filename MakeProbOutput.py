import sys
from numpy import *
import pylab
from matplotlib import cm
import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from enthought.mayavi import mlab
import random

fileInputname = sys.argv[1]

print "File name input = " + fileInputname
print "Graphing...."

fileInputnameZ = fileInputname + "Z.csv"


Z  = loadtxt(fileInputnameZ, delimiter=',')	


#Start with a prob of .5 all likely
X,Y = Z.shape
priorMult = 1.0/(X*Y)
prior = ones(Z.shape)
viewed = ones(Z.shape)*priorMult
print prior
print X*Y
def MakeProbCircle(x,y,good,bad):
	Selected = zeros(Z.shape)
	count = 0
	S = 3
	for Sx in xrange(X):
		for Sy in xrange(Y):
			if Sx - S <x and Sx + S >x and Sy - S<y and Sy + S >y :
				count = count + 1
				Selected[Sx,Sy]=1
	ProbMult = good/(count)
	ProbBad = bad/(X*Y*1.0-count*1.0)
	#Selected = Selected * ProbMult
	Selected = Selected * good
#	print ProbMult
#	print ProbBad
	for Sx in xrange(X):
		for Sy in xrange(Y):
			if Selected[Sx,Sy] == 0:
				#Selected[Sx,Sy]=ProbBad 
				Selected[Sx,Sy]=bad
	return Selected

Xguess =  random.randrange(X)
Yguess = random.randrange(Y)
print Xguess
print Yguess
for i in xrange(828):
	good = 0
	bad = 0
	if Z[Xguess,Yguess]<20.0:
		good = 1.0-Z[Xguess,Yguess]/100.0
		bad  = Z[Xguess,Yguess]/100.0
		good = .4
		bad = .35
	else:
		good = 0
		bad = 1
	likelyhood = MakeProbCircle(Xguess,Yguess,good,bad)
	viewed = viewed * MakeProbCircle(Xguess,Yguess,good,bad)
	prior = likelyhood*prior
	count = 1
	priorList = viewed.copy()
	priorList = priorList.ravel()
	listA = priorList.tolist()
	sort(listA)
	mid = int(len(listA)/2.0)
	midValue = listA[-1]
	listX = list()
	listY = list()
	count = 1
	for Sx in xrange(X):
		for Sy in xrange(Y):
			if viewed[Sx,Sy] == midValue:
				listX.append(Sx)
				listY.append(Sy)
				count = count + 1
	if count == 1:
		Xguess = listX[0]
		Yguess = listY[0]
	else:
		mid = random.randrange(count-1)
		Xguess = listX[mid]
		Yguess = listY[mid]
#fig = plt.figure()

#ax = Axes3D(fig)

#ax.plot_surface(B,C,A,rstride=5,cstride=5,cmap=cm.jet)

#ax.plot_surface(Y,X,Z,rstride=5,cstride=5,cmap=cm.jet)
#ax.contourf(B.transpose(),C.transpose(),A.transpose(),cmap=cm.jet)
#ax.plot(X.ravel(),Y.ravel(),Z.ravel())

#pylab.show()

#l = mlab.points3d(X,Y,Z,line_width=1,resolution=3)
#x,y = mgrid[-500.:500.:1.,-500.:500.:1.]

l = mlab.surf(prior)
mlab.show()
