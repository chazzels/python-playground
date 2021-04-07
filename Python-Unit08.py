import sys
import os
import subprocess

try:
	os.rmdir('tempPython')
except OSError as e:
	print("fail")

print(clean(os.getlogin()))
print()
print(clean( str(os.get_exec_path())))
print()

print(clean(str(sys.path)))
print()

print(clean(str(sys.byteorder)))
print()

print(clean(os.listdir()))
os.makedirs('tempPython')
print(clean(os.listdir()))
print()

# popen to run a git command instead because linux
with open("pythonOut.txt","w+") as f:
	proc = subprocess.Popen(["/usr/bin/git", "status"], stdout=f)
	print("# $ git status output saved to pythonOut.txt")
	print()

# no gui must using command line. 
# running a calculation in a linux shell instead.
print("Terminal experssion calculation:")
subprocess.Popen(["/usr/bin/dc", "--expression=100 0.5 * p"])