'''coverting height in cm to feet'''
# num=int(input("Enter height in CM:"))
# num1=num/30.48
# print(num1,"feet")

'''temperature in celsius to fahrenheit'''
# num=int(input("Enter temperture in Clecius:"))
# num1=num*(9/5)+32
# print(num1)

'''calculate simple interest'''
# num1=int(input("Enter pricipal amount:"))
# num2=int(input("Enter Annual Interest rate:"))
# num3=int(input("Enter time(in years):"))
# num4=num1*(1+num2*num3)/100
# print(num4)

'''exchanging values using temp varibles'''
# num1=int(input("Enter a first number:"))
# num2=int(input("Enter a second number:"))
# print("first number is",num2)
# print("second number is",num1)


'''exchanging values using temp varibles'''
# a = 2
# b = 4
# temp = 2
# a = b
# b = temp
# print(a)
# print(b)

'''calcutation using a mathematical expression'''
# n=int(input("Enter a number:"))
# num=n+n*n+n*n*n
# print(num)

'''to find quotient and remainder'''
# num1=int(input("Enter a Dividend:"))
# num2=int(input("Enter a Divisor"))
# num3=num1/num2
# num4=num1%num2
# print("Quotient",num3)
# print("Remainder",num4)

'''replace all occurrence of "a" with "$" in a string'''

# str = ("alphabet")
# str1 = str.replace("a","$")
# print(str1)

'''remove nth index character from a non-empty string'''

# str = "sebin"
# n = -1
# str1 = str[0:n]
# print(str1)



'''anagram'''
# str = "listen"
# str1 = "silent"
# if (sorted(str)==sorted(str1)):
#     print("ith anagram ahnn")
# else:
#     print("ith anagram alla")

'''exchange character in string nythop'''
# str = "python"
# str1 = str[0]
# n = str[-1]
# m = str[1:-1]
# print(n+m+str1)

'''vowels in a string'''
# str = "aaaaeeiiiooouuu"
# a = str.count("a")
# e = str.count("e")
# i = str.count("i")
# o = str.count("o")
# u = str.count("u")
# print(a+e+i+o+u)

'''replace blank space with hyphen'''

# str = ("alp habe t")
# str1 = str.replace(" ","-")
# print(str1)

'''length of the string'''

# str = "malayalam"
# print(len(str))

# str = "python"
# x = str.index("n")
# print(x+1)

'''to remove character of odd index value'''

# str = "python"
# for x in range(len(str)):
#     if x % 2 == 0:
#         print(str[x])

'''calculate number of words and character in a string'''

# str = "hai hello python malayalam"
# x = str.count(" ")
# y = len(str)
# print("number of words is",x+1)
# print("number of character is",y-x)

'''to display largest string'''
# str = "malayalam"
# str1 = "python"
# if len(str)>len(str1):
#     print(str,"is the largest string")
# else:
#     print(str1,"is the largest string")

'''to count lowercase in the string'''

# str = "MalAYalam"
# x = [char for char in str if char.islower()]
# print(len(x))

'''palindrome'''

# str = "malayalam"
# if str[::-1] == str[0::]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

'''claculate the number of uppercase and lowercase'''

# str = "MalAYalam"
# x = [q for q in str if q.islower()]
# y = [m for m in str if m.isupper()]
# print("number od uppercase character is",len(x))
# print("number of lowercase character is",len(y))

'''pangram'''

# str = "python30"
# x = str.isalpha()
# print(x)

'''hypenated word ordered alphabetically'''

# y = input(("enter a sentence:"))
# str = [x for x in y.split("-")]
# str.sort()
# print('-'.join(str))

'''calculate number of digit and letters'''

# str = input(("enter a string:"))
# x = [q for q in str if q.isalpha()]
# y = [m for m in str if m.isdigit()]
# print("number of character is",len(x))
# print("number of digit is",len(y))

''' First 2 and Last 2 characters to a new string'''

# str = input(("enter a string:"))
# m = str[0:2]
# n = str[-2:]
# print(m+n)

''' Count the Occurrences of word'''

