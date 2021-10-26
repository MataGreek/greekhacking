#################################################

#################################################

#####       GREEK HACKING FORUM             #####

#####           PROXY LIST                  #####

#####            Copyright                  ##### 

#####     Greek Hacking �2021 Forum         #####                       

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







###################################################  IMPORTS   ###################################################





import socket

from ip2geotools.databases.noncommercial import DbIpCity

import pyfiglet

import colorama

import time

from colorama import *

colorama.init()

yes_choice = ['Yes', 'y', 'Y', 'yes', 'YES']
no_choice = ['No', 'n', 'no', 'NO', 'N']






###################################################  LOGO && QUESTION && STARTING   ###################################################





print(Fore.LIGHTBLUE_EX + "")

logo = pyfiglet.figlet_format("GH Proxy List")

print(logo)

print("" + Fore.RESET)



socket.setdefaulttimeout(0.5)

print("")

print("")

Question = input("Do you want to start scanning for proxies? (Y/N) ==>        ")

if Question in yes_choice:

    time.sleep(2)

    print("")

    print("")

    pass

else:

    time.sleep(1.5)

    print("")

    print("")

    print("Bye, thank you :)")

    print("")

    print("")

    quit()



print('\n' + '#' * 50 + '\n                 Starting Scan.....' + '\n' + '#' * 50)

time.sleep(3)

print("")

print("")

print("")



print(" IP Address" + "                 PORT" + "               COUNTRY" + "                      STATUS")

print("")

print("")





###################################################  SOCKETS && PRINTS && RESULTS   ###################################################



def port_check(ip,port):



    device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = device_socket.connect_ex((ip,port))

    response = DbIpCity.get(ip, api_key="free")



    if result == 0:

        print(str(ip) + "               " + Fore.LIGHTBLUE_EX + str(port) + Fore.YELLOW + "                  " + str(response.country) + Fore.GREEN + "                          Open" + Fore.RESET)

        device_socket.close()

        time.sleep(0.5)

    else:

        print(str(ip) + "               " + Fore.LIGHTBLUE_EX + str(port) + Fore.YELLOW + "                  " + str(response.country) + Fore.RED + "                      Closed" + Fore.RESET)

        device_socket.close()

        time.sleep(0.5)





###################################################  IP && PORT   ###################################################



port_check('88.255.234.192', 80)

port_check('182.23.107.210', 3128)

port_check('152.32.187.208', 80)

port_check('43.255.113.232', 82)

port_check('95.165.187.202', 45396)

port_check('41.138.166.6', 80)

port_check('93.157.163.66', 35081)

port_check('200.111.182.6', 443)

port_check('110.74.222.71', 44970)

port_check('140.227.211.47', 8080)

port_check('82.114.106.40', 1256)

port_check('222.74.202.240', 82)

port_check('113.255.189.126', 443)

port_check('43.224.10.27', 6666)

port_check('222.74.202.242', 8080)

port_check('175.101.16.65', 82)

port_check('80.154.203.122', 8080)

port_check('190.11.192.118', 999)

port_check('79.142.95.90', 55443)

port_check('180.87.102.69', 80)

port_check('64.124.38.139', 8080)

port_check('27.72.149.205', 8080)

port_check('147.92.41.56', 80)

port_check('5.11.17.105', 8090)

port_check('95.140.27.135', 58901)

port_check('85.84.14.9', 80)

port_check('43.224.8.124', 6666)

port_check('222.74.202.234', 8080)

port_check('209.141.56.127', 80)

port_check('200.46.65.66', 8080)

port_check('190.13.82.102', 999)

port_check('43.250.127.98', 9001)

port_check('64.124.38.26', 8080)

port_check('41.161.92.138', 8080)

port_check('82.65.35.131', 8080)

port_check('202.1.197.227', 80)

port_check('34.132.61.61', 3127)

port_check('152.67.204.155', 80)

port_check('158.177.253.24', 80)

port_check('111.118.218.126', 8080)

port_check('109.254.124.106', 9090)

port_check('140.227.25.56', 5678)

port_check('109.195.23.223', 34031)

port_check('188.166.162.1', 3128)

port_check('113.176.94.186', 8080)

port_check('144.91.86.144', 3128)

port_check('1.20.166.142', 8080)

port_check('202.150.158.170', 8080)

port_check('79.101.67.154', 8080)

port_check('201.184.53.179', 999)









###################################################  COUNTRIES && Cities   ###################################################





#### Turkey

#### Indonesia				

#### United States

#### Japan	

##### Russia 

##### Chile 	

##### Russia 

#### Cambodia	

#### China	

#### Hong Kong

#### India

#### Germany

#### Argentina 

#### Kazakhstan

####Viet Nam

#### Europe

#### Spain

#### Canada

#### Panama	

#### South Africa

#### France

#### Maldives

#### United Kingdom 	

#### Australia

#### Ukraine 

#### Thailand

#### Indonesia

#### Serbia

#### Colombia