#WELCOME TO GH SUBDOMAIN FINDER

#THIS IS SO SIMPLE PROGRAM THAT YOU CAN FIND WEBSITES SUBDOMAINS

#USAGE: JUST ENTER THE DOMAIN. FOR EXAMPLE greekhacking.gr

#CAREFUL: WITHOUT "www."

#CREATED BY <============================ MATA | https:www.greekhacking.gr ============================>



#imports



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



print("")

print("")

print("")

print(Fore.YELLOW + "")

domain = input("    Enter Domain here (e.x greekhacking.gr):   ")
ip = socket.gethostbyname(domain)

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


    url1 = f"http://{subdomain}.{domain}"
    
    

    url2 = f"https://{subdomain}.{domain}"

  





    try:

        req = requests.get(url1)


        if req.status_code != 403 or 404:

        
            
            print(Fore.GREEN + "    Possible Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url1) +  "    (Status: " + str(req.status_code) + ")   ", ip)
        else:
            pass

        req1 = requests.get(url2)

        if req1.status_code != 403 or 404:

            print(Fore.GREEN + "    Possible Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url2) + "    (Status: " + str(req1.status_code) + ")   ", ip)
        else:
            pass

    except requests.ConnectionError:

        pass

    except KeyboardInterrupt:

        print("Exiting.......")


        sys.exit()