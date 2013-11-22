#!/usr/bin/python
import sys
import os

fileName = sys.argv[1]
targetStart = sys.argv[2]
targetEnd = sys.argv[3]
mutRange = int(sys.argv[4])

fileCount = mutRange * 2

# Make the mutations into folding files
os.system("./mutate.py " + fileName + " " + targetStart + " " + targetEnd + 
          " " + str(mutRange));
print "Mutation complete"

for x in range(0, int(fileCount) ):
  print "./foldandconvert.py " + "out" + str(x) + " " + str(x) + "\n"
  os.system("./foldandconvert.py " + "out" + str(x) + " " + str(x))
