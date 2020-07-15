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
from functools import partial


combinations_generator = itertools.product(string.ascii_lowercase, repeat=2) #repeat=2
combinations = list(map(''.join, combinations_generator))
f = open("student_pwd.txt", 'r')

adeeb_pass = f.readlines()[0].split(',')[1]
# print(adeeb_pass)
# def run(k):
for passwd in combinations:
    # passwd = combinations[k]
    if bp.checkpw(passwd.encode(), adeeb_pass.encode()) is True:
        print("Password Matches")
        print(passwd)
# print(combinations)

# def main():
#     pool = multiprocessing.Pool(os.cpu_count() - 1)
#     length = range(len(combinations))
#     start_time = time.time()
#     for _ in tqdm.tqdm(pool.imap_unordered(run, length), total=len(combinations)):
#         pass
#     end = time.time()
#     print((end-start_time)/60)
#     pool.close()
#     pool.join()

# if __name__ == "__main__":
#     main()
