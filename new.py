# print("hello")## syntax  

# a=50 
# b=100
# if a<b:
#     print("b is greater")
# else:
#     print("a is greater")

#     #global b
#     #b=5

#     '''
#     exp handling
#     oops
#     cl,obj,abs,enc,pol,inhe,
#     string opertions
    
#     '''
 



'''################# COLLLECTION DATA TYPES #####################'''



## LIST ##
# * LIST ITEMS ARE ORDERD
# * LIST ITEMS ARE CHANAGEBLE            MUTABLE
# * LIST ITEMS ALLOW DUPLICATES

## TUPLE ##
#* TUPLE ITEMS ARE ORDERD 
#* TUPLE ITEMS ARE NOT CHANGEBLE         IMMUTABLE
#* TUPLE ITEMS ARE ALLOW DUPLIACTES

## SETS ##
#* SETS ITEMS ARE UNRODERD
#* SET ITEMS ARE UNCHANGEBLE 
#* SET ITEM ARE NOT ALLOW DUPLICATES

## DICTIONARIES ##
#* DICT ITEMS ARE ORDERD
#* DICT ITEMS ARE CHANGEBLE
#* DICT ITEMS ARE NOT ALLOW DUPLICATES



###### LIST ########



# A = {'APPLE',2,2.2,True}
# print(A)
# # print(type(A))




# a = {
# 'brand':'casio',
#     'model':'gshok',
#     'year':2000,
# }
# print(a)
# print(type(a))


a=['apple','orange','pinapple','grape']
'''insert method'''
# a.insert(1,'banana')

# b=['banana','cherry']
# a.insert(0,b)

'''append method'''
# a.append('banana')

'''extent method'''
# b=['banana','cherry']
# a.extend(b)

# b=('banana','cherry')
# a.extend(b)

'''remove method'''
# a.remove('apple')

# a.pop(0)
# a.pop(-1)
# a.pop()
# del a[1]

'''clear method'''
# a.clear()

'''looping list'''
# for i in a:
# print(i)

###### string operation

# a="sebin"
# b='hello'

'''spiltinng with index'''

# print(a[0])
# print(a[1])
# print(a[4])

'''slice operator []'''
# print(a[0:])
# print(a[0:1])
# print(a[1:5])
# print(a[2:4])
# print(a[::2])
# print(a[:1])
# print(a[-1])
# print(a[-2:])
# print(a[-4:-1])
# print(a[::-1])

'''deleting'''
# del a
# print(a)

'''concatention'''
# print(a+b)

'''repetition'''
# print(a*4)

'''true/false'''
# print('w' in a)
# print('se' not in a)

''''''
# print("The string a : %s and b:%s" % (a,b))

'''backslash'''
# print("Python1 \
# Python2 \
# Python3")

'''backspace'''
# print("Hello  \bWorld")

'''new line'''
# print("hai \n hello")

'''tab'''
# print("Hello \t World!")


'''Python rstrip() method example'''
# a = "python and html#2468..."
# b = a.rstrip(".8642# ")
# print("Old string: ",a)
# print("New String: ",b)

'''Python split() method example'''
# str = "Java is a programming language"
# str2 = str.split(" ")
# print(str)
# print(str2)

'''Python lstrip() method example'''
# str =  "     python"
# str2 = str.lstrip()
# print(str)
# print(str2)


'''Tuple index() Method'''

# thistuple = (10, 30, 70, 80, 70, 50, 40, 60, 80, 50)
# x = thistuple.index(80)
# print(x)

'''tuple count() method'''

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7)
# x = thistuple.count(7)
# print(x)

'''multiply tuples'''

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)

'''Join Tuples'''

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

'''while loop'''

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

'''loop through index number'''

'''using len()'''
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])


# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

'''asterisk'''

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

'''remove items from tuple'''

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

'''addition'''

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

'''append'''

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

'''check if item exist'''

# thistuple = ("apple", "banana", "cherry")
# if "kiwi" in thistuple:
#  print("Yes, 'kiwi' is in the fruits tuple")

'''range of index'''

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-6:-1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

'''list'''

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)




######## set #########


#unorderd - unchangeble - duplicates not alllowed 

# fruits = {"apple", "banana", "cherry", "kiwi", "mango"}
# fruits.add('lemon')
# print(fruits)


# Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
# x = Days1.pop()
# print(x)
# print(Days1)
 

 ######################################################################################################################################


##  ccollection data types

# List- orderd-changeble-allow duplicates

# tuple - orderd - unchangeble - allow duplicates 

# set - unorderd - unchanageble - not allow duplictes

# dict - orderd - changeble - not allowed duplicates



### LIST ###


# def home(n):
#     print(abs(n -20))
# mylist = [10,40,30,50,20,60,80,90]
# mylist.sort(key=home)
# home(mylist)



# set 

# unchangeble
# duplicates allowed-2
# unorderd




# set1={1,2,3,4,5}
# print(set1)


###   dictionaries   ###


# ordered
# Changeble
# dupplictes not allowed

# child1 = {
#     'name':'emil',
#     'age':26
# }
# child2 = {
#     'name':'hari',
#     'age':36
# }
# myfamily = {
#     'child1':child1,
#     'child2':child2
# }

# print(myfamily)



'''nested dict'''
# mydict1 = {
#     "name" : "name1",
#     "age"  : "age1",
#     "year" : "year1"
# }
# mydict2 = {
#     "name" : "name2",
#     "age"  : "age2",
#     "year" : "year2"
# }
# mydict = {
#     "mydict1" : mydict1,
#     "mydict2" : mydict2
# }

# print(mydict)

'''copy'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

'''loop'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x,y in thisdict.items():
#      print(x,y)


# for x in thisdict.keys():
#     print(x)

# for x in thisdict.values():
#     print(x)

# for x in thisdict:
#     print(thisdict[x])

'''clear'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

'''del'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict)

# del thisdict['model']
# print(thisdict)

'''pop'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# thisdict.pop("model")
# print(thisdict)



'''update'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color" : "red"})
# print(thisdict)

'''add'''

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# def hello():
#     print("hello hai")

# hello()    

# def product():
#     a = 12
#     b = 16
#     c = a*b
#     return c
# print(product())

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily)

'''function'''

# def sum():
#     a = 10
#     b = 20
#     c = a + b
#     return c
# print("The sum is:",sum())





############## FUCNTIONS #############



# def home(**name):
#     print('my name is ',name['fname'])
# home(fname='sebin',lname='aiegil',tname='risnan')


# def home(**name):
#     print('my name is ',name['tname'])
# home('sebin','aiegil','risnan')



# name = {
#     'fname':'sebin',
#     'lname':'rinsan'
# }

# a = name['fname']
# print(a)


# num = -80
# print(abs(num))

# x = 1
# y = bin(x)
# print(y)

# s = sum([1,2,4])
# print(s)

# print(float(4))

#d -"integer"
#f - "float"
#b - "binary"
# print(format(12, "d")) 

# list = [1,2,3,4,5]
# listIter = iter(list)
# print(next(listIter))
# print(next(listIter))
# print(next(listIter))

# obj = int()
# print(type(obj))
# print(dir(obj))

# a = complex(5,7)
# b = complex(1,2)
# print(a)
# print(b)

# att = dir()
# print(att)

# result = divmod(10,3)
# print(result)


# result2 = dict(a=1,b=2)
# print(result2)

# result = hash(21)
# result2 = (hash(22.2))
# print(result)
# print(result2)

# s = min(5,6,8,1,23,4,6,41,23,)
# print(s)

# result2 = set('12')
# result3 = set('datascience')
# print(result2)
# print(result3)

# result = hex(1)
# result2 = hex(342)
# print(result)
# print(result2)

# val = id("python")
# print(val)
# val1 = id(548)
# print(val1)
# val3 = id([25,336,95,236,92,3225])
# print(val3)

# str = "pythonpoint"
# sorted1 = sorted(str)
# print(sorted1)

# val =  oct(7)
# print(val)

# print(pow(2,3))

# print(list(range(2,9)))

# Tuple = ('J', 'a', 'v', 'a')
# print(list(reversed(Tuple)))
# lst = (list(range(2,9)))
# print(list(reversed(lst)))

# print(round(10.6))

# s1 = "hai"
# s = s1 + ","+str(25)
# print(s)

# t1 = tuple()
# print('t1=', t1)
# t2 = tuple([1, 6, 9])
# print('t2=', t2)

# x = lambda a : a + 10
# print(x(5))
# y = lambda a,b : a * b
# print(y(4,5))

# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))

# def displayMsg(name):
#     print("Hi " +name)
# def show():
#     print("show here")

# import new
# name = input("Enter Name: ")
# new.displayMsg(name)
# new.show()

# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%c"))

# import math
# x = math.pow(5,2)
# print(x)
# y = math.floor(10.26895458)
# print(y)
# r = math.ceil(5.47963258)
# print(r)
# g = math.factorial(2)
# print(g)
# h = math.modf(85.6)
# print(h)
# e = math.sqrt(225)
# print(e)
# pi = math.pi
# print(pi)
# re = math.fmod(20,3)
# print(re)
# fs = math.fsum([1,5,8,9,7,2])
# print(fs)
# u = math.gcd(3,6)
# print(u)
# i = math.isinf(math.inf)
# print(i)
# b = math.isnan(78)
# print(b)

# import random
# lst = [1,2,5,8,9]
# random.shuffle(lst)
# print(lst)

# import statistics
# lst = [1,2,3,4,5,6,7,8,9]
# x = statistics.mean(lst)
# print(x)
# y = statistics.median(lst)
# print(y)
# z = statistics.mode(lst)
# print(z)
# a = statistics.stdev(lst)
# print(a)
# b = statistics.median_low(lst)
# print(b)
# c = statistics.median_high(lst)
# print(c)

# import json
# x = '{"name":"John", "Age":30,"city":"New york"}'
# y = json.loads(x)
# print(y)
# print(y["name"])

# import json
# x = {
#     "name":"john",
#     "age":30,
#     "city":"new york"
# }
# y = json.dumps(x)
# print(y)

# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))

# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x, indent=4,sort_keys=True, separators=(".","=")))

# try:
#     a = 5
#     b = 0
#     c = a/b
#     print("result:",c)
#     print("hi..")
# except Exception as e1:
#     print("Can't divide with zero")
#     a = 5
#     b = 0
#     c = a/b
#     print("result:",c)
# except:
#     print("Can't divide with zero")

# print("outside exception")



# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     c = a/b
#     print("a/b = %d"%c)
#     # multiple exception
# except(ArithmeticError, IOError):
#     print("Arithmetic Exception")
# else:
#     print("Successfully Done")

# print("outside exception")

# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     c = a/b
#     print("a/b = %d"%c)
# except Exception as e:
#     print("can't divide by zero")
#     print(e)
# else:
#     print("Hi I am else block")
# finally:
#     print("inside finally")

# print("outside exception")

# try:
#     age = int(input("Enter the age:"))
#     if(age<18):
#         raise ValueError("enttu poda")
#     else:
#         print("the age is valid")
# except Exception as e:
#     print(e)
# print("outside exception")

# try:
#     a = int(input("Enter a"))
#     b = int(input("Enter b"))
#     if b == 0:
#         raise ArithmeticError("Division by zero")
#     else:
#         print("a/b =",a/b)
# except ArithmeticError as e:
#     print("the value of b can't be 0")
#     print("Error:",e)        

# f = open(r"C:\Users\sebin\OneDrive\Desktop\myfile.txt")
# content = f.readline()
# content1 = f.readline()
# print(content)
# print(content1)
# f.close()

# f = open(r"C:\Users\sebin\OneDrive\Desktop\myfile.txt", 'a+')
# print("The filepointer is at byte:",f.tell())
# content = f.read()
# print("After reading, the f is at:",f.tell())

# f = open(r"C:\Users\sebin\OneDrive\Desktop\myfile.txt")
# print("The filepointer is at byte:",f.tell())
# f.seek(10)
# print("After reading, the f is at:",f.tell())

# import os
# os.rename(r"C:\Users\sebin\OneDrive\Desktop\myfile.txt", r"C:\Users\sebin\OneDrive\Desktop\file.txt")
# print("rename")

# f = open(r"C:\Users\sebin\OneDrive\Desktop\myfile.txt",'x')
# print(f)

# import os
# os.remove(r"C:\Users\sebin\OneDrive\Desktop\myfile.txt")
# print("file removed")

# import os
# os.mkdir(r"C:\Users\sebin\OneDrive\Desktop\hello")
# print('folder created')

# import os
# print(os.getcwd())
# print("current directory")

