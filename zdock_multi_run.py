import os
import subprocess 
import sys
import time
import psutil

pdb_dir = sys.argv[1]
start_time = time.time()
mem = psutil.virtual_memory()
cpu_usage = psutil.cpu_percent(interval=1)

for root, dirs, files in os.walk(pdb_dir):
	print r"There are " + str(len(files)) + r" files in the directory."
	for file1 in files:
		for file2 in files:
			if file1 != file2:
				while True:
					mem = psutil.virtual_memory()
					cpu_usage = psutil.cpu_percent(interval=1)
					print cpu_usage
					if mem.percent >= 50.0 or cpu_usage >= 50.0:
						time.sleep(120)
						print 'skip'
					elif file1 == files[-1] and file2 == files[-2]:
						out_file_name = str(file1.split(".")[0]) + str(file2.split(".")[0]) + r".pdb"
						cmd = r"/home/philip/zdock3.0.2_linux_x64/zdock -R " + str(root) + "//" + str(file1) + r" -L " + str(root) + "//" + str(file2) + r" -o " + str(root) + "//" + str(out_file_name) 
						print cmd
						p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
						break
					else:
						out_file_name = str(file1.split(".")[0]) + str(file2.split(".")[0]) + r".pdb"
						cmd = r"/home/philip/zdock3.0.2_linux_x64/zdock -R " + str(root) + "//" + str(file1) + r" -L " + str(root) + "//" + str(file2) + r" -o " + str(root) + "//" + str(out_file_name) 
						print cmd
						p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
						time.sleep(30)
						break

p.wait()
print p.returncode
print (time.time() - start_time)	