# str = input(("enter a sentence:"))
# x = input(("enter the word:")) 
# n = str.count(x)
# print(n)

'''to check substring'''

# str = input("enter the string:")
# x = input("enter the substring:")
# if str.find(x):
#     print("substring is present")
# else:
#     print("substring is not present")

'''to  reverse a given number'''

# str = input("enter three digit value :")
# print(str[::-1])

'''divisible by a given number'''

# n = int(input("Enter number:"))
# m = int(input("Enter number:"))
# d = int(input("Enter the number that should be divided by:"))
# for i in range(n,m+1):
#    if(i%d==0):
#       print(i)

'''odd nummber in a given range'''

# n = int(input("Enter number:"))
# m = int(input("Enter number:"))
# for i in range(n,m):
#     if(i%2!=0):
#         print(i)

'''sum of digit n a number'''

# num = int(input("Enter a number:"))
# sum = 0
# for i in str(num):
#     sum=sum+int(i)
# print(sum)

'''smallest divisor of an integer'''

# num = int(input("Enter a number:"))
# a=[]
# for i in range(2,num):
#     if(num % i == 0):
#         a.append(i)
# print("smallest divisor of",num ,"is",a[0])

'''count number of digit in a number'''

# num = int(input("Enter a number:"))
# a=[]
# for i in str(num):
#  a.append(i)
# print(len(a))

'''to check a number is palindrome'''

# str = (input("enter a number:"))
# if str[::-1] == str[0::]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

'''integer that aren't divisible 2 and 3 '''

# for i in range(0,50):
#     if (i%2!=0) and (i%3!=0):
#         print(i)

'''n and print 1+2+...+n'''

# n = int(input("enter a number"))
# a=[]
# for i in range(1,n+1):
#     a.append(i)
#     s = str(a)
#     s = ' +'.join(x for x in s.split(",")) 
# print(a)

'''summation pattern'''

# n = int(input("enter a number"))
# a=[]
# for i in range(1,n+1):
#     a.append(i)
#     s = str(a)
#     s = ' +'.join(x for x in s.split(","))
#     print(s,"=",sum(a))

'''identity matrix'''

# n = int(input("enter the size of the matrix:"))
# for m in range(0,n):
#     for x in range(0,n):
#      if(m == x):
#       print("1 ",end=" ")
#      else:
#        print("0 ",end=" ")
#     print()

'''prime factor of an integer'''

# n = int(input("Enter the number"))
# for i in range(2,n + 1):
#     if n % i == 0:
#         count = 1
#         for x in range(2,(i//2 + 1)):
#             if(i % x == 0):
#                 count = 0
#                 break
#         if(count == 1):
#             print(i)

'''divisor of an integer'''

# num = int(input("Enter a number:"))
# a=[]
# for i in range(2,num):
#     if(num % i == 0):
#         a.append(i)
# print(" divisor of",num ,"is",a)

'''divisible by 7 and multiple of 5'''

# for i in range(1,1000):
#     if(i % 7 == 0) and (i % 5 == 0):
#        print(i)

'''lcm of 2 numbers'''

# num1 = int(input("enter a number:"))
# num2 = int(input("enter second number:"))
# for i in range(max(num1, num2), 1 + (num1 * num2)):
#     if (i % num1 == 0) and (i % num2 == 0):
#         lcm = i
#         break
# print("LCM of", num1, "and", num2, "is", lcm)

'''gcd of 2 numbers'''

# num1 = int(input("enter a number:"))
# num2 = int(input("enter second number:"))
# while num1 != num2:
#     if num1 > num2:
#         num1 -= num2
#     else:
#         num2 -= num1
# print("GCD is" ,num1)
    

'''to check prime number'''

# num = int(input("enter a number:  "))
# for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
# else:
#        print(num,"is a prime number")


'''sum of n natural numbers'''

# n = int(input("enter a number: "))
# a=[]
# for i in range(1,n+1):
#     a.append(i)
# print(sum(a))

'''sum of series'''

