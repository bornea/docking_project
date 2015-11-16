import sys
import os

pdf_files = sys.argv[1]
pdf_list = pdf_files.split()

for file1 in pdf_list:
	for file2 in pdf_list:
		cmd = r"/home/zdock3.0.2_linux_x64/zdock" + str(file1) + str(file2)
		os.system(cmd) 
	file2.seek(0)