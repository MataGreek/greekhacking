import random

import time

import pyfiglet

import os, sys  

from typing import Text

import hashlib

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

try:
    Question = input("  Do you want to Generate a safe password?(Y/n) :   ")



    if Question == '' or 'Y' or 'y' or 'Yes' or 'yes' or 'YES':

        print("")
        pass

        

    else:
        quit()

except Exception as e:
    print("Error: ", e)
    



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

    print("")

    print("")

    print("")

    print(Fore.WHITE + "")

    ask = input("   Do you want to encrypt it? (Y/n):  " + Fore.GREEN)

    if ask == '' or 'y' or 'Y' or 'YES' or 'yes' or 'Yes':



                result = hashlib.md5(password.encode())

                print("")

                print("")

                print("")

                print(Fore.GREEN + "                        Your hashed password is: " + Fore.RED, end="")

                print(result.hexdigest())

                print("")

                print("")

                print("")

    if ask == 'no' or 'n' or 'NO' or 'No' or 'N':
        print(" Exit.")
        quit()