# n=int(input("Enter the number : "))
# s=0
# for i in range(1,n+1):
#     s=s+(1/i)
# print(round(s,2))



'''prime number of given range'''

# n = int(input("Enter range: "))
# a=[]
# for num in range(2, n + 1):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             a.append(num)
# print(a)

'''star pattern'''

# n = int(input("enter the size of the matrix:"))
# for m in range(0,n):
#     for x in range(0,n):
#      if(m == x):
#       print(" ",end=" ")
#      else:
#        print("* ",end=" ")
#     print()


'''calculate average of a give list of number'''

# n = (1,2,3,4)
# x = sum(n)
# y = len(n)
# print(x/y)

'''largest even number and largest odd number'''

# n = [int(i) for i in input('enter a value :').split(',')]
# a = []
# b = []
# for x in range(len(n)):
#     if n[x] % 2 == 0:
#         a.append(n[x])
#         a.sort()
# print(a[-1],"is the largest even number...")
# for x in range(len(n)):
#     if n[x] % 2 != 0:
#         b.append(n[x])
#         b.sort()
# print(b[-1],"is the largest odd number")        

'''number occur in a list'''

# n = [1,2,9,4,5,6,10,8,9,7]
# x = int(input("Enter a value: "))
# m = n.count(x)
# print(m)

'''largest number in list'''

# n = [1,2,9,4,5,6,10,8,9,7]
# a = []
# for x in range(len(n)):
#     a.append(n[x])
# a.sort()
# print(a[-1],"is the largest number")

'''second largest number '''

# n = [1,2,9,4,5,6,10,8,9,7]
# a = []
# for x in range(len(n)):
#     a.append(n[x])
# a.sort()
# print(a[-2],"is the second largest number")
        

'''even and odd number to different list'''

# n = [int(i) for i in input('enter a value :').split(',')]
# a = []
# b = []
# for x in range(len(n)):
#     if n[x] % 2 == 0:
#         a.append(n[x])
#         a.sort()
# print(a,"is  even number...")
# for x in range(len(n)):
#     if n[x] % 2 != 0:
#         b.append(n[x])
#         b.sort()
# print(b,"is odd number") 

'''merge two list and sort''' 

# n = [int(i) for i in input('enter a value :').split(',')]
# a = []
# b = []
# for x in range(len(n)):
#     if n[x] % 2 == 0:
#         a.append(n[x])
# print(a)
# for x in range(len(n)):
#     if n[x] % 2 != 0:
#         b.append(n[x])
#         a.append(n[x])
# print(b)
# a.sort()        
# print(a)

'''second element to another list'''

# n = [1,7,9,4,5,6,10,8,9,7,2]
# m = len(n)
# a = []
# for x in range(1,m,2):
#  if x % 2 != 0:
#   a.append(n[x])
# print(a)  

'''sort according to length of element'''

# n = [1,7,97,4,548,6,10,8,9,7,23]
# n.sort()
# m = len(n)
# a = []
# b = []
# c = []
# d = []
# for x in range(0,m):
#     i = len(str(n[x]))
#     a.append(i)  
# k = a.index(2)
# l = a.index(3)
# b = list(n[0:k])
# c = list(n[k:l])
# d = list(n[l::])
# print(b)
# print(c)
# print(d)

'''Union of two Lists'''

# n = [1,3,5,7,9,]
# m = [2,4,6,8]
# print(n + m)

'''Intersection of Two Lists'''

# n = {1,3,5,7,9,}
# m = {1,2,3,4,6,8}
# k = (m.intersection(n))
# print(k)

'''First Element as the Number and Second Element as the Square of the Number'''

# a = [(x,x**2) for x in range(2,10+1)]
# print(a)


'''Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements From The Original List'''

# l = [1,2,3,4,5,6,7,8,9,10]
# nl = []
# k = 0
# for i in range(0,len(l)):
#     # print(i)
#     k+=l[i]
#     nl.append(k)
# print(nl)


'''Generate Random Numbers from 1 to 20 and Append Them to the List'''

# import random
# n = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# random_number = random.choice(n)
# print(random_number)

