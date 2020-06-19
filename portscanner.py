# @author: Şükrü Erdem Gök https://github.com/SukruGokk
# @date: 19/06/2020
# @os: Windows 10 Python 3.8

# Simple port scanner with python

# Lib
import threading # I used threading to scan faster It really works so fast with thread
import socket
from os import system

# To print port' s service
portDict = {20: "FTP", 21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP", 50: "IPSec", 51: "IPSec", 53: "DNS",
            67: "DHCP", 68: "DHCP", 69: "TFTP", 80: "HTTP", 8080: "HTTP", 110: "POP3", 119: "NNTP", 123: "NTP",
            135: "NetBIOS", 139: "NetBIOS", 143: "IMAP4", 161: "SNMP", 162: "SNMP", 389: "LDAP", 443: "SSL",
            445: "MICROSOFT-DS",
            3389: "RDP"}


# Port scan function
def portscan(port):
    # Creates an object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    # Try-Except' s purpose is : if connected to port succesfully, prints it but if cant connect an error occurs and that means port is closed
    try:
        con = s.connect((target, port))

        print(port, "          ", portDict[int(port)])

        con.close()
    except:
        pass


# To use it again without restarting
while True:

    system("color b")

    # Get target
    target = input("------------IP OR WEBSITE------------\n")

    system("color a")

    # Method selection
    print(
        "\nCHOOSE ONE OF THEM: \n------------------------------------------------------------------\n1-) Write which ports do you want to scan\n2-) Write a range that program will scan(ex: scan ports between 50, and 150)\n3-) Scan general ports".upper())

    # I used while loop to get input until correct selection
    while True:

        print("CHOICE: ")

        try:
            choice = int(input())
            if choice > 0 and choice < 4:
                break
            else:
                raise NameError

        except:
            print("UNAVALIBLE")

    system("color d")

    # First method
    if choice == 1:

        # List of ports that will scan
        portList = []
        print("\nTO FINISH WRITE 's'")

        # Get ports
        while True:
            try:
                portInput = input("PORT NUMBER: ")
                portInput = int(portInput)
                portList.append(portInput)

            except:
                print(portInput)
                if portInput.lower() == "s":
                    break
                else:
                    print("Unavalible")

        print("\nOPEN PORTS\n")

        print("PORT        SERVICE")
        print("--------------------")

        # And scan them
        for portNumber in portList:
            t = threading.Thread(target=portscan, kwargs={'port': int(portNumber)})
            t.start()
            t.join()

    # Second method
    elif choice == 2:

        print("\n")

        # Get range
        while True:
            try:
                range1 = int(input("LOWEST RANGE: "))
            except:
                print("UNAVALIBLE")

            try:
                range2 = int(input("HIGHEST RANGE: "))
                break
            except:
                print("UNAVALIBLE")
        print("\nPORT        SERVICE")
        print("--------------------")

        for x in range(range1, range2):
            t = threading.Thread(target=portscan, kwargs={'port': x})
            t.start()
            t.join()

    # Third method
    elif choice == 3:

        print("\nPORT        SERVICE")
        print("--------------------")

        # Get portDict's keys and do scanning with them
        for x in list(portDict.keys()):
            t = threading.Thread(target=portscan, kwargs={'port': x})
            t.start()
            t.join()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")