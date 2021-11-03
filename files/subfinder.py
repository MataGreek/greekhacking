#WELCOME TO GH SUBDOMAIN FINDER

#THIS IS SO SIMPLE PROGRAM THAT YOU CAN FIND WEBSITES SUBDOMAINS

#USAGE: JUST ENTER THE DOMAIN. FOR EXAMPLE greekhacking.gr

#CAREFUL: WITHOUT "http(s)://"

#CREATED BY <============================ MATA | https:www.greekhacking.gr ============================>



#imports



from os import path
import requests
import pyfiglet
import colorama
import datetime
import socket
import time
import sys

from colorama import *

colorama.init()
x = datetime.datetime.now()


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

print(Fore.RED + "     Make sure that you have removed the: http(s)://" + Fore.RESET)

print("")

print("")

print("")

print(Fore.YELLOW + "")

domain = input("    Enter Domain here (e.x greekhacking.gr):   ")
try:
    ip = socket.gethostbyname(domain)
except Exception:
    print("")
    print(Fore.RED + "    [!] Please remove the http(s)://")
    print("")
    sys.exit()


print(Fore.RESET + "")

print("")

print("")

print("")

print("")
print("=" * 50)
print(Fore.RED + "  Scan started:"+ Fore.RESET + str(x))
print("=" * 50)
time.sleep(1)
print("")
print("                                     Subdomain" + "                Status" + "           IP")
print("")
print("")


file = open('subdomain.txt', 'r')

content = file.read()



subdomains = content.splitlines()



for subdomain in subdomains:
    spaces = ' ' * 10    
    print("\rScanning: " +str(subdomain) + str(spaces), end='')
    url = f"{subdomain}.{domain}"
    try:
        req = requests.get("http://"+url)
        print("")
        if req.status_code == 200:
            print(Fore.GREEN + "    \nPossible Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url) +  "    (Status: " + str(req.status_code) + ")   ", ip)
            print("")
    
        
    except requests.ConnectionError:
        pass

    except KeyboardInterrupt:
        print("")
        print("")
        print("="*50)
        print(Fore.RED + "  Scan Stopped:"+ Fore.RESET + str(x))
        print("="*50)

        print("Exiting.......")


        sys.exit()