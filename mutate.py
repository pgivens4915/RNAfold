#!/usr/bin/python
import sys
from random import randint

# Declarations
BASEPAIRS = ('A', 'C', 'U', 'G')

# Verifying command line arguments
if (len(sys.argv) != 7):
    print "Usage ./mutate.py <inputFile> <Target start> <Target end> <mutationRange> <mutCount> <iterations>"
    sys.exit()

# Getting the command line args
inputFile     = sys.argv[1]
targetStart   = int(sys.argv[2])
targetEnd     = int(sys.argv[3])
mutationRange = int(sys.argv[4])
mutCount      = int(sys.argv[5])
iterations    = int(sys.argv[6])


# File IO
out = open("out0", 'w')
f = open(inputFile, 'r')
line = list(f.readline())

# Printing the base file
base = open("base", "w")
base.write(";\n")
base.write("A TITLE\n")
base.write("".join(line) + "1")

mutatedAreas = []
outNumber = 0 

for x in range(1, iterations + 1):
    mut = list(line)
    rand = randint(0,3)
    for i in range(0,mutCount):
        targetArea = randint(0, 2 * mutationRange)
        while(targetArea in mutatedAreas):
            targetArea = randint(0, 2 * mutationRange)
        # Add the target area to the mutatedArea's list
        mutatedAreas.append(targetArea)

        # Messing with the target area so it works
        if (targetArea > mutationRange):
            targetArea = targetArea - mutationRange
            targetArea = targetArea + targetEnd
        else :
            targetArea = targetStart - targetArea -1
        while (BASEPAIRS[rand] == mut[targetArea]):
          rand = randint(0,3)
        mut[targetArea - 1] = BASEPAIRS[rand]
    mutatedAreas = []
    
    print "".join(mut)

    out.write(";\n")
    out.write("A TITLE\n")
    out.write("".join(mut) + "1")
    out.close()
    outNumber = outNumber + 1
    out = open("out" + str(outNumber), "w")
