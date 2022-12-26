import os
import sys
import subprocess

dirPath = r"C:/Users/Sasikumar S/own_programs/"
os.chdir(dirPath)
path = os.path.join(dirPath, "variables_scope.py")
#command = r'python "' + path + '"'
command = r'python "'+path+'"'
print(command)

(status, output) = subprocess.getstatusoutput(command)