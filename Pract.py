# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/Create")
# driver.maximize_window()
#
# year = "2023"
# month = "march"
# date = "30"
# driver.find_element(By.XPATH,"(//span[@class='k-select'])[1]").click()
# while True:
#     month = driver.find_element(By.XPATH,"")
#
# class Students():
#
#     def __init__(self,name,age,rollno):
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#
#     def talk(self):
#         print("Hello My name is",self.name)
#         print(" my age is",self.age)
#         print("my rollno is",self.rollno)
#
# obj = Students("chaitanya",27,12345)
# obj.talk()

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 49
#
#     def m1(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)

# t= Test()
# t.m1()
# del t.c
# # t.m1()
# print(t.__dict__)
# print(t.a,t.b)


# class Test:
#     a=10
#     def __init__(self):
#         Test.b =20
#
#     def m1(self):
#         Test.c = 30
#     @classmethod
#     def m2(cls):
#         cls.d1  = 40
#         Test.d2 = 50
#     @staticmethod
#     def m3():
#         Test.e = 50
#
#
#
# print(Test.__dict__)
# t = Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__)
# Test.m2()
# print(Test.__dict__)
# Test.m3()
# print(Test.__dict__)
# Test.f = 60
# print(Test.__dict__)




# class Test:
#     a = 666
#
#     @classmethod
#     def m1(cls):
#         cls.a = 777
#         # Test.a = 789
#
#     @ staticmethod
#     def m2():
#         Test.a = 888
#
# print(Test.a)
# Test.m1()
# print(Test.a)
# Test.m2()
# print(Test.a)



# class Test:
#     a= 10
#     def __init__(self):
#         Test.b = 20
#
#     @ classmethod
#     def m1(cls):
#         cls.a = 888
#         del cls.b
#
#
# t1 = Test()
# t2 = Test()
# t1.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# print(Test.a,Test.b)

# class Test:
#     a = 100
#     def __init__(self):
#         Test.b  = 200
#
#     def m1(self):
#         Test .c =300
#         del Test.b
#
#     @ classmethod
#     def m2(cls):
#         Test.d = 500
#         cls.e = 600
#
#     @ staticmethod
#     def m3():
#         Test.f = 700
#         # self.g = 800
# print(Test.a)
# t = Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__)
# t.m2()
# print(Test.__dict__)


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print("hi",self.name)
#         print("your marks is:",self.marks)
#     def grade(self):
#         if self.marks>=60:
#             print("you got First Grade")
#         elif self.marks>= 50:
#             print("you got the second grade")
#         elif self.marks>=35:
#             print("you got the pass")
#
#         else:
#             print("sorry you got failed")
#
#
# n = int(input("enter number of students:"))
# for i in range(n):
# #     name = input("enter name:")
#     marks = int(input("enter marks:"))
#     S=Student(name,marks)
#     S.display()
#     S.grade()
# print()

# class A:pass
# class B(A): pass
# class C(A): pass
# class D(B,C):pass
#
#
# print(A.mro())
# print(B.mro())
# print(C.mro())
# print(D.mro())

# *************Super Method*****************
# class Student:
#     def __init__(self,name,age):
# #         self.name = name
#         self.age = age
#     def display(self):
#         print('Name',self.name)
#         print('age is',self.age)
#
# class Person(Student ):
#
#     def __init__(self,name,age,rollno,marks):
#         super().__init__(name,age)
#         self.rollno = rollno
#         self.marks = marks
#
#     def display(self):
#         super().display()
#         print('Roll No is:',self.rollno)
#         print('Marks is:',self.marks)


# s = Person('Chaitanya Kumar',27,1234,89)
# s.display()


# class A:
#     def m1(self):
#         print('A Class Method')
# class B(A):
#     def m1(self):
#         print('B Class Method')
# class C(B):
#     def m1(self):
#         print('C class Method')
# class D(C):
#     def m1(self):
#         print('D classmethod')
# class E(D):
#     def m1(self):
#         A.m1(self)
#
# e = B()
# e.m1()


# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def __mul__(self, other):
#         return self.salary *other.days
#
# class Timesheet:
#     def __init__(self,name,days):
#         self.name = name
#         self.days = days
#
#
# e = Employee('chaitanya',567)
# t = Timesheet('chaitanya',30)
# print("this month salary is:",e*t)

# class Test:
#     def m1(self):
#         print("no-arg method")
#     def m1(self,a):
#         print("one_arg method")
#     def m1(self,a,b):
#         print("two_args method")
#
#
# t = Test()
# t.m1(1,2 )


# class Test:
#     def sum(self,a=None,b=None,c=None):
#         if a!= None and b!=None and c!=None:
#             print("the sum of 3 numbers is:",a+b+c)
#         elif a!= None and b!= None:
#             print("the sum of 2 numbers is:",a+b)
#         else:
#             print("please provide 2 or 3 arguments")
#
#
# t = Test()
# t.sum(10,20)
# t.sum(10)
# # t.sum(10,20,30,40)
# t.sum(10,20,30)
# t.sum(10,20,30,80)


# class Test:
#     def sum(self,*a):
#         total = 0
#         for x in a:
#             total= total +x
#         print("the sum is:",total)
#
#
# t = Test()
# t.sum(10,20,30)
# t.sum(10,20)
# t.sum(10,20,30,40)


# a = [10,20,30,40,50]
# a[1],a[-1]=a[-1],a[1]
# print(a)

# def func(a):
#     a[0], a[1] = a[1],a[0]
#     return a
#
#
# a=[10,20,30,40,50]
# print(func(a))



# [23, 65, 19, 90], pos1 = 1, pos2 = 3
# [19, 65, 23, 90]


# def func(a):
#     a[0], a[2] = a[2],a[0]
#     return a
#
#
# a=[23,65,19,90]
# print(func(a))
#



# import keyword
# k1 = keyword.kwlist
# # print(k1,end = " ")
# print(len(k1))


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
search_link = driver.find_element(By.XPATH,"//input[@name ='q']")
search_link.send_keys("mphasis")
search_link.submit()





































