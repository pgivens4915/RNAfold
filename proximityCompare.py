import os
import sys

stringFileName = sys.argv[1]

finalOutputFile = open('final_output', 'w')

proximity = 1
even = 0
sameCount = 0
for row in open(stringFileName, 'rb'):
	old, new = row.split('\t')
	old = old.strip()
	new = new.strip()
	if old == new:
		print 'same'
		sameCount = sameCount+1
	if even == 0:
		even = even+1
	else:
		finalOutputFile.write(str(proximity))
		finalOutputFile.write('\t')
		finalOutputFile.write(str(sameCount))
		finalOutputFile.write('\n')
		sameCount = 0
		even = even-1
		proximity = proximity+1