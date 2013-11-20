#!/usr/bin/python
import os
import sys

seqFileName = sys.argv[1]
print seqFileName
# The -m 5 specifies that only up to the first 5 sub-optimal structures will be calculated
# see: http://rna.urmc.rochester.edu/Text/Fold.html
os.system("date")
os.system("./Fold " + seqFileName + " fold_output.ct -m 5")
for x in range(1,6):
# The ct2dot function will only convert 1 ct sequence at a time,
# so we have to loop through them.
# see: http://rna.urmc.rochester.edu/Text/ct2dot.html
  os.system("./ct2dot fold_output.ct " + str(x) + " fold_output" + str(x) + ".dot")
