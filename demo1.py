import calc
print(calc.add(200, 300))

# import sys
# print(dir(sys))
# print(sys.getsizeof('123'))

# import time
# print(time.time())
# file = open("/Users/yangkuo/个人文件/Learn_program/python_learn/a.txt", '+r')
# # file.write("hello world")
# print(file.readlines()) 
# file.close()
with open('/Users/yangkuo/个人文件/Learn_program/python_learn/a.txt', 'r') as file:
    print(file.read())
import os
os.system("pwd")  # 显示文件目录的命令
print(os.getcwd())
# os.mkdir("yangkuo")
# os.rmdir("yangkuo")
