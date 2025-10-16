from pygame.scrap import contains

import os
import sys
import shutil
# # os.rmdir('D:/PythonProject1/papka')
# text_file=open('test.txt',"w")
# text_file.write('abeme')
# os.mkdir('papka')
# os.rename('test.txt','D:/PythonProject1/papka/test.txt')
# os.remove('D:/PythonProject1/papka/test.txt')
# os.rmdir('D:/PythonProject1/papka')
# print(os.listdir())
#
# if not os.path.exists('D:/PythonProject1/papaka'):
#     os.mkdir('papka')
#     print('Папка создана')
# else:
#
# print(os.getcwd())
# print(os.listdir())
# # os.mkdir("1")
# os.mkdir("2")
# os.mkdir("3")
# print(os.listdir())

# os.rmdir('3')
# print(os.listdir())
# os.rename('lol.txt', "lolkek.txt")

# print(os.listdir())
# a= os.path.exists('lolkek.txt')
# print(a)
# path = os.getcwd()
# os.rename('lolkek.txt','D:/PythonProject1/2/lolkek.txt')








#
# os.rmdir('papka1')
# os.mkdir('papka1')
# os.rmdir('papka')

# os.getcwd()
# os.mkdir('papka1')
# os.mkdir('papka')
# os.chdir('papka1')
# text_file=open('test.txt',"w")
# shutil.move('test.txt','PythonProject1/papka/test.txt')
# os.listdir

# print(sys.version)
# print(sys.platform)
# sys.stdout.write('ctandart viviod' "\n")
# fail=open('fail.txt','w')
# fail.write('Тест,Test')
# fail.close()
#
# f = open('fail.txt','r')
# # print(f.read())
# # print("===========")
# print(f.readline())
# f.close()

if not os.path.exists('D:/PythonProject1/111'):
    os.mkdir('111')
    print('папка 111 создана')
if not os.path.exists('D:/PythonProject1/222'):
    os.mkdir('222')
    print('папка 222 создана')
os.chdir('..')
os.chdir('111')
file=open('test.txt','w')
file.write('Hello, World')
file.close()
os.rename('D:/PythonProject1/111/test.txt','D:/PythonProject1/222/test.txt')
print(os.getcwd())
os.chdir('..')
os.chdir('222')
file=open('test.txt','a')
file.write('Hello,<Алексей>')
file.close()
file=open('test.txt','r')
print(file.read())
