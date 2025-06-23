import os
import sys

print(sys.path)
print("++++++++++++++++++++++++++")
print(type(os.getcwd()))
print(os.getcwd())
print(os.listdir(os.getcwd()))

now_dir = os.path.join(os.getcwd(), 'test')

if not os.path.exists(now_dir):
    os.mkdir(now_dir)
else:
    os.rmdir(now_dir)

dirpath = os.path.join(now_dir, 'test')

print(dirpath)