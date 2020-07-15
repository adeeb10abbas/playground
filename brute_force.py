import bcrypt as bp  
import string
import itertools
import time
import multiprocessing
import tqdm 

combinations_generator = itertools.product(string.ascii_lowercase, repeat=2)
combinations = list(map(''.join, combinations_generator))
print(len(combinations))
f = open("student_pwd.txt", 'r')


adeeb_pass = f.readlines()[0].split(',')[1]
# friend_1 = f.readlines()[1].split(',')[1]
# friend_2 = f.readlines()[2].split(',')[1]

start_time = time.time()
for passwd in combinations:
    hashed = bp.hashpw(passwd.encode(), bp.gensalt())
    if bp.checkpw(hashed, adeeb_pass.encode()):
        print("Password Matches")
        print(passwd.decode())
        break
end = time.time()
print('Time_taken :', (end-start_time)/60)

# def main():
#     pool = multiprocessing.Pool(1)
#     length = range(len(combinations))
#     start_time = time.time()
#     for _ in tqdm.tqdm(pool.imap_unordered(run, length), total=len(combinations)):
#         pass
#     end = time.time()
#     print('Time_taken :', end-start_time)
#     #range(len(X)
#     pool.close()
#     pool.join()
#     pool.close()

# main()