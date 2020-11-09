"""
Cybersecurity Project #2
Author: Joe Roybal
Date: 11/09/2020
Goal: Access the ftp service on a Windows Server using the credentials [ anonymous : you@southwestern.edu ]
"""
from ftplib import FTP


def getUser():
    return "anonymous"


def getPass():
    return "roybalj@southwestern.edu"


def main():
    print("Enter FTP IP address:")
    target = raw_input()
    ftp = FTP(target)
    try:
        ftp.login(getUser(), getPass())
        print("Success!")
    except:
        print("Login Failed")
    ftp.quit()


if __name__ == "__main__":
    main()


"""
   _
 >(.)__
  (___/
Cyber Ducky Strikes Again!!!

"""
