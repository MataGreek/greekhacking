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


versionpath = ("core", "version.txt") 
os.system("cls||clear")


print(Fore.GREEN + "")
logo = pyfiglet.figlet_format("GREEK HACKING")
print(logo)
print("#" * 100)
print("                                 Author: MATA    |   https://www.greekhacking.gr/")
print("#" * 100)


def check_updates():
    try:
        requests.get('https://raw.githubusercontent.com/MataGreek/greekhacking/main/core/version.txt')
        os.write("  [~] Checking for updates...\n")
        conn = httplib.HTTPSConnection("raw.githubusercontent.com")
        conn.request("GET", "/MataGreek/greekhacking/main/core/version.txt")
        repoVersion = conn.getresponse().read().strip().decode()
        with open(versionpath) as vf:
            currentVersion = vf.read().strip()
        if repoVersion == currentVersion:os.write("  [*] The script is up to date!\n")
        else:
                print("  [+] An update has been found ::: Updating... ")
                conn.request("GET", "/MataGreek/greekhacking/main/greekhacking.py")
                newCode = conn.getresponse().read().strip().decode()
                with open("greekhacking.py", "w") as  greekscript:
                   greekscript.write(newCode)
                with open(versionpath, "w") as ver:
                     ver.write(repoVersion)
                os.write("  [+] Successfully updated :)\n")

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