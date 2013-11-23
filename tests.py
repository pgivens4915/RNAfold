import unittest
import os

class TestFunctions(unittest.TestCase):

	def setUp(self):
		#create a random string to be used in the mutate function
		os.system("./randString.py 10 > testFunctions.seq");
		assert os.path.exists("./testFunctions.seq") == 1
	
	def test_mutate(self):
		#clean out old out<#> files
		for x in range(0, 5):
			os.system("rm out"+str(x));
		#run the mutate function
		os.system("./mutate.py mutateTest.seq 2 3 2");
		#check that all the new out<#> files exist now
		for x in range(0, 5):
			assert os.path.exists("./out"+str(x)) == 1
		
	def test_foldandconvert(self):
		#clean out old files
		os.system("rm fold_output.ct");
		for x in range(0, 5):
			os.system("rm out"+str(x));
		#rerun mutate just to ensure all the out<#> files are there
		os.system("./mutate.py mutateTest.seq 2 3 2");
		#for all the out<#> files run foldandconvert on them
		for x in range(0, 5):
			os.system("./foldandconvert.py out"+str(x)+" "+str(x));
		#check that all the new <#>.dot files exist now
		for x in range(0, 5):
			assert os.path.exists(str(x)+".dot");
	
	
if __name__=='__main__':
	unittest.main()