import os
import random, math
import time
import subprocess
from subprocess import *
import geocoder
import scapy.all as scapy
import re
import socket
from datetime import datetime
import sys
import zstandard



os.system('cls')
aninames = ['/','—',"\ ",'|']
aniframes = 0 


for i in range(8):
        if aniframes == 4:
                aniframes = 0
        print("...", aninames[aniframes])
        time.sleep(0.1)
        aniframes = aniframes + 1
        os.system('cls')



tslow = 0.00000000000001

def tw(message):
        for char in message:
                sys.stdout.write(char)
                sys.stdout.flush
                time.sleep(tslow)
        print()


def twf(message):
        for char in message:
                sys.stdout.write(char)
                sys.stdout.flush
                time.sleep(0)
        print()



timenow = datetime.now()
current_time = timenow.strftime("%H:%M:%S")
lineskip = ("-----------------------------")
longlineskip = ("---------------------------------------------")


welcomeintro = f"""{longlineskip}
     ___   _      _   _   _            _    
    / / \ | | ___| |_| | | | __ _  ___| | __
   / /|  \| |/ _ \ __| |_| |/ _` |/ __| |/ /
  / / | |\  |  __/ |_|  _  | (_| | (__|   < 
 /_/  |_| \_|\___|\__|_| |_|\__,_|\___|_|\_\.
"""
time.sleep(0.5)
tw(welcomeintro)
tw(current_time)
tw("Version 2.9 | Copyright 2021-2022 | OjanRN/M3D4NG")
tw(longlineskip)
print("\n")

def start():

    while True:
        print("")
        print("|")
        usercm1 = input("L@-")
        if usercm1 == "/h":
            print("\n")
            tw(f"{lineskip}")
            tw("IPInfo Commands:")
            tw(f"{lineskip}")
            twf(f"get ipw = Get the IP Adress of a WWW link(example:google.com)")
            twf(f"get iphn = Get hostname and IP address")
            twf(f"get hn = Get hostname")
            twf(f"get iph = Get ip by hostname")
            twf(f"locate me = Get current host's IP Address")
            twf(f"locate ip = Locate an IP Adress")
            tw(f"{lineskip}")
            tw("Network Interface Commands:")
            tw(f"{lineskip}")
            twf(f"scanforprofiles = Scan the network profiles on the current pc")
            twf(f"scanprofile = View information about a network profile on the host")
            twf(f"scanallprofiles = Scan all profiles and key available on the host")
            twf(f"connect = Connect to a wifi by using a registered profile")
            twf(f"dconnect = Disconnect current connected wifi")
            tw(f"{lineskip}")
            tw("Network Commands:")
            tw(f"{lineskip}")
            twf(f"ping = Ping/Send package to an IP Address")
            twf(f"get ipl = Get IP Addresses connected to the network your connected")
            twf(f"scanlocalnet = Scan all IP TCP connected to home network")
            tw(f"{lineskip}")
            tw("Disabled Commands:")
            tw(f"{lineskip}")
            twf(f"changehostpass = Change host's password - Disabled because it can change accidentally")
            tw(f"{lineskip}")
            tw("Program Commands")
            tw(f"{lineskip}")
            twf(f"/matrix = Create a hacker style matrix of one and zeros")
            twf(f"/credits = Credits")
            twf(f"/exit = Exit the program")
            twf(f"/h = List commands")
            twf(f"/clear = Clears the command line")
            tw(f"{lineskip}")
            tw("Additional Notes:")
            tw(f"{lineskip}")
            tw("For commands like get ping,scanallprofiles,scanprofile,connect,etc requires additional input like network name and stuffs like that")
            
            print("\n")
            continue
        elif usercm1 == "get":
            tw("Please specify 'get' or type/h to list all commands")
        elif usercm1 == "scan":
            tw("Please specify 'scan' or type /h to list all commands")
        elif usercm1 == "scanforprofiles":
            p1 = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True).stdout.decode()
            p2 = (re.findall("All User Profile     : (.*)\r", p1))
            tw(f"Profiles available to scan:")
            tw("\n")
            ind = 0
            for i in range(len(p2)):
                    if ind < len(p2):
                            tw(f"< {p2[ind]} >")
                            ind = ind + 1
                    elif ind == len(p2):
                            ind = 0
                            break
            tw("\n")
            continue
        elif usercm1 == "scanprofile" or usercm1 == "scanprofiles":
                print("\n")
                tw("Scan Options?")
                print("")
                tw("[1] Key Only")
                tw("[2] Fullscan")
                print("")
                print("|")
                useropt1 = input("L@-")
                print("\n")
                if useropt1 == "1":
                        print("|")
                        netName = input("L@-")
                        p1 = subprocess.run(['netsh', 'wlan', 'show', 'profiles', netName, 'key=clear'], capture_output=True).stdout.decode()
                        if "Key Content" in p1:
                                p2 = (re.findall("Key Content            : (.*)\r", p1))
                                tw("\n")
                                tw("Key = Present")
                                tw(f"Key Is {p2[0]}")
                                tw("")
                                continue
                        else:
                                tw("The SSID is wrong or it has no key \n")
                                continue
                elif useropt1 == "2":
                        print("|")
                        netName = input("L@-")
                        profilescan = subprocess.run(['netsh', 'wlan', 'show', 'profile', netName, 'key=clear'], capture_output=True).stdout.decode()
                        print(profilescan)
                        tw("for the password/key, look for Key Content")
                else:
                        tw("Incorrect SSID")
                continue
        elif usercm1 == "connect":
                print("\n")
                print("|")
                rqNetName = input("L@-")
                cncommand = subprocess.run(['netsh', 'wlan', 'connect', rqNetName], capture_output=True, shell=True).stdout.decode()
                tw(cncommand)
                continue
        elif usercm1 == "dconnect":
                print("\n")
                dcncommand = subprocess.run(['netsh', 'wlan', 'disconnect'], capture_output=True).stdout.decode()
                tw(dcncommand)
                tw("Disconnected this pc from wifi")
                continue
        elif usercm1 =="ping":
                print("\n")
                print("|")
                pingad = input("L@-")
                pingcommand = subprocess.run(['ping','-f', pingad])
                tw(f"{pingcommand.stdout}")
                tw("Pinging")
                continue
