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

def check_updates():
    try:
        conn = httplib.HTTPSConnection("raw.githubusercontent.com")

        conn.request("GET", "/MataGreek/fuzzyfa/main/core/version.txt")
        repver = conn.getresponse().read().strip().decode()

        print("")
        print("=" * 70)
        print("[!] Latest Version:",repver)
        print("=" * 70)
        print("")
        

        with open('./core/version.txt') as f:
            current = f.read().strip()
        if repver == current:
            print("[+] Script is up to date.")
            print("")
            

        else:
            ask = input("[+] Update is available. Do you want to update? [Y/n]  ")

            if ask in yes_choice:
                print("")
                print("[*] updating...")
                print("")
                time.sleep(2)



            try:
                conn.request("GET", "/MataGreek/fuzzyfa/main/fuzzyfa.py")

                new = conn.getresponse().read().strip().decode()

                with open('fuzzyfa.py', 'w+') as fa:
                    currentfa = fa.read().strip()
                    
                    if new != currentfa:
                        fa.write(new)
                
            except KeyboardInterrupt:
                print("exit.")
            try:
                conn.request("GET", "/MataGreek/fuzzyfa/main/setup.py")

                new = conn.getresponse().read().strip().decode()
                
                with open('setup.py', 'w+') as se:
                    currentfa = se.read().strip()
                    
                    if new != currentfa:
                        se.write(new)

                print("[+] Updated!")
                time.sleep(1)
                print("")
                print(Fore.LIGHTRED_EX + "[!] PLEASE REOPEN THE PROGRAM FOR THE UPDATES TAKE AFFECT!" + Fore.RESET)
                print("")
                pass
                if repver != current:

                    with open('./core/version.txt', 'w+') as pf:

                        pf.write(repver)
                else:

                    print("[!] Your version is:", current + "You are not up to date! Please update the program.")

            except KeyboardInterrupt:
                print("exit.")
                                

            except KeyboardInterrupt:
                print("Exit.")
    except Exception as e:
        print("unable to check for update. Error: ", e)


check_updates()





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
            print("[!] Exit.")
            sys.exit()

