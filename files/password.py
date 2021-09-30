import random
import time
import pyfiglet
from typing import Text
import colorama
from colorama import *
colorama.init()

print("" + Fore.LIGHTBLUE_EX)
logo = pyfiglet.figlet_format("GH Password Generator")
print(logo + Fore.RESET)
print(Fore.RED + "#" * 100 + Fore.RESET)
print(Fore.LIGHTBLUE_EX + "                         Created By Mata | https://www.greekhacking.gr/")
print(Fore.RED + "#" * 100 + Fore.RESET)

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "12345678910"
symbols = "!@#$%^&*()_+-=[];'\:|<>?,./"

upper, lower, nums, syms = True, True, True, True

all = ""
print("")
print("")
print("")
Question = input("  Do you want to Generate a safe password?(Y/n) :   ")
if Question == "Y" or "y" or "Yes" or "yes" or "YES" or "ναι" or "Ναι" or "ΝΑΙ":
    time.sleep(1)
    pass
else:
    time.sleep(1)
    print(" Maybe next time.")
    quit()


print("")
print("")
print("\n" + "#" * 50 + "\n         Please wait. password is generating..." + "\n" + "#" * 50)
time.sleep(2)
print("")
print("")
print("\n" + "#" * 50 + Fore.RED + "\n        DO NOT SHARE YOUR PASSWORD TO ANYONE!" + Fore.RESET + "\n" + "#" * 50)
print("")
print("")
print("")
print("")
time.sleep(2)

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 1

for x in range(amount):
    password = "".join(random.sample(all,length))
    print(Fore.LIGHTWHITE_EX +"                         Your Password is: " + Fore.GREEN + password)
    print("hey")
    print("")
    print("")
    print("")
    quit()
