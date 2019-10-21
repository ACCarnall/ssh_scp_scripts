import sys
import os

if len(sys.argv) == 1:
	os.system("ssh -Y adamc@stacpolly.roe.ac.uk")

files = sys.argv[1:-1]

filestr = ""

for file in files:
	filestr += file + " "

destination = sys.argv[-1]

os.system("scp -r " + filestr + " adamc@stacpolly.roe.ac.uk:/home/adamc/" + destination)