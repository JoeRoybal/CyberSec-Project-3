"""
Cybersecurity Project #4
Author: Joe Roybal
Date: 11/23/2020
Goal: Access the ftp service on a Windows Server using the credentials [ anonymous : you@southwestern.edu ]
"""
from ftplib import FTP


def FTPAttempt():
    print("Enter FTP IP address:")
    target = raw_input()  # raw_input() if python 2 & input() for python 3
    user, password = bruteForce("userPass.txt")
    ftp = FTP(target)
    try:
        ftp.login(user, password)
        print("Success!")
    except:
        print("Login Failed")
    ftp.quit()


def bruteForce(passwdFile):
    pFile = open(passwdFile, 'r')
    for line in pFile.readlines():
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
    return username, password


if __name__ == "__main__":
    FTPAttempt()


"""
   _
 >(.)__
  (___/
Cyber Ducky Strikes Again!!!

"""
