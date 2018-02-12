import socket
import subprocess
import sys
import random
from random import randint
import time
from datetime import datetime

subprocess.call('clear', shell=True)

def scan1(remoteServerIP):
    sec = input("Choose how long time to sleep\n")
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60
    file = open('Open_Ports.txt', 'w+')
    file.write('Those ports are open:\n')
    socket.setdefaulttimeout(0.05)

    try:

        counter = 0
        for port in range(65535):
            if counter%10==0:
                 print "waiting {} seconds".format(sec)
                 time.sleep(sec)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
                file.write("port {}\n".format(port))
            counter=counter+1
            sock.close()
            file.closed

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    return None

def scan2 (remoteServerIP):
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60
    file = open('Open_Ports.txt', 'w+')
    file.write('Those ports are open:\n')
    socket.setdefaulttimeout(1)
    counter = 0
    try:
       while counter<1000:
            port = randint(1, 65000)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            print "Try {}".format(port)
            if result == 0:
                print "Port {}: 	 Open".format(port)
                file.write("port {}\n".format(port))
            counter = counter + 1
            sock.close()
            file.closed

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
         print 'Hostname could not be resolved. Exiting'
         sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    return None


def scan3 (remoteServerIP):
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60
    list_of_ports=[21,22,23,25,53,80,443,110,135,137,138,139,1433,1434]

    file = open('Open_Ports.txt', 'w+')
    file.write('Those ports are open:\n')
    socket.setdefaulttimeout(1)
    try:
        for i in range(len(list_of_ports)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, list_of_ports[i]))
            if result == 0:
                print "Port {}: 	 Open".format(list_of_ports[i])
                file.write("port {}\n".format(list_of_ports[i]))
            else:
                print "port {}:      close".format(list_of_ports[i])
            sock.close()
            file.closed

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()


def main():
    remoteServer    = raw_input("Enter a ip host to scan:\n ")
    version      = input("Choose:\nNaive scan (1)\nRandom scan (2)\nSmart scan (3)\n")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    if version==1:
        scan1(remoteServerIP)
    elif version==2:
        scan2(remoteServerIP)
    elif version==3:
        scan3(remoteServerIP)

if __name__ == '__main__':
    main()