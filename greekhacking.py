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















































import colorama















import requests















import time















import os, sys















import http.client as httplib















from colorama import *















colorama.init()







yes_choice = ['','Yes', 'y', 'Y', 'yes', 'YES']



no_choice = ['No', 'n', 'no', 'NO', 'N']















































versionpath = ("core", "version.txt") 















os.system("cls||clear")















































print(Fore.GREEN + "")
















































































def check_updates():















    try:















        conn = httplib.HTTPSConnection("raw.githubusercontent.com")















        conn.request("GET", "/MataGreek/greekhacking/main/core/version.txt")











        repoVersion = conn.getresponse().read().strip().decode()







        print("")













        print(Fore.GREEN + "")











        with open('./core/version.txt') as vf:











            currentVersion = vf.read().strip()























        if repoVersion == currentVersion:







            print("")















        else:










                print("""

                 ??????       ??????  ?????????????????????????????????  ?????????????????????????????????  ?????????????????????????????????       ?????????????????????????????????  ?????????????????????????????????  ???         
????????????     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????     ???????????????????????????????????????????????????????????????????????????????????????       ????????????????????????????????????????????????
???????????????   ?????????????????????????????????????????????????????? ????????????????????????????????? ???????????????????????????????????????     ???????????????????????????????????? ????????????????????????????????????????????????       ????????????????????????????????????????????? 
?????????????????? ???????????????????????????       ?????????     ?????????     ?????????       ?????????     ?????????          ?????????       ??????????????????       ??????????????????          
????????? ??????????????? ????????????????????????????????????????????????     ?????????     ???????????????????????????????????????     ???????????????????????????????????? ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 
?????????  ?????????  ????????????????????????????????????????????????     ?????????     ???????????????????????????????????????     ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
?????????   ???   ????????????????????????????????????????????????     ?????????     ???????????????????????????????????????      ??????????????????????????????????????????????????????????????????????????? ?????????????????????????????????  ????????????????????????????????????
?????????       ??????????????????       ?????????     ?????????     ?????????       ?????????               ??????????????????       ?????????     ?????????               ?????????
?????????       ??????????????????       ?????????     ?????????     ?????????       ?????????      ?????????????????????????????????????????????       ?????????     ?????????      ????????????????????????????????????
?????????       ??????????????????       ?????????     ?????????     ?????????       ?????????     ????????????????????????????????????????????????       ?????????     ?????????     ???????????????????????????????????????
 ???         ???  ???         ???       ???       ???         ???       ?????????????????????????????????  ???         ???       ???       ????????????????????????????????? 
                                                                                                              """)

                print("")
                print("")
                
                




                ask = input("  [+] Version "+str(repoVersion)+" Is Available! Do you want to update? [Y/n]:   ")















                if ask in yes_choice:







                    print("")







                    print("  [!] Updating... Please do not close your application.")







                    print("")







                    time.sleep(4)



                    











                    try:











                        conn.request("GET", "/MataGreek/greekhacking/main/greekhacking.py")











                        newCode = conn.getresponse().read().strip().decode()



                        











                        with open('greekhacking.py', 'w+') as gr:







                            currentgr = gr.read().strip()







                            if newCode != currentgr:







                                gr.write(newCode)



                    except KeyboardInterrupt:



                        print("Exit.")



                    try:



                        conn.request("GET", "/MataGreek/greekhacking/main/files/password.py")







                        newcode1 = conn.getresponse().read().strip().decode()







                        with open('./files/password.py', 'w+') as ps:



                            currentps = ps.read().strip()



                            if newcode1 != currentps:



                                ps.write(newcode1)



                    except KeyboardInterrupt:



                        print("exit.")







                    



                    



                    try:



                        conn.request("GET", "/MataGreek/greekhacking/main/files/port.py")



                        newcode5 = conn.getresponse().read().strip().decode()







                        with open('./files/port.py', 'w+') as pr:



                            currentpr = pr.read().strip()



                            if newcode5 != currentpr:



                                pr.write(newcode5)



                    except KeyboardInterrupt:



                        print("exit.")



                    



                    try:



                        conn.request("GET", "/MataGreek/greekhacking/main/files/proxy.py")



                        newcode6 = conn.getresponse().read().strip().decode()







                        with open('./files/proxy.py', 'w+') as px:



                            currentpx = px.read().strip()



                            if newcode6 != currentpx:



                                px.write(newcode6)



                    except KeyboardInterrupt:



                        print("exit.")



                    try:



                        conn.request("GET", "/MataGreek/greekhacking/main/files/admin.py")



                        newcode7 = conn.getresponse().read().strip().decode()







                        with open('./files/admin.py', 'w+') as ad:



                            currentad = ad.read().strip()



                            if newcode7 != currentad:



                                ad.write(newcode7)



                    except KeyboardInterrupt:



                        print("exit.")



                    try:



                        conn.request("GET", "/MataGreek/greekhacking/main/files/subfinder.py")



                        newcode8 = conn.getresponse().read().strip().decode()







                        with open('./files/subfinder.py', 'w+') as su:



                            currentsu = su.read().strip()



                            if newcode8 != currentsu:



                                su.write(newcode8)

                    except KeyboardInterrupt:

                        print("exit.")



                    try:

                        conn.request("GET", "/MataGreek/greekhacking/main/setup.py")

                        newcode9 = conn.getresponse().read().strip().decode()

                        with open('setup.py', 'w+') as se:

                            currentse = se.read().strip()

                            if newcode9 != currentse:

                                se.write(newcode9)

                    except KeyboardInterrupt:

                        print("exit.")

                    

                    try:

                        conn.request("GET", "/MataGreek/greekhacking/main/subdomain.txt")

                        newcode10 = conn.getresponse().read().strip().decode()

                        with open('subdomain.txt', 'w+') as st:

                            currentst = st.read().strip()

                            if newcode10 != currentst:

                                st.write(newcode10)

                    except KeyboardInterrupt:

                        print("exit.")

                    try:

                        conn.request("GET", "/MataGreek/greekhacking/main/requirements.txt")

                        newcode11 = conn.getresponse().read().strip().decode()

                        with open('requirements.txt', 'w+') as req:

                            currentreq = req.read().strip()

                            if newcode11 != currentreq:

                                req.write(newcode11)

                    except KeyboardInterrupt:

                        print("exit.")

                    try:

                        conn.request("GET", "/MataGreek/greekhacking/main/files/cracker.py")

                        newcode12 = conn.getresponse().read().strip().decode()

                        with open('./files/cracker.py', 'w+') as cra:

                            currentcra = cra.read().strip()

                            if newcode12 != currentcra:

                                cra.write(newcode12)

                    except KeyboardInterrupt:

                        print("exit.")

                    

                    try:

                        conn.request("GET", "/MataGreek/greekhacking/main/files/fuzzyfa.py")

                        newcode13 = conn.getresponse().read().strip().decode()

                        with open('./files/fuzzyfa.py', 'w+') as fuz:

                            currentfuz = fuz.read().strip()

                            if newcode13 != currentfuz:

                                fuz.write(newcode13)

                    except KeyboardInterrupt:

                        print("exit.")

                    try:

                        conn.request("GET", "/MataGreek/greekhacking/main/fuzz.txt")

                        newcode14 = conn.getresponse().read().strip().decode()

                        with open('fuzz.txt', 'w+') as fuztxt:

                            currentfuztxt = fuztxt.read().strip()

                            if newcode14 != currentfuztxt:

                                fuztxt.write(newcode14)



                        print("")







                        print("  [+] Updated!")







                        time.sleep(1)



                    

                        print("")
                        print(Fore.RED+" REOPEN THE PROGRAM FOR UPDATES TAKE AFFECT"+Fore.RESET)
                        print("")







                        pass                              







                        if repoVersion != currentVersion:



                                with open('./core/version.txt', 'w+') as pf:







                                        pf.write(repoVersion)



                                                               



                        else:







                                print(Fore.RED + " [!] Your version is:", currentVersion + "You are not up to date! Please update the program." + Fore.GREEN)



                          



                    except KeyboardInterrupt:















                        print()











                   































    except Exception as e:















            print(Fore.RED + "Unable to Check for Update, Error:", str(e) + Fore.RESET)








    print("""  ____ ____  _____ _____ _  __  _   _    _    ____ _  _____ _   _  ____ """+"v"+str(repoVersion))
    print(""" / ___|  _ \| ____| ____| |/ / | | | |  / \  / ___| |/ /_ _| \ | |/ ___|""")
    print("""| |  _| |_) |  _| |  _| | ' /  | |_| | / _ \| |   | ' / | ||  \| | |  _ """)
    print("""| |_| |  _ <| |___| |___| . \  |  _  |/ ___ \ |___| . \ | || |\  | |_| |""")
    print(""" \____|_| \_\_____|_____|_|\_\ |_|| _/_/   \_\____|_|\_\___|_| \_|\____| """)

    print("#" * 100)















    print("                                 Author: MATA    |   https://www.greekhacking.gr/")















    print("#" * 100)


check_updates()

















print("")



















print("""



[01] Subdomain Finder                               

[02] Admin Login Finder

[03] Port Scanner

[04] Password Generator

[05] Proxy List

[06] MD5 Cracker

[07] Dir Scanning

[0] Exit.""")















print("")















print("")































































































































Question = (int(input("     [?] Choose -->  ")))















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





if Question == 7:

    from files import fuzzyfa



















if Question == 0:















    print("")















    print("")















    print("     Exiting.........")















    time.sleep(1)















    quit()