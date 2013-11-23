#!/usr/bin/python
import sys
from random import randint

# Declarations
BASEPAIRS = ('A', 'C', 'U', 'G')

# Verifying command line arguments
if (len(sys.argv) != 5):
    print "Usage ./mutate.py <inputFile> <Target start> <Target end> <length of mutation>"
    sys.exit()

# Getting the command line args
inputFile     = sys.argv[1]
targetStart   = int(sys.argv[2])
targetEnd     = int(sys.argv[3]) - 2
mutationRange = int(sys.argv[4])

# File IO
out = open("out0", 'w')
f = open(inputFile, 'r')
line = list(f.readline())

# Printing the base file
base = open("base", "w")
base.write(";\n")
base.write("A TITLE\n")
base.write("".join(line) + "1")


outNumber = 0 

for x in range(1, mutationRange + 1):
    forwardMut = list(line)
    backMut = list(line)
    rand = randint(0,3)
    while (BASEPAIRS[rand] == forwardMut[targetEnd + x]):
      rand = randint(0,3)
    forwardMut[targetEnd + x] = BASEPAIRS[rand]
    rand = randint(0,3)
    while (BASEPAIRS[rand] == backMut[targetEnd + x]):
      rand = randint(0,3)
    backMut[targetStart - x] = BASEPAIRS[rand]
    out.write(";\n")
    out.write("A TITLE\n")
    out.write("".join(forwardMut) + "1")
    out.close()
    outNumber = outNumber + 1
    out = open("out" + str(outNumber), "w")
    out.write(";\n")
    out.write("A TITLE\n")
    out.write("".join(backMut) + "1")
    out.close()
    outNumber = outNumber + 1
    out = open("out" + str(outNumber), "w")
