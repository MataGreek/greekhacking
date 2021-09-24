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
import time
from colorama import *
colorama.init()

print(Fore.GREEN + "")
logo = pyfiglet.figlet_format("GREEK HACKING")
print(logo)
print("#" * 100)
print("                                 Author: MATA    |   https://www.greekhacking.gr/")
print("#" * 100)

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