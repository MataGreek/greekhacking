import time
import os
import sys
from sys import platform
print(" Installing requirements....")
time.sleep(2)

if sys.platform == "linux" or platform == "linux2":
    cmd1 = 'sudo apt install python3-pip'
    cmd = 'pip install -r requirements.txt'
    os.system(cmd1)
    os.system(cmd)

if sys.platform == "win32":
    cmd2 = 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
    cmd3 = 'python get-pip.py'
    cmd4 = 'pip install requirements.txt'
    os.system(cmd2)
    os.system(cmd3)
    os.system(cmd4)

question = input("Do you want to open the program right now? (Y/n)  :    ")
if question == 'Yes' or 'yes' or 'YES' or 'y' or 'Y':
    import greekhacking
    pass
else:
    quit()