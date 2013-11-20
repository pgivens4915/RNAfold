#!/usr/bin/python
import sys

# Getting all the input
inputFileOne = sys.argv[1]
inputFileTwo = sys.argv[2]
targetStart  = int(sys.argv[3])
targetStop   = int(sys.argv[4])

fileOne = open(inputFileOne, 'r')
fileTwo = open(inputFileTwo, 'r')

print fileOne
print fileTwo

# Done three times to get to the correct line
stringOne = fileOne.readline()
stringTwo = fileTwo.readline()
stringOne = fileOne.readline()
stringTwo = fileTwo.readline()
stringOne = list(fileOne.readline())
stringTwo = list(fileTwo.readline())

print "".join(stringOne)
print "".join(stringTwo)

targetOne = stringOne[targetStart : targetStop]
targetTwo = stringTwo[targetStart : targetStop]

print "".join(targetOne)
print "".join(targetTwo)
print "".join(targetOne) == "".join(targetTwo)