'''Swap the First and Last Value of a List'''

# n = [1,3,5,7,9]
# m = [2,4,6,8]#
# print("first original list is",n)
# print("second original list is",m)
# p = -1
# p1 = 0
# n[p1] ,  m[p1] = m[p1] , n[p1]
# n[p] ,  m[p] = m[p] , n[p]
# print("list after swapping is",n)
# print("list after swapping is",m)

''' Remove the Duplicate Items from a List'''

# n = [1,3,5,7,9,8]
# m = [1,2,4,6,8]
# a = n + m
# a.sort()
# x = [*set(a)]
# print(x)

'''Read a List of Words and Return the Length of the Longest One'''

# n = ['apple','ball','cat','dog','elephant','fox']
# a = []
# x = len(n)
# for i in range(0,x):
#     m = len(n[i])
#     a.append(m)
# k = (max(a))
# j = (a.index(k))
# print('longest word is',n[j])
# print('length of the word is',k)

'''Remove the ith Occurrence of the Given Word in a List where Words can Repeat'''

# n = ['apple','ball','fox','cat','dog','elephant','fox']
# x = [*set(n)]
# a = list(x)
# print(a)


'''Capitalize'''

# n = input("Enter a sentence: ")
# m = n.upper()
# print(m)


'''sort sentence'''

# n = [str(i) for i in input('enter a sentence :').split(' ')]
# n.sort()
# print(' '.join(n))

'''to calculate letter and digits'''

# alpha, n = 0 , "hello123456789"
# for i in n:
#     if(i.isalpha()):
#         alpha += 1
# print("Letter",alpha)
# print("Digit",len(n)-alpha)

'''select odd numbers '''

# n = [int(i) for i in input('enter a value :').split(',')]   
# n.sort()
# for x in range(len(n)):
#     if n[x] % 2 != 0:
#      print(' '.join(n)) 

'''Remove All Tuples in a List of Tuples with the USN Outside the Given Range'''

'''Second Largest Number in a List Using Bubble Sort'''

'''Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10'''

'''Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements From The Original List'''


'''add a key-value pair to dict'''

# thisdict = {
#     "brand" : "asus",
#     "model" : "tuf",
#     "year"  : 2022,
#     }
# x = thisdict["color"] = "black"
# print(thisdict)

'''concatenate 2 dict into one'''

# laptop = {
#     "laptop1" : {
#       "brand" : "asus",
#       "model" : "tuf",
#       "year"  : 2022,
#     },
# "laptop2" : {
#   "brand" : "hp",
#   "model" : "dv4",
#   "year"  : 2014,
# }   
# }
# print(laptop)

'''to check a key exists in a dict'''

# thisdict = {
#     "brand" : "asus",
#     "model" : "tuf",
#     "year"  : 2022,
#     }
# for x in thisdict.keys():
#     if "color " == x:
#      print("Color is present in this dict...")
# else:
#  print("Color is not present in this dict...")

'''numbers in the form of (x,x*x)'''

# n = int(input("Enter the upperlimit:  "))
# a = {}
# for x in range(1,n+1):
#     a[x] = x*x
# print(a)

'''to remove a given key'''

# thisdict = {
#     "brand" : "asus",
#     "model" : "tuf",
#     "year"  : 2022,
#     }
# thisdict.pop("model")
# print(thisdict)

'''list into dict'''

# a = ['brand','model','year']
# b = ['asus','tuf',"2022"]
# mydict = {}
# for x in a:
#  for y in b:
#   mydict[x]=y
#   break
#  b.remove(y)
# print(mydict)

'''key fisrt char and value word'''

# a = []
# b = []
# mydict = {}
# n = "hello world"
# i = n.split()
# for x in i:
#  a.append(x)
#  b.append(x[0])   
# for x in a:
#  for y in b:
#   print(y)
#   mydict[y]=x
#   break
#  b.remove(y)
# print(mydict)
   
'''sum in a dict'''   

# mydict = {
# "a" : 10,
# "b" : 20,
# "c" : 30
# }
# x = mydict.values()
# print(sum(x))

