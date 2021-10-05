#################################################



#################################################



#####       GREEK HACKING FORUM             #####



#####            Copyright                  ##### 



#####     Greek Hacking @2021 Forum         #####                       



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



        conn = httplib.HTTPSConnection("raw.githubusercontent.com")



        conn.request("GET", "/MataGreek/greekhacking/main/core/version.txt")



        repoVersion = conn.getresponse().read().strip().decode()

        print("")

        print("=" * 70)

        print(Fore.LIGHTBLUE_EX + " [!] Latest Version:",repoVersion + Fore.GREEN)

        print("=" * 70)



        print(Fore.GREEN + "")



        with open('./core/version.txt') as vf:



            currentVersion = vf.read().strip()







            print("")



            print("=" * 70)



            print(Fore.LIGHTBLUE_EX + " [*] Your Version: ",currentVersion + Fore.RESET)



            print(Fore.GREEN + "=" * 70)



            print("")



        if repoVersion == currentVersion:



            print("")



            print("=" * 70)



            print(" [*] The script is up to date!")



            print("=" * 70)



            print("")



        else:



                ask = input("  [+] An update has been found! Do you want to update? (Y/n):   ")



                if ask == '' or 'Yes' or 'yes' or 'YES' or 'Y' or 'y':

                    print("")

                    print("  [!] Updating... Please do not close your application.")

                    print("")

                    time.sleep(4)
                    

                    



                    try:



                        conn.request("GET", "/MataGreek/greekhacking/main/greekhacking.py")
                        conn.request("GET", "/MataGreek/greekhacking/main/files/password.py")
                        
                        



                        newCode = conn.getresponse().read().strip().decode()
                        newCode1 = conn.getresponse().read().strip().decode()

                        with open('./files/password.py', 'w+') as ps:
                            currentps = ps.read().strip()
                            
                            if newCode1 != currentps:
                                ps.write(newCode1)






                        with open('greekhacking.py', 'w+') as gr:



                            currentgr = gr.read().strip()



                            if newCode != currentgr:



                                gr.write(newCode)

                                print("")

                                print("  [+] Updated!")

                                time.sleep(1)

                                print(Fore.RED + " [!] PLEASE REOPEN THE PROGRAM!" + Fore.GREEN)



                                pass

                                

                            if repoVersion != currentVersion:

                                with open('./core/version.txt', 'w+') as pf:

                                        pf.write(repoVersion)
                            
                                    


                            else:



                                print(Fore.RED + " [!] Your version is:", currentVersion + "You are not up to date!" + Fore.GREEN)

                            

                    except KeyboardInterrupt:



                        print()


                   







    except Exception as e:



            print(Fore.RED + "Unable to Check for Update, Error:", str(e) + Fore.RESET)

check_updates()



















print("")



print("     [1] Subdomain Finder")



print("")





print("     [2] Admin Login Finder")



print("")



print("     [3] Port Scanner")



print("")



print("     [4] Password Generator")



print("")



print("     [5] Proxy List")



print("")



print("     [6] MD5 Cracker")



print("")



print("     [0] Exit.")



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