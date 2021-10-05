#WELCOME TO GH SUBDOMAIN FINDER
#THIS IS SO SIMPLE PROGRAM THAT YOU CAN FIND WEBSITES SUBDOMAINS
#USAGE: JUST ENTER THE DOMAIN. FOR EXAMPLE greekhacking.gr
#CAREFUL: WITHOUT "www."
#CREATED BY <============================ MATA | https:www.greekhacking.gr ============================>

#imports

import requests
import pyfiglet
import colorama
import time
import sys
from colorama import *
colorama.init()

#logo 


print(Fore.LIGHTBLUE_EX + "")
logo = pyfiglet.figlet_format("GH Subdomain Finder")
print(logo)
print("-" * 100)
print("                                           WELCOME TO GH SUBDOMAIN FINDER")
print("")
print("                 <============== CREATED BY MATA | https://www.greekhacking.gr ==============>")
print("-" * 100)
print(Fore.RESET + "")

print("")
print("")
print("")
print(Fore.YELLOW + "")
domain = input("    Enter Domain here (e.x greekhacking.gr):   ")
print(Fore.RESET + "")
print("")
print("")
print("")
print("")
print(Fore.RED + "                      <================================= Please wait... =================================>" + Fore.RESET)
time.sleep(4)
print("")
print("")
print("")
file = open('subdomain.txt', 'r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        
        print(Fore.GREEN + "    Possible Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url1))
        requests.get(url2)
        print(Fore.GREEN + "    Possible Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url2) + Fore.RESET)

    except requests.ConnectionError:
        pass
    except KeyboardInterrupt:
        print("Exiting.......")
        time.sleep(1)
        sys.exit()
