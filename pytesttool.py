import pytest
import subprocess
import os
import platform
'''
print(platform.system())
pwd = os.getcwd()
inputsource = input("Please type the source of a test file, folder contaiining test files or \n a bash script to execute test files:")
if os.path.isdir(inputsource):
    sourceisdir = True
    print("looking for tests in folder.....")
elif os.path.exists(inputsource):
    sourceisfile = True
    print("looking for tests in file or bash.....")
else:
    print("need a valid source!")
'''

#subprocess.call(pwd/bashtest.sh')
#r = subprocess.run(['ls', '-lha'])
r = subprocess.check_output(['which', 'bash'])
print("r ist : ...........")
print(r)