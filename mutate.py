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
targetEnd     = int(sys.argv[3])
mutationRange = int(sys.argv[4])

# File IO
out = open('output', 'w')
f = open(inputFile, 'r')
line = list(f.readline())

for x in range(1, mutationRange + 1):
    forwardMut = list(line)
    backMut = list(line)
    rand = randint(0,3)
    forwardMut[targetEnd + x] = BASEPAIRS[rand]
    rand = randint(0,3)
    backMut[targetStart - x] = BASEPAIRS[rand]
    out.write("".join(forwardMut))
    out.write("".join(backMut))
