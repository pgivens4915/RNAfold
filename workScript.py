#!/usr/bin/python
import sys
import os

same = 0

fileName = sys.argv[1]
targetStart = sys.argv[2]
targetEnd = sys.argv[3]
mutRange = int(sys.argv[4])


fileCount = mutRange * 2

# Make the mutations into folding files
os.system("./mutate.py " + fileName + " " + targetStart + " " + targetEnd + 
          " " + str(mutRange));

os.system("./foldandconvert.py " + "base"  + " " + "base")

for x in range(0, int(fileCount)  ):
  os.system("./foldandconvert.py " + "out" + str(x) + " " + str(x))

baseFile = open("base.dot", "r")

# Getting the base string
stringOne = baseFile.readline()
stringOne = baseFile.readline()
stringOne = list(baseFile.readline())
targetOne = stringOne[int(targetStart) - 1 : int(targetEnd)]

stringOutputFile = open('string_output', 'w')

for x in range(0, int(fileCount)):
  compare = open(str(x) + ".dot", "r")
  stringTwo = compare.readline()
  stringTwo = compare.readline()
  stringTwo = list(compare.readline())
  targetTwo = stringTwo[int(targetStart) - 1: int(targetEnd)]

  if ("".join(targetTwo) == "".join(targetOne)):
    same = same + 1
  total = x
  print "".join(targetOne)
  print "".join(targetTwo)
  stringOutputFile.write("".join(targetOne))
  stringOutputFile.write("\t")
  stringOutputFile.write("".join(targetTwo))
  stringOutputFile.write("\n")
  
stringOutputFile.close()
os.system("./proximityCompare.py string_output")

ratio = float(same) / float(total + 1) 

print "We have a ratio of " + str(ratio)
print "From same " + str(same) + " over " + str(total + 1)

