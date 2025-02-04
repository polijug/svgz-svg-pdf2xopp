import glob
import os
from pathlib import Path
import subprocess
from pdf2xopp import pdf2xopp

root_dir = input("Enter directory, where will be all .svg files replaced with .xopp: ")

os.chdir(root_dir)

for filename in glob.iglob(root_dir + '**/*.svg', recursive=True):
	file = filename.rsplit('.', 1)[0]
	print(file)
	subprocess.run(["inkscape", "--export-area-drawing", "--export-filename=" + file + ".pdf", file + ".svg"])
	os.remove(file + ".svg")
	pdf2xopp(file + ".pdf", file + ".xopp")
	os.remove(file + ".pdf")
