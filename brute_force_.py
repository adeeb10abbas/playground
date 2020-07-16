import bcrypt as bp  
import string
import itertools
import time
import multiprocessing
import sys
import os
import warnings
warnings.simplefilter(action='ignore')
from functools import partial


combinations_generator = itertools.product(string.ascii_lowercase, repeat=2) #repeat=2
combinations = list(map(''.join, combinations_generator))
f = open("student_pwd.txt", 'r')

listOfLines = f.readlines()
adeeb_pass = listOfLines[0]
friend_1 = listOfLines[1]
friend_2 = listOfLines[2]

def runner(hash):
    hash_ = hash.split(',')[1].strip()
    start = time.time()
    for passwd in combinations:
        if bp.checkpw(passwd.encode(), hash_.encode()):
            print("Password Matches: ", passwd)
            break
    end = time.time()
    print("Time taken to decode %s is %.2f mins and the password is %s"%(hash.split(',')[0], (end-start)/60, passwd))

def main():
    runner(adeeb_pass)
    runner(friend_1)
    runner(friend_2)
main()
