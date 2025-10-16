# passw=(input("Введите пароль:"))
# if passw=="111":
#     print("Верный пароль")
# else:
#     print("Неверный")
#     exit()

# # 2 na 2 stolb 3-4
# for i in range (2):
#     d=4
#     for j in range(3,4):
#         print(j,d,sep="-")


# a=0
# for i in range(3):
#     print(end="\n")
#     for j in range(3):
#         a+=1
#         print(a,end=" ")

# a=0
# for i in range(3):
#     print(end="\n")
#     for j in range(3):
#         print(a,end=" ")


# chipsi=[1,2,"bua",4,True,47]
# for i in range(6):
#     print(chipsi[i])

# mass1=[22,23,25,26,27]
# for d in range(5):
#     print(mass1[d])
#
# print("==="*3)
#
# for e in range(5):
#     if e==2:
#         continue
#     print(mass1[e])
# #
# print("======")
#
# oreshki=mass1[0]+mass1[1]+mass1[2]+mass1[3]+mass1[4]
# # print(oreshki)
# #
# # print("======")
# print("==="*3)
# s=0
# for k in range(5):
#     s+=mass1[k]
# print(s)

# list1=[1,2,4,"a"]
# list1.append(42)
# print(list1)
# list1.insert(-2, "gol")
# print(list1)
#
# list2=[52,52,52]
# list1.extend(list2)
# print(list1)
#
# list1.remove(52)
# print(list1)
#
# list1.clear()
# print(list1)
#
# numbers = [1, 2, 3, 42, 4, 5, 42]
#
# # print(numbers.index(52))
# a = numbers.count(42)
# print(a)
#
# numbers.reverse()
# print(numbers)

# list1 = [1,2,3,4,5]
# list3=list1.copy()
# list2=['a','b','c','d','e']
# list4=list2.copy()
# list3.insert(1,(list4.pop(0)))
# list3.insert(3,(list4.pop(0)))
# list3.insert(5,(list4.pop(0)))
# list3.insert(7,(list4.pop(0)))
# list3.insert(9,(list4.pop(0)))
# print(f"\n{list3}")
# print(f"\n{list1}")
# print(f"\n{list2}")

# list1=[1,2,"we",3,"wer",4,5,6,"sad",7]
# list1.remove("we")
# list1.remove("wer")
# list1.remove("sad")
# print(sum(list1))
# list2=[]
# for i in range(7):
#     list2.append(list1.pop(0))
# print (list2)

# list1 = [1,True,2,"x",'eret',-2,'list1',2.5,False,3-77,'Hello World',4,-7,':-)',4.5,'index',]
# list2 = []
# list3=[]
# list4=[]
# list5=[]
# list6=[]
# # Найти сумму чисел
# # Найти количекство целых числ, вещественных чисел
# # Найти количество логических значений
# # Найти количество строковых значений
# list2.append(list1.pop(0))
# list2.append(list1.pop(1))
# list2.append(list1.pop(3))
# list2.append(list1.pop(4))
# list2.append(list1.pop(5))
# list2.append(list1.pop(6))
# list2.append(list1.pop(6))
# list2.append(list1.pop(7))
# print(f"Сумма целых чисел: {sum(list2)}")
#
# for i in list2:
#     if type(i)==int:
#         list3.append(i)
# print(f"Количество целых чисел: {len(list3)}")
# for d in list2:
#     if type(d)==float:
#         list4.append(i)
# print(f"Количество вещественных символов: {len(list4)}")
# for e in list1:
#     if type(e)==bool:
#         list5.append(e)
# print(f"Количество логических символов: {len(list5)}")
# for chi in list1:
#     if type(chi)==str:
#         list6.append(chi)
# print(f"Количество строк: {len(list6)}")


# a=input("Блины или чипсы? ")
# def cook(ingredients):
#     if a.lower()=="блины":
#         print(f"Ингредиенты: {cook1}")
#     elif a.lower()=="чипсы":
#         print(f"картошка","соль","хз")
# cook1="вода","мука","сахар"
# cook(cook1)


