import os 
import subprocess
from time import sleep


def menu():
    print(
"""
1. Connection status 
2. list of networks
3. Disconnect from the current network
4. Connect to the network
5. Network adapter status
6. Previously connected networks

0. Exit
""")

    main()      

def main(): 
    choise = None
    while choise != "0":
        choise = input("#: ")
        if choise == "1":
            subprocess.run(["nmcli", "general", "status"])
        elif choise == "2":
            subprocess.run(["nmcli", "device", "wifi", "list"])
        elif choise == "3":
            subprocess.run(["nmcli", "radio", "wifi", "off"])
            sleep(0.3)
            subprocess.run(["nmcli", "radio", "wifi", "on"])
        elif choise == "4":
            login = input("Enter login: ")
            password = input("Enter password: ")
            subprocess.run(["nmcli", "device", "wifi", "connect", "\"" + login + "\"", "password", password, "name", "\"" + login + " Wifi" + "\""])
        elif choise == "5":
            subprocess.run(["nmcli", "radio", "wifi"])
        elif choise == "6":
            subprocess.run(["nmcli", "connection", "show"])
        else:
            print("command not found")

menu()