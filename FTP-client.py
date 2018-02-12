import scapy
import sys
from scapy.all import *
from ftplib import FTP
import os

ftp = FTP('')
ftp.connect('127.0.0.1',1026)
ftp.login()
ftp.cwd('/uriel/Downloads') #the destination to upload or download from
ftp.retrlines('LIST')

def uploadFile():
 filename = '/home/uriel/Desktop/82241470100993640360no.jpg' #the path of the file i want to upload
 myFile= open(filename, 'rb')
 ftp.storbinary('STOR '+'test' ,myFile)# 'test' is the new name of file you uploading
 ftp.quit()

def downloadFile():
 filename = '82241470100993640360no.jpg' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()
#downloadFile()