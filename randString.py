#!/usr/bin/python
import sys
from random import randint

length = sys.argv[1]
BASEPAIRS = ('A', 'C', 'U', 'G')
string = ""

for x in range(0, int(length)):
  rand = randint(0,3)
  string = string + BASEPAIRS[rand]

print string
