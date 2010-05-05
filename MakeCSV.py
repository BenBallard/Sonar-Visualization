import sys
import string

fileInputname = sys.argv[1]
fileOutputname = sys.argv[2]

print "File name input = " + fileInputname
print "File name output = " + fileOutputname
print "Converting...."

Input = open(fileInputname,"r")
Output = open(fileOutputname,"w")

startFound = False

def writeOut(out):
	if startFound:
		Output.write(out);

OutString=""
for line in Input:
	if startFound:
		if "xPos" in line:
			OutString =  OutString + ","
		elif "yPos" in line:
			writeOut((OutString+'\n')[1:])
			OutString = ""
		else:
			OutString = OutString + string.strip(line)
	if "Start" in line:
		startFound = True 
		OutString=""
	
		