#        elif usercm1 =="changepass":
#                print("\n")
#                print("|")
#                userinp = input("L@-")
#                passinp = input("L@-")
#                netusercmd = subprocess.run(['net', 'user', userinp, passinp ])
#                tw(netusercmd)
#                continue
        elif usercm1 == "get ipw":
                print("\n")
                print("|")
                nspinp = input("L@-")
                nspcmd = subprocess.run(['nslookup', nspinp], shell=True)
                tw(f"{nspcmd}")
                continue
        elif usercm1 == "get ipl":
                print("\n")
                ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
                tw("Scanning method?")
                tw("")
                tw("[1] Scapy (Requires NPCap provider, available in website)")
                tw("[2] arp -a (Does not require NPCap)")
                print("|")
                useropt1 = input("L@-")
                if useropt1 == "1":
                        print("\n")
                        ip_add_range_entered = "192.168.0.1/24"
                        if ip_add_range_pattern.search(ip_add_range_entered):
                                tw(f"{ip_add_range_entered} is a valid ip address range")
                                arp_result = scapy.arping(ip_add_range_entered)
                                continue
                        else:
                                tw("Incrorrect input,(example:192.xxx.x.x/24")
                                continue
                elif useropt1 == "2":
                        print("\n")
                        arpscan = subprocess.run(['arp', '-a'], capture_output=True).stdout.decode()
                        print(arpscan)
                        continue
                continue
        elif usercm1 == "get hn":
                print("\n")
                hostname = subprocess.run(['hostname'], capture_output=True).stdout.decode()
                tw(f"hostname is: {hostname}")
                continue
        elif usercm1 == "get iph":
                print("\n")
                print("|")
                gh = input("L@-")
                iphost = socket.gethostbyname(gh)
                tw(f"IPv4: {iphost}")
                continue
        elif usercm1 == "get iphn":
                print("\n")
                gh = socket.gethostname()
                iphost = socket.gethostbyname(gh)
                tw(f"IPv4: {iphost}")
                tw(f"Hostname: {gh}")
                continue
        elif usercm1 == "locate me":
                print("\n")
                ip = geocoder.ip("me")
                tw(f"{lineskip}")
                tw(f"[+] IP: {ip.ip}")
                tw(f"[+] Coordinates: {ip.latlng}")
                tw(f"[+] City: {ip.city}")
                tw(f"[+] State/Province: {ip.state}")
                tw(f"[+] Postal Code: {ip.postal}")
                tw(f"[+] Country: {ip.country}")
                tw(f"[+] ASN/Org: {ip.org}")
                tw(f"{lineskip}")
                continue
        elif usercm1 == "locate ip":
                print("\n")
                print("|")
                location = input("L@-")
                locationdata = geocoder.ip(location)
                tw(f"{lineskip}")
                tw(f"[+] IP: {location}")
                tw(f"[+] Coordinates: {locationdata.latlng}")
                tw(f"[+] City:  {locationdata.city}")
                tw(f"[+] State/Province: {locationdata.state}")
                tw(f"[+] Postal Code:  {locationdata.postal}")
                tw(f"[+] Country:  {locationdata.country}")
                tw(f"[+] ASN/Org: {locationdata.org}")
                tw(f"{lineskip} \n")
                continue
        elif usercm1 == "scanlocalnet":
                print("\n")
                iplist = subprocess.run(['netstat', '-an'], capture_output=True).stdout.decode()
                print(f"Detected: {iplist}")
                continue
        elif usercm1 == "scanallprofiles":
                print("\n")
                proData = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True).stdout.decode()
                p2 = (re.findall("All User Profile     : (.*)\r", proData))
                tw("\n")
                ind = 0
                passlist = []
                for i in range(len(p2)):
                    if ind < len(p2):
                            proPass = subprocess.run(['netsh', 'wlan', 'show', 'profile', p2[ind], 'key=clear'], capture_output=True).stdout.decode()
                            passData = (re.findall("Key Content            : (.*)\r", proPass))
                            passlist.append(passData)
                            ind = ind + 1
                ind = 0
                print("             SSID             |             Key             ")
                print("                              |                             ")
                for i in range(len(p2)):
                        if ind < len(p2):
                                p2linespace = " "*(30-len(p2[ind]))
                                tw("{SSID}{linespace}| {Key}".format(SSID = p2[ind], linespace = p2linespace, Key = passlist[ind]))
                                time.sleep(0.2)
                                ind = ind + 1
                        elif ind == len(p2):
                                ind = 0
                                break
                continue
        elif usercm1 == "/matrix":
                print("animation starting...,this is a while loop,meaning it won't stop until you close the application")
                time.sleep(5)
                matrix = subprocess.run(['-matrix'], capture_output=True)
                print(matrix)
        elif usercm1 == "/credits":
                print("\n")
                print(lineskip)
                tw("Tools Used:")
                tw("VSCode - Text Editor")
                tw("PyInstaller - py to exe converter")
                tw("Coded in Python 3.9")
                print(lineskip)
                tw("Icon Used:")
                tw("Icon by Freepik:Flaticon Link \/")
                tw("https://www.flaticon.com/free-icons/security Security icons created by Freepik - Flaticon")
                print(lineskip)
                tw("Created By:OjanRN")
                tw("Github \/")
                tw("https://github.com/OjanRN")
                print(lineskip)
                print("\n")
        elif usercm1 == "/clear":
                os.system('cls')
                print(longlineskip, """
     ___   _      _   _   _            _    
    / / \ | | ___| |_| | | | __ _  ___| | __
   / /|  \| |/ _ \ __| |_| |/ _` |/ __| |/ /
  / / | |\  |  __/ |_|  _  | (_| | (__|   < 
 /_/  |_| \_|\___|\__|_| |_|\__,_|\___|_|\_\.
                """)
                print(current_time)
                print("Version 2.9 | Copyright 2021-2022 | OjanRN/M3D4NG")
                print(longlineskip)
                print("\n")
                continue
        elif usercm1 == "/exit":
                tw("Are you sure? (Y/N)")
                print("|")
                yrn = input("L@-")
                if yrn == "Y" or yrn == "y":
                        tw("Exit confirmed")
                        tw("Exiting in 3 seconds")
                        time.sleep(3)
                        break #
                else: 
                        tw("Exit Canceled")
        else:
                tw("Incorrect Command")
                time.sleep(0.5)
                tw("Type /h to list all commands")
                continue
start()