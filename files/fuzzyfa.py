#imports

import time
import pyfiglet
import sys, os
import colorama
from colorama import *
import requests
import http.client as httplib
colorama.init()

yes_choice = ['','Yes', 'y', 'Y', 'yes', 'YES']
no_choice = ['No', 'n', 'no', 'NO', 'N']


#logo

logo = pyfiglet.figlet_format("Fuzzy Fa")
print(logo)




############

print("=" * 50)
print("[*] Please enter the url like this: http://example.com/")    
print("=" * 50)
print("")
target = input("[-] Enter the target: ")



print("")
wlist = open('fuzz.txt', 'r')
content = wlist.read()

wordlist = content.splitlines()


for path in wordlist:
    url = f"{target}{path}"
    try:
       
        req = requests.get(url)
        if req.status_code == 200:
            print("\n[+] Directory Found: ", str(url) + "   (Status: " + str(req.status_code) + ")    ")
        if req.status_code != 200:
            spaces = ' ' * 10
            print("\rScanning: " +str(path) + str(spaces), end='')
                  
    except KeyboardInterrupt:
            print("\n[!] Exit.")
            sys.exit()
