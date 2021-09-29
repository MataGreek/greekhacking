#################################################
#################################################
#####       GREEK HACKING FORUM             #####
#####            Copyright                  ##### 
#####     Greek Hacking ©2021 Forum         #####                       
##### Please use it for ethical purposes    #####
#################################################
#################################################


##################################################
##################################################
####                                          ####
####                FIND US HERE              ####
####         https://www.greekhacking.gr/     #### 
####                                          ####
##################################################
##################################################

import pyfiglet
import colorama
import requests
import time
import os, sys
import http.client as httplib
from colorama import *
colorama.init()

__version__ = '1.1.4'

os.system("cls||clear")


print(Fore.GREEN + "")
logo = pyfiglet.figlet_format("GREEK HACKING")
print(logo)
print("#" * 100)
print("                                 Author: MATA    |   https://www.greekhacking.gr/")
print("#" * 100)


def check_updates():
    try:
        response = requests.get('https://raw.githubusercontent.com/MataGreek/greekhacking/main/core/version.txt')
        data = response.text
        conn = requests.get('https://raw.githubusercontent.com/MataGreek/greekhacking/main/greekhacking.py')
        if float(data) > float(__version__):
                updateavailable = input(" [*] UPDATE AVAILABLE! DO YOU WANT TO UPDATE? (Y/n) :  ")
        if updateavailable == 'Y' or 'y' or 'yes' or 'Yes' or 'YES':
            conn.request('GET', 'https://raw.githubusercontent.com/MataGreek/greekhacking/main/greekhacking.py')
            newCode = conn.getresponse().read().strip().decode()
            with open("greekhacking.py", "w") as  greekhackingScript:
                    greekhackingScript.write(newCode)
        else:
            print(" [*] You are up to date!")

    except Exception:
            print("Unable to Check for Update, Error:")




print("")
print("     1 ==> Subdomain Finder")
print("")
print("     2 ==> Admin Login Finder")
print("")
print("     3 ==> Port Scanner")
print("")
print("     4 ==> Password Generator")
print("")
print("     5 ==> Proxy List")
print("")
print("     6 ==> MD5 Cracker")
print("")
print("     0 ==> Exit.")
print("")
print("")








Question = (int(input("     Choose: ")))
if Question == 1:
    from files import subfinder

if Question == 2:
    time.sleep(1)
    from files import admin
if Question == 3:
    time.sleep(1)
    from files import port
    time.sleep(1)
if Question == 4:
    time.sleep(1)
    from files import password
if Question == 5:
    time.sleep(1)
    from files import proxy
if Question ==6:
    from files import cracker
if Question == 0:
    print("")
    print("")
    print("     Exiting.........")
    time.sleep(1)
    quit()