'''multiply in a dict'''

# mydict = {
# "a" : 1,
# "b" : 2,
# "c" : 3
# }
# a = 1
# for i in mydict:
#     a = a*mydict[i]
# print(a)

'''Count the Frequency of Words Appearing in a String Using a Dictionary'''

# str = input("Enter the string :")
# lst=[]
# lst=str.split()
# cnt=[lst.count(i) for i in lst]
# print(dict(zip(lst,cnt)))



'''Form a Dictionary from an Object of a Class'''


# class obj(object):
#    def __init__(self):
#       self.A = 32
#       self.B = 60
#       self.C = 90
# inst = obj()
# print(inst.__dict__)


'''calculate area and perimeter of a rectangle'''

# def rectangle(num1,num2):
#     area =  num1 * num2 
#     perimeter =  2 * num1 + 2 * num2
#     print("Area of the rectangle is",area)
#     print("Perimeter of the rectangle is",perimeter )
# num1 =  int(input("Enter the length of the Rectangle:"))
# num2 = int(input("Enter the  width of the reactangle:"))
# rectangle(num1,num2)

'''calculate area and circumference of a circle'''


# def circle(num):
#     area = 3.14159265359 * (num * num)
#     circumference = 2 * ( 3.14159265359 * num)
#     print("area of the circle is",area)
#     print("circumference of the circle is",circumference)
# num = float(input("Enter the radius of the circle:"))
# circle(num)    

''' even or not'''


# def even(num):
#     if num % 2 == 0 :
#         print(num,"is a even number") 
#     else:
#         print(num,"is not a even number")
# num =  int(input("Enter a number: "))  
# even(num)       

'''prime number or not'''

# def prime(num):
#     for i in range(2,num):
#           if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#     else:
#         print(num,"is a prime number")
# num = int(input("enter a number:  "))
# prime(num)

'''average'''

# def aver():
#     a = int(input("enter a number:  "))
#     b = int(input("enter a number:  "))
#     c = int(input("enter a number:  "))
#     d = (a + b + c)
#     return d
# print(aver())


'''even number'''

# i = 0
# for i in range(4,31):
#     if i % 2 == 0:
#         print(i)


'''largest item from a given list'''

# lst = [2,7,8,23,65,12 ]
# lst.sort()
# print(lst[-1])


'''power of number raised to another'''

# import math
# def power(n,p):
#     a = math.pow(n,p)
#     return a
# n = int(input("Enter a number:"))
# p = int(input("Enter the power:"))
# print(power(n,p))

'''varible length of the argument'''


# def sum(**s):
#     print("my name is ",s['fname'])
# sum(fname='jhon',lname='tom')


'''Return multiple values from the function'''

# def sum(*s):
#     n = 0
#     for i in s:
#         n = n + i
#     return n
# print(sum(10, 20))
# print(sum(50,60))  


'''default argument '''

# def add_numbers( a = 7,  b = 8):
#     sum = a + b
#     print( sum)
# add_numbers()
# add_numbers(a = 2)
# add_numbers(2, 3)

'''area of a circle using a circle'''

# class circle():
#     def __init__(self,r):
#         self.radius = r

#     def  area(self):
#         return self.radius**2*3.14
# NewCircle = circle(1)
# print(NewCircle.area()) 

'''operation a list using list'''   

# class list():
#     def __init__(self):
#         self.n = []
#     def add(self,a):
#         self.n.append(a)
#     def remove(self,a):
#         self.n.remove(a)
#     def dis(self):
#         return(self.n)
# obj=list()
# print("Enter your choice number\n1.Add\n2.Delete\n3.Display")
# choice=1
# while(choice==1 or choice==2 or choice==3):
#  choice=int(input("Enter your Choice number:"))
#  if(choice==1):
#    n=int(input("Enter the number to append:"))
#    obj.add(n)
#    print("List:",obj.dis())
#  elif(choice==2):
#    n=int(input("Enter the value to delete:"))
#    obj.remove(n)
#    print("List:",obj.dis())
#  elif(choice==3):
#    print("List:",obj.dis())

