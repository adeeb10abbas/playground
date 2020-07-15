import bcrypt as bp  
import string
import itertools
import time
import multiprocessing
import tqdm 
import sys
import os
import warnings
warnings.simplefilter(action='ignore')


combinations_generator = itertools.product(string.ascii_lowercase, repeat=2) #repeat=2
combinations = list(map(''.join, combinations_generator))
f = open("student_pwd.txt", 'r')


adeeb_pass = f.readlines()[0].split(',')[1]
# friend_1 = f.readlines()[1].split(',')[1]
# friend_2 = f.readlines()[2].split(',')[1]

def run(k):
    passwd = combinations[k]
    hashed = bp.hashpw(passwd.encode(), bp.gensalt())
    if bp.checkpw(hashed, adeeb_pass.encode()):
        print("Password Matches")
        print(passwd.decode())
        sys.exit()


def main():
    pool = multiprocessing.Pool(os.cpu_count())
    length = range(len(combinations))
    start_time = time.time()
    for _ in tqdm.tqdm(pool.imap_unordered(run, length), total=len(combinations)):
        pass
    end = time.time()
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
