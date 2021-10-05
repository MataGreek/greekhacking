#________________________________________________________ IMPORTS ________________________________________________________
import requests as r
from requests import status_codes
import pyfiglet
import time
import datetime
import sys
import colorama
from colorama import *
colorama.init()

if sys.version_info < (3,0):
    print("Sorry, requires Python 3.x, not Python 2.x")
    sys.exit(1)

#________________________________________________________ LOGO ________________________________________________________

print(Fore.LIGHTBLUE_EX + "")
logo = pyfiglet.figlet_format("GH ADMIN FINDER")
print(logo + Fore.RESET)
print("-" * 70)
print(Fore.RED + "          Created by Mata | https://www.greekhacking.gr/" + Fore.RESET)
print("-" * 70)
print("")
print("SS")
print("")




#________________________________________________________ INPUTS ________________________________________________________

print(Fore.LIGHTYELLOW_EX + "")
url = input("  Please Enter the URL Here:  ")
print("" + Fore.RESET)
wlist = open('admin.txt', 'r')
content = wlist.read()

wlist = content.splitlines()

#________________________________________________________ Checking ________________________________________________________

print("-" * 70)
print(Fore.LIGHTYELLOW_EX +"Checking admin panel for url: " + Fore.LIGHTBLUE_EX + str(url) + Fore.RESET)
print("-" * 70)
time.sleep(3)
x = datetime.datetime.now()
print(" Scan started at: " + Fore.RED + str(x) + Fore.RESET)
print("-" * 70)
print("")
time.sleep(2)

#________________________________________________________ 200 ________________________________________________________

for path in wlist:
    try:
        usrl_use = url + path
        got = r.get(usrl_use)
        if got.status_code == 200:
                print(Fore.GREEN + "[+]  " + usrl_use + " ==>  " + str(got.status_code) + "     OK! "+ Fore.RESET)
    

#________________________________________________________ NOT 200 _______________________________________________________
        if got.status_code != 200:
                print(Fore.RED + "[-]   " + usrl_use + "    ==>   " + str(got.status_code) + "    NOT FOUND!" + Fore.RESET)
                time.sleep(1)
    except KeyboardInterrupt:
        time.sleep(1)
        print("Exiting......")
        time.sleep(1)
        print(Fore.WHITE + "-" * 70)
        print(" Scan stopped at:    " + Fore.RED +str(x))
        print(Fore.WHITE + "-" * 70)
        sys.exit()
print("")
print("")
print(Fore.WHITE + "-" * 70)
print(" Scan stopped at:    " + Fore.RED +str(x))
print(Fore.WHITE + "-" * 70)

                
            
            