#  else:
#   print("Invalid value!!!")

'''area of rectangle'''

# class reactangle():
#     def __init__(self, l, b):
#         self.length = l
#         self.breath = b

#     def area(self):
#         return self.length*self.breath
# Newrectangle = reactangle(2,6)  
# print(Newrectangle.area())      

'''area and perimeter of a circle '''

# class circle():
#     def __init__(self,r):
#         self.radius = r

#     def  area(self):
#         return self.radius**2*3.14
#     def perimeter(self):
#         return self.radius*6.28
# NewCircle = circle(2)
# print(NewCircle.area()) 
# print(NewCircle.perimeter())

'''calculator'''

# class calculator():
#     def __init__(self, num1, num2):
#          self.num1 = num1
#          self.num2 = num2 
#     def add(self):
#         return self.num1 + self.num2
#     def subtract(self):
#         return self.num1 - self.num2
#     def multiply(self):
#         return self.num1 * self.num2
#     def divide(self):
#         return self.num1 / self.num2 
    
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))  
# obj = calculator(num1,num2)
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# choice = 1
# while(choice==1 or choice==2 or choice==3 or choice==4):
#  choice=int(input("Enter your Choice number:"))
#  if(choice==1):
#    print(num1, "+", num2, "=",obj.add())
#  elif(choice==2):
#      print(num1, "-", num2, "=",obj.subtract())
#  elif(choice==3):
#      print(num1, "*", num2, "=",obj.multiply())
#  elif(choice==4):
#      print(num1, "/", num2, "=",obj.divide())
# else:
#         print("Invalid Input")

'''string accepts and print '''

# class str():
#     def __init__(self):
#         self.str1 = ""
#     def accept(self):
#         self.str1 = input("Enter a string: ")
#     def prin(self):
#         print(self.str1)
# inst = str()
# inst.accept()
# inst.prin()             

'''clecius to fahrenheit'''

# class converter():
#     def __init__(self):
#         self.cel = ""
#     def acc(self):
#         self.cel = int(input("Enter temperture in Clecius:"))
#     def pri(self):
#         print(self.cel*(9/5)+32)
# inst = converter()
# inst.acc()
# inst.pri()              

'''person'''

# class person():
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

# p1 = person("sebin",21)        
# print(p1.name,p1.age)

'''odd number between two point'''

# class odd():
#     def __init__(self):
#         self.start = ""
#         self.end = ""
#     def accept(self):
#         self.start = int(input("Enter the starting point:"))
#         self.end = int(input("Enter the end point:"))
#     def print(self):      
#         for i in range(self.start,self.end):
#             if(i%2!=0):
#                 print(i)

# obj = odd()
# obj.accept()
# obj.print()

'''even number betwween two point'''

# class even():
#     def __init__(self):
#         self.start = ""
#         self.end = ""
#     def accept(self):
#         self.start = int(input("Enter the starting point:"))
#         self.end = int(input("Enter the end point:"))
#     def print(self):      
#         for i in range(self.start,self.end):
#             if(i%2==0):
#                 print(i)
# obj = even()
# obj.accept()
# obj.print()

'''palindrome '''

# class palindrome():
#     def __init__(self):
#         self.str1 = ""
#     def accept(self):
#         self.str1 = str(input("Enter a sentence:"))
#     def print(self):
#         if self.str1[::-1] == self.str1[0::]:
#             print("string is palindrome")
#         else:
#             print("string is not palindrome")

# obj = palindrome()
# obj.accept()
# obj.print()

'''prime number'''

# class prime():
#     def __init__(self):
#         self.start = []
#         self.end = []
#         self.result = []
#     def accept(self):
#         self.start = int(input("Enter start point:"))
#         self.end = int(input("Enter end point:"))
#     def print(self):
#         for num in range(self.start, self.end + 1):
#             for i in range(2, num):
#              if (num % i) == 0:
#                     break
#             else:
#                     self.result.append(num)
#         print(self.result)
# obj = prime()
# obj.accept()
# obj.print()

