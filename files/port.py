import sys, os
import socket
import pyfiglet
import threading
import time
import colorama
from datetime import datetime
from colorama import *




colorama.init()

print_lock = threading.Lock()

#LOGO

logo = pyfiglet.figlet_format("GH   port   scanner")
print(Fore.LIGHTBLUE_EX + logo + Fore.RESET)
print("-" * 120)
print("                                     Created By Mata | https://www.greekhacking.gr/          ")
print("                                         Donations ==> paypal.me/vbourant                    ")       
print("-" * 120)

#INPUT
print("")
print("")
print("")

try:
    print(Fore.LIGHTYELLOW_EX + '')
    target = input("  Enter the Host Here:    ")
    print("" + Fore.RESET)
    target_ip = socket.gethostbyname(target)
    time.sleep(3)
except Exception:
    print("")
    print(Fore.RED +  "  Error: Could not find the HOST. (Check your internet connection or your input is wrong)")
    print("")
    print("")
    print("")
    sys.exit()


    
print("-" * 60)
print("Please wait, GH scanning the host... ==>  ", (Fore.LIGHTBLUE_EX + target_ip + Fore.RESET))
time.sleep(3)
print("")
print("Will take sometime, go get a coffee :)")
time.sleep(2)
print("")
print(Fore.LIGHTRED_EX + 'Scanning Started at: ')
print(datetime.now())
print('' + Fore.RESET)
print("-" * 60)
print("")

#PORTS

try:
        for port in range(1,1000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)
            r = s.connect_ex((target_ip,port))
            with print_lock:
                if r == 0:
                    print( Fore.RED + " [+]  " + Fore.WHITE + str(port) + Fore.WHITE + " ==> " + Fore.GREEN + " Open! " + Fore.RESET)
                    s.close()

except KeyboardInterrupt:
    print("")
    print("")
    print("")
    print("Exiting........")
    print("")
    print("")
    print("")

    sys.exit()

    
