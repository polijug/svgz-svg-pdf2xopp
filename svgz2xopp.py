import glob
import os
import sys
import subprocess
from pdf2xopp import pdf2xopp

root_dir = ""
if(len(sys.argv) == 2):
	root_dir = sys.argv[1]
else:
	root_dir = input("Enter directory, where will be all .svgz files replaced with .xopp: ")

os.chdir(root_dir)

for filename in glob.iglob(root_dir + '**/*.svgz', recursive=True):
	file = filename.rsplit('.', 1)[0]
	print(file)
	os.rename(filename, file + ".svg.gz")
	comp = subprocess.run(["gunzip", file + ".svg.gz"])
	if(comp.returncode == 0):
		subprocess.run(["inkscape", "--export-area-drawing", "--export-filename=" + file + ".pdf", file + ".svg"])
		os.remove(file + ".svg")
		pdf2xopp(file + ".pdf", file + ".xopp")
		os.remove(file + ".pdf")