# import os
# print("current working directory")
# print(os.getcwd())
# os.chdir(r"C:\Users\sebin\OneDrive\Desktop\hello")
# print(os.getcwd())

# import os
# os.rmdir(r"C:\Users\sebin\OneDrive\Desktop\hello")
# print('folder removed')

# import re
# txt = "The rain in spain"
# x = re.findall("in", txt)
# print(x)

# import re 
# txt  = "the rain in spain"
# x = re.search("\s",txt)
# print(x.start())

# import re
# txt  = "the rain in spain"
# x = re.split("\s", txt)
# print(x)

# import re 
# txt = "the rain in spain"
# x = re.sub("\s","0",txt)
# print(x)

# import re
# txt = "the rain in spain"
# x = re.findall("[a-m]",txt)
# print(x)

# import re 
# txt = "hello world"
# x =  re.findall("he..o",txt)
# print(x)

# import re
# txt = "hello planet"
# x = re.findall("^hello",txt)
# if x:
#     print("yes")
# else:
#     print("no")    

# import re 
# txt = "hello planet"
# x  = re.findall("planet$",txt)
# if x:
#     print("yes")
# else:
#     print("no") 

# import re
# txt = "hello planet"
# x = re.findall("he.*o",txt)
# print(x)

# import re
# txt = "hello planet"
# x = re.findall("he.+o", txt)
# print(x)

# import re 
# txt = "hello planet"
# x = re.findall("he.?o",txt)
# print(x)

# import re
# txt = "hello planet"
# x = re.findall("he.{2}o",txt)
# print(x)

# import re
# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("falls|stays",txt)
# print(x)
# if x:
#     print("yes")
# else:
#     print("no")

# import re
# txt = "the rain in spain"
# x = re.findall("[arn]",txt)
# print(x)

# import re
# txt = "the rain in spain"
# x = re.findall("[a-n]",txt)
# print(x)

# import re
# txt = "the rain in spain"
# x = re.findall("[^arn]",txt)
# print(x)

# import re
# txt =  "the2 rain in spain1"
# x = re.findall("[0123]",txt)
# print(x)

# import re 
# txt = "8 times before 11:45 AM"
# x = re.findall("[0-9]",txt)
# print(x)

# import re 
# txt = "8 times before 11:45 AM"
# x = re.findall("[0-5][0-9]",txt)
# print(x)

# import re
# txt = "8 times before 11:45 AM"
# x  = re.findall("[a-zA-Z]",txt)
# print(x)

# f  = open(r"C:\Users\sebin\OneDrive\Desktop\myfile.txt","a")
# f.write("hai hello")
# f.close()

# parameterized cunstructor
# non-parameterized cunstructor

# class parent:
#     a = 10
#     name = "jhon"
#     def display(self):
#         print(self.a,self.name)
# d = parent()
# d.display()


# class parent:
#     def __init__(self,name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id


#     def disp(self):
#         print(self.name,self.age,self.id)

# s = parent("jhon",23,101)
# # print(getattr(s,"id"))
# # setattr(s,"id",201)
# delattr(s,"id")
# # print(getattr(s,"id"))

# s.disp()

# class Student:
#     "A class about students and their addresses"
#     def __init__(self,name,id,age):
#         self.name = name
#         self.id = id
#         self.age = age
#     def display_details(self):
#         print(self.name,self.id,self.age)
# s = Student("John",101,22)
# print("Doc:",s.__doc__)
# print("Dict:",s.__dict__)
# print("Module:",s.__module__)
# print("Name:",Student.__name__)
# print("Base:",Student.__bases__)

# INHERITANCE 


# class Animal:
#     def speak(self):
#         print("Animal Speaking")


# class Dog:
#     def bark(self):
#         print("dog barking")


# class Childdog(Dog,Animal):
#     def eat(self):
#         print("dog eating")
# d = Childdog()
# print(isinstance(d,Animal))


# class Bank:
#     def getroi(self):
#         return 10
# class SBI(Bank):
#     def getroi(self):
#         return 7

# class ICICI(Bank):
#     def getroi(self):
#         return 8
# b1 = Bank()
# b2 = SBI()
# b3 = ICICI()
# print("Bank Rate of interest:",b1.getroi())
# print("SBI Rate of interest:",b2.getroi())
# print("ICICI Rate of interest:",b3.getroi())