# list1 = [1,2,3,4,5]
# list3=list1.copy()
# list2=['a','b','c','d','e']
# for i in list1:
#     if i==3:
#         list1.remove(i)
# for i in list1:
#     if i==4:
#         list1.remove(i)
#
# for i in list2:
#     if i=='b':
#         list2.remove(i)
# print(list1,list2,sep=" | ")

# list1 = [1,2,3,4,5]
#
# tuple1=tuple(list1)
# print((tuple1))
# a, b, c, d, e=tuple1
# print(e)

# tuple1 = (1,2,3,4,5)
# list1 = list(tuple1)
# print(list1)
# list1.append(42)
# print(list1)
# tuple2 = tuple(list1)
# del tuple2
# print(tuple2)

# list1 = [1,2,3]
# list2 = [1,2,3]
# if list1==list2:
#     print("da")
# else:
#     print("no")

# tuple1 = ()
# i=0
# while True:
#     user_num=int(input("number="))
#     list1 =list(tuple1)
#     list1.append(user_num)
#     tuple1 = tuple (list1)
#
#     if i==3:
#         break
#     i+=1
# print(tuple1)
#
# list1 = ['1', ',', '2', ',', '3']
# list2= []
# for i in range (2):
#     list1.remove(',')
# print(list1)
#
# for i in list1:
#     list2.append(int(i))
#
# print(list2)
# tuple1 = tuple(list2)
# print((tuple1))

# #словарь
# pcinfo = {
#     "pc":"COMP10",
#     "gp":"Встройка",
#     "devices":"Мышь,Клавиатура,Монитор",
#     "ver win":"10.0.19045.6332",
#     "leng":"Русский",
#     "ether":"Intel(R) Ethernet Connection (2) I219-V",
#     "typesys":"Система x64",
#     "cp":"Intel64 Family 6 Model 94 Stepping 3 GenuineIntel",
#     "bios":"American Megatrends Inc. P2.00, 18.04.2017",
#     "ram":"8gb"

# }
# #удаление
# # print(pcinfo["ether"])
# # del pcinfo[("ram")]
#
# #получение
# print(pcinfo)
# a=input("Ключ для получения:")
# b= pcinfo.get(a,"нет такого")
# print(b)
#
# #изменение
# pcinfo['cp']= "незнаю"
# print(pcinfo["cp"])
#
# dogs1={
#     "poroda":"Овчарка",
#     "name":"Рекс",
#     "age":5,
#     "veskg":20,
#     "rostsm":85
# }
# dogs2=dogs1.copy()
# dogs2.update(poroda="Лайка")
# dogs2.update(name="Хай")
# dogs2.update(age=7)
# dogs2.update(veskg=23)
# dogs2.update(rostsm=100)
#
# sbor=input("Введите собаку которую хотите посмотреть 1 или 2:")
# if sbor=="1":
#     sbordog=input("Введите ключ который хотите посмотреть,если все, то введите n:")
#     if sbordog=='n':
#         print(dogs1)
#     else:
#         print(dogs1.get(sbordog, "Нет такого"))
#
# if sbor=="2":
#     sbordog = input("Введите ключ который хотите посмотреть,если все, то введите n:")
#     if sbordog == 'n':
#         print(dogs2)
#     else:
#         print(dogs2.get(sbordog, "Нет такого"))

# a=dogs1.get('age')
# b=dogs1.get('veskg')
# c=dogs1.get('rostsm')
# print(a+b+c)
#
# dict1={
#     '1':1,
#     '2':2,
#     '3':3
# }
# a=0
# for i in dict1.keys():
#     a+=i
# print(a)

# dict2 = {
#     1:1,
#     4:2,
#     3:3
# }

# print(dict2)
# print(dict2["key1"])
# print(dict2["key1"]+dict2["key2"]+dict2["key3"])

