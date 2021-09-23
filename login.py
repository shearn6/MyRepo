import hashlib
from datetime import datetime
import getpass
import os
import time

def timestamp():
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S\n')
    return date

def new_user(name):
    while True:
        uName = input("What is your user name going to be?\n")
        pass1 = hashlib.md5(getpass.getpass("What is your password: ").encode("UTF-8")).hexdigest()
        pass2 = hashlib.md5(getpass.getpass("Confirm your password: ").encode("UTF-8")).hexdigest()
        if pass1 == pass2:
            with open("shadow.txt","a") as fShadow:
                fShadow.write(f"{uName} {pass1}\n")
            with open("log.txt","a") as flog:
                fShadow.write(f"New user: {uName}, created by: {name}, at: {timestamp()}\n")
                break
        else:
            print("Your passwords do not match")

new_user("System")