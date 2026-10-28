# polymorphism means method overriding .when a child class provides its own implementation of a method which exits in its parent class .the child object replace the parent class version when it called the child object.
# class Shapes:
#    def area(self):
#        return 0
#    def describe(self):
#        return f"shape with area: {self.area():.2f}"
# class Circle(Shapes):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*self.r**2
# class Rectangle(Shapes):
#     def __init__(self,w,h):
#         self.w=w
#         self.h=h
#     def area(self):
#         return self.w*self.h
# class Triangle(Shapes):
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h
#     def area(self):
#         return 0.5*self.b*self.h
# shapes=[Circle(7),Rectangle(2,4),Triangle(4,6)]
# for i in shapes:
#     print(i.describe())

# Duck typing
# it execute same as polymorphism but without using inheritencs concept.

# class Dog:
#     def speak(self):
#         return 'Woof!'
#     def move(self):
#         return "dog running"
# class Cat:
#     def speak(self):
#         return 'meow!'
#     def move(self):
#         return 'cat slinks'
# class Robot:
#     def speak(self):
#         return 'beep beep'
#     def move(self):
#         return 'robot wheel'
# def make_it_act(thing):
#     print(thing.speak())
#     print(thing.move())
# for obj in [Dog(),Cat(),Robot()]:
#     make_it_act(obj)

# class Payment:
#     def __init__(self,balance):
#         self.balance=balance
#     def process(self,amount):
#         print("Processing payment Rs.",amount)
# class CreditCard(Payment):
#     def process(self,amount):
#         print("Processing payment of Rs.",amount,"via credit card")
#         self.balance+=amount
#         print("Payment Processed.")
#         print("Total balance:RS.",self.balance)
# class UpiPayment(Payment):
#     def process(self,amount):
#         print("Processing payment of RS.",amount,"via UpiPayment")
#         self.balance+=amount
#         print("Payment Processed")
#         print("Total balance:RS.",self.balance)
# class NetBanking(Payment):
#     def process(self,amount):
#         print("processing payment of rs.",amount,"via Netbanking")
#         self.balance+=amount
#         print("Payment Processed.")
#         print("Total Balance :RS.",self.balance)
# def checkout(payment):
#     payment.process(1500)
# # my_credit_card=checkout(CreditCard(10000))
# my_credit_card=checkout(UpiPayment(1500))
# # chechout(Netbanking(2000))
# #


# class PDFReport:
#     def send(self):
#         print("Pdf sending")
# class ExcelSheet:
#     def send(self):
#         print("Sending Excelsheet")
# class EmailMessage:
#     def send(self):
#         print("Sending email.")
# def dispatch(item):
#     item.send()
# d=[PDFReport(),ExcelSheet(),EmailMessage()]
# for i in d:
#     print(dispatch(i))

# def total_area(shapes):
#     area=0
#     for shape in shapes:
#         area+=shape.area()
#     print(area)
# import math
# class Circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return math.pi*self.r**2
# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l*self.b
# class Triangle:
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h
#     def area(self):
#         return 0.5*self.b*self.h
# class Hexagon:
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return (3*math.sqrt(3)/2)*self.side**2
# shapes=[Circle(10),Rectangle(2,4),Triangle(5,6),Hexagon(10)]
# total_area(shapes)

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self._log=[]
#         self.__balance=balance
#     def deposite(self,amount):
#         self.__balance+=amount
#         self._log.append(f"{amount}")
#     def get__balance(self):
#         return self.__balance
# acc=BankAccount('Alice',5000)
# acc.deposite(1000)
# # print(acc.owner)
# # print(acc._log)
# # print(acc.get__balance())
# print(acc.__balance)
# # print(acc._BankAccount__balance)

# class Temperature:
#     def __init__(self,celsius):
#         self.__celsius=celsius
#     @property
#     def celsius(self):
#         return self.__celsius
#     @property
#     def fahrenheit(self):
#         return self.__celsius*9/5+32
# t=Temperature(100)
# print(t.celsius)
# print(t.fahrenheit)
# t.__celsius=250
# print(t.celsius)
# print(t.fahrenheit)

# class Bank:
#     bank_name='ABC BANK'
#     def __init__(self,acc_holder_name,accno,balance,pin):
#         self.acc_holder_name=acc_holder_name
#         self._accno=accno
#         self.__balance=balance
#         self.__pin=pin
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,new_balance):
#         self.__balance=new_balance
# alice=Bank("alice",1223455,100000,1234)
# print(alice.acc_holder_name)
# print(alice._accno)
# print(alice.get_balance())
# alice.set_balance(1500)
# print(alice.get_balance())


# class Bank:
#     def __init__(self,balance):
#         self.__balance=balance
#     @property
#     def balance(self):
#         accno=int(input("enter account number: "))
#         pin=int(input("enter your pin: "))
#         if accno==123456 and pin==0000:
#             return self.__balance
#         else:
#             return "accessed denied!!"
#     @balance.setter
#     def balance(self,new_balance):
#         if new_balance>0:
#             self.__balance=new_balance
#         else:
#             print("value cannot be zero")
# a=Bank(1000)
# print(a.balance)


# import math
# class Circle:
#     def __init__(self,r):
#         self.__r=r
#     @property
#     def r(self):
#         return self.__r
#     @r.setter
#     def r(self,r):
#         if r>0:
#             self.__r=r
#         else:
#             print('Radius cannot be zero')
#     @property
#     def area(self):
#         return math.pi*self.__r**2
#     @property
#     def circumstence(self):
#         return 2*math.pi*self.__r
# c1=Circle(10)
# print(c1.r)
# c1.r=0
# print(c1.r)
# print(c1.area)
# print(c1.circumstence)

# class Config:
#     def __init__(self):
#         self.system_name='sys'
#         self._settings={'mode':'dark',
#                               'Ram':4,
#                          'Rom':12}
#         self.__secrete_key='py21'
#     def get_setting(self,key):
#         return self._settings[key]
# c1=Config()
# print(c1.system_name)
# print(c1._settings)
# print(c1.Config_secret_key)
# print(c1.get_setting('mode'))
#
# class Person:
#     def __init__(self,fn,ln):
#         self.__fn=fn
#         self.__ln=ln
#     @property
#     def fn(self):
#         return self.__fn
#     @fn.setter
#     def fn(self,fn):
#         self.__fn=fn
#     @property
#     def ln(self):
#         return self.__ln
#     @ln.setter
#     def ln(self,ln):
#         self.ln=ln
#     @property
#     def fullname(self):
#         return self.fn+''+self.ln
#     @fullname.setter
#     def full_name(self,fullname):
#         self.__fullname=fullname
#         self.fn,self.ln=fullname.split(' ')
# person1=Person("alice","smith")
# print(person1.fullname)
# person1.fullname