# s = 0
# for i in dict2.values():
#     s +=i #s = s + i
# print(s)
#
# s1 = 0
# s2 = 0
# for i in dict2.keys():
#     s1+=i
#     print(i)
#     s2+=i
# print(s1)
# print('=======')
# print(s1+s2)

# a=0
# b=0
#
# for k,v in dict2.items():
#     print(f'Ключ={k},Значение{v}')
#     a+=k
#     b+=v
# print(a)
# print(b)
# print(a+b)
#суммировать значения у которых ключи четные
#сумма ключей если нечетные значения
# dict2 ={
#     1:1,
#     4:2,
#     5:3,
#     7:5,
#     8:11,
#     9:3
# }
#
# # a=0
# #
# # for k,v in dict2.items():
# #     if k%2==0:
# #         a+=v
# # print(a)
#
# # a=0
# # for k,v in dict2.items():
# #     if v%2==1:
# #         a+=v
# # print(a)
#
# a=0
# for k,v in dict2.items():
#     print(k,v,sep="|")
#     if not v%2==0:
#         a+=v
# print(a)

# set1={1,'hi',2,3,True,'world'}
# print(set1) #вывод{1, 2, 3, 'hi', 'world'}

# set1={1,2,'boo',3,"hi"}
# print(set1)
# set1.add(42)
# set1.remove('hi')
# print(set1)
#
# list1=[1,2,'boo',3,"hi"]
# print(set(list1))
# list1.append(42)
# list1.remove('hi')
# print(set(list1))
#
# list2=[1,2,'boo',3,"hi"]
# set2=list2.copy()
# print(set(set2))
# list2.append(42)
# list2.remove('hi')
# print(set(list2))

# set5={4,5,6,7,89,10}
# set5.remove(89)
# set5.add(8)
# set5.add(9)
# print(set5)

# set1={0}
# for i in range (5):
#     a = input("Ввведите элемент:")
#     set1.add(a)
# set1.remove(0)
# print(set1)

#четные в список нечетв множества
# list1=[]
# set1={0}
# for i in range (5):
#     vvod=int(input('Введите числo:'))
#     if vvod%2==0:
#         list1.append(vvod)
#     elif vvod%2==1:
#         set1.add(vvod)
# set1.remove(0)
# print(list1)
# print(set1)
#
# list1=[i for i in range(5)]
# print(list1)
#
# tuple1=([i for i in range(5)])
# print(tuple1)

# str1= 'hello, world'
# for i in range(len(str1)):
#     print(str1[i],i)
#
# str1='lolkek 42'
# if str1.isalpha():
#     print('символы алфовитные')
#     if str1.isupper():
#         print('все символы в верхенем регистре')
# elif str1.isdigit():
#     print('символы это символы чисел')

# if str1.startswith('lolkek'):
#     print('da')
# else :
#     print('net')
#
# print(str1.upper())
# print(str1.lower())
# print(str1.capitalize())
#
# name=input('Введите ваше имя:')
#
# print(name.strip())
#кек42 лол52 птица мечеть яблочки

# получ от пользв предлож из 5 слов,в двух словах имеются числа,
# получ строку преобразов в список слов,
# слова где есть числа преоброзав в загла в тех где нет чисел тольк первые символы в заглав,
# после него собрать полученные слова в строку


# str_input = input('Вставьте сюда предложение из 5 слов (два из них должны иметь числа): ')
# words = str_input.split()
# print(words)
#
# result_words = []
# for word in words:
#     if any(gaw.isdigit() for gaw in word):
#         result_words.append(word.upper())
#     else:
#         result_words.append(word.capitalize())
#
# str_final = " ".join(result_words)
# print(str_final)


inp=input("Введите свои слова: ")
words=inp.split()
list1=[]
for word in words:
    if word.isalpha()==False:
        list1.append(word.upper())
    else:
        list1.append(word.title())
final=" ".join(list1)
print(final)
