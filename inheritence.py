# class Bank:
#     def __init__(self,balance,name):
#         self.balance=balance
#         self.name=name
#     def deposit(self,amount):
#         self.amount=amount
#         self.balance+=amount
#     def withdraw(self,amount):
#         self.amount=amount
#         self.balance-=self.amount
#     def check_balance(self):
#        return self.balance
# class User(Bank):
#
#     pass
# obj=User()
# obj.deposit(500(10000,'archana'))


# single level inhertence
# one child calss and one parent class
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return f"{self.name} makes a sound"
# class Dog(Animal):
#     def fetch(self):
#         return f"{self.name} fetches the ball!"
# # d=Dog('puppy')
# # print(d.speak())
# # print(d.fetch())
# a=Animal('bunty')
# print(a.speak())
# # print(a.fetch())



# multilevel_inheritence
# grandparent to parent to child
# class Vehicle:
#     def start(self):
#         return 'vehicle started'
# class Car(Vehicle):
#     def drive(self):
#         return 'car is driving'
# class ElectricCar(Car):
#     def charge(self):
#         return 'charging battery'
# ec=ElectricCar()
# print(ec.start())
# print(ec.drive())
# print(ec.charge())


# Multiple Inheritence
# child inhert from two parents
# class Flyable:
#     def fly(self):
#         return 'It can fly'
# class Swimmable:
#     def swim(self):
#         return 'It can swim'
# class Duck(Flyable,Swimmable):
#     def quack(self):
#         return "Quack!"
# d=Duck()
# print(d.fly())
# print(d.swim())
# print(d.quack())


# Hierachical Inheritence
# multiple children from one parent
# class Shape:
#     def area(self):
#         return 0
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*self.r**2
# class Rectangle(Shape):
#     def __init__(self,w,h):
#         self.w=w
#         self.h=h
#     def area(self):
#         return self.w*self.h
# print(Circle(5).area())
# print(Rectangle(4,6).area())


# Hybrid Inherientence
# It is a combination of multiple and hierachical inheritence

# class A:
#     def hello(self):
#         return 'Hello from A'
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# print(D().hello())
# print([C.__name__ for C in D.__mro__])
# print(D.mro())
# print(D.__mro__)


# Section 2 MRO---METHOD RESOULATION ORDER
# when a method is called of an object .pyhton searches for a specif order .this order is called method resoulation order it prevalents the ambugity in multiple inherientes.
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
#
# print(D.__mro__)
# print(D.mro())
# for c in D.mro():
#     print(c.__name__,end='-->')


# MRO DETERMINES WHICH METHOD RUNS
# class A:
#     def greet(self):
#         return 'Hello from A'
# class B(A):
#     def greet(self):
#         return 'Hello from B'
# class C(A):
#     def greet(self):
#         return 'Hello from c'
# class D(B,C):
#     pass
# print(D().greet())


# SECTION 3 SUPER()-- IN INSTANCE & CLASS METHODS
# super return a proxy object that delegates method calls to the next class in the mro.it lets you call a parent method withod hard coding the parent class name
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def describe(self):
#         return f"{self.name},age {self.age}"
# class Employee(Person):
#     def __init__(self,name,age,department):
#         super().__init__(name,age)
#         self.department=department
#     def describe(self):
#         base=super().describe()
#         return f'{base},dept:{self.department}'
# class Manager(Employee):
#     def __init__(self,name,age,department,team_size):
#         super().__init__(name,age,department)
#         self.team_size=team_size
#     def describe(self):
#         base=super().describe()
#         return f'{base},team:{self.team_size} people'
# m=Manager('Archana',22,'cse_ai',3)
# print(m.describe())


# class Animal:
#     species='Unknown'
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def create(cls,name):
#         print(f'Animal.create() called with cls={cls.__name__}')
#         return cls(name)
# class Dog(Animal):
#     species='canis lupus familiaris'
#     @classmethod
#     def create(cls,name):
#         print(f'Dog.create() called')
#         x=super().create(name)
#         return x
# d=Dog.create('Relax')
# print(d.name,d.species)




# 1. Bank Management System
# Create a Bank class with:
# • balance variable
# • deposit()
# • withdraw()
# • check_balance()
# Create a User class that inherits Bank and displays the user's name. Perform
# deposit, withdrawal, and balance check.


# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print(f"RS {amount} deposited successfuly")
#     def withdraw(self,amount):
#         self.balance-=amount
#         print(f'Withdraw  of RS {amount} successfuly')
#     def check_balance(self):
#         print(f"your current available balance {self.balance}")
# class User(Bank):
#     def __init__(self,username,balance):
#         self.name=username
#         super().__init__(balance)
# user1=User('Archana',100000)
# user1.check_balance()
# print(user1.name)


# 2. Employee Salary System
# Create an Employee class with:
# • emp_name
# • salary
# • display_details()
# Create a Manager class that inherits Employee and adds a bonus(). Display the
# total salary.


# class Employee:
#     def __init__(self,emp_name,salary):
#         self.employee_name=emp_name
#         self.salary=salary
#     def display_details(self):
#         print(f"Employee Name {self.employee_name}")
#         print(f'employee_salary {self.salary}')
# class Manager(Employee):
#     def bonus(self):
#         self.salary=self.salary+self.salary*0.1
# manager1=Manager('Archana',100000)
# manager1.bonus()
# print(manager1.salary)




#3. Create a Student class with:
# • Name
# • marks
# • display_marks()
# Create a Result class that inherits Student and calculates whether the student has
# passed or failed.

# class Student:
#     def __init__(self,Name,Marks):
#         self.Name=Name
#         self.Marks=Marks
#     def display(self):
#         print(self.Marks)
# class Result(Student):
#     def display(self):
#         if self.Marks>60:
#             print('Pass')
#         else:
#             print("Fail")
#
# s1=Result('Archsna',95)
# s1.display()


# 4. Food Ordering System Using Multilevel Inheritance
# Class 1: Restaurant
# • Create a method menu(item) that returns the price of the selected food
# item.
# Class 2: FoodCourt (inherits Restaurant)
# Create the following methods:
# • display_menu() – Display the available food items.
# • order() – Accept the food item from the user and allow multiple orders.
# • billing() – Display the total bill and add a packing charge of ₹20.
# Class 3: Customer (inherits FoodCourt)
# • Create an object of the Customer class.
# • Call the order() method.


# class Restaurant:
#     def menu(self,item):
#         items={
#             'briyani':200,
#             'coke':20,
#             'dessert':100,
#             'curd rice':50
#         }
#         return items.get(item)
# class FoodCourt(Restaurant):
#     def display_menu(self):
#         print("briyani:200\ncoke:20\ndessert:100\ncurd rice:50")
#     def billing(self,cost):
#         print(f"your total cart value is :RS.{cost}")
#         print("packining charges are :RS.20")
#         print(f"Your total bill is :RS{cost+20}")
#     def order(self):
#         total_cost=0
#         while True:
#             self.display_menu()
#             choice=input("enter your food items you want: ")
#             total_cost+=self.menu(choice)
#             next=input("do want to continue your order?y/n")
#             if next=='n':
#                 break
#         self.billing(total_cost)
# class Customer(FoodCourt):
#     pass
# c=Customer()
# c.order()

#
# 5. Movie Ticket Booking System Using Multilevel Inheritance
# Class 1: Movie
# • Create a method ticket(movie) that returns the ticket price.
# Class 2: Booking (inherits Movie)
# Create the following methods:
# • movies() – Display the available movies.
# • selection() – Allow the user to book multiple tickets.
# • billing() – Display the total amount and add a booking charge of ₹30.
# Class 3: Customer (inherits Booking)
# • Create an object and call the selection() method.

# class Movie:
#     def ticket(self,movie):
#         if movie=='Ranabali':
#             return 200
#         elif movie=='kalki':
#             return 120
#         elif movie=='fidda':
#             return 100
# class Booking(Movie):
#     def movies(self):
#         print("Ranabali\nkalki\nfidda")
#     def billing(self,cost):
#         print(f"your total cost for booking is {cost}")
#         print("booking charges included RS.30")
#         print(f"your total amount to payable is {cost+30}")
#     def selection(self):
#         total=0
#         self.movies()
#         while True:
#             choose=input("enter a movie name that you would watch: ")
#             tickets=int(input("enter how many tickets you want: "))
#             total += self.ticket(choose) * tickets
#             ch=input("enter if you want to book for another movie ?y/n")
#             if ch=='n':
#                 break
#         self.billing(total)
#
#
# class Customer(Booking):
#     pass
# c=Customer()
# c.selection()


# class Course:
#     def fee(self,course):
#         if course=='CSE':
#             return 100000
#         elif course=='ECE':
#             return 80000
#         elif course=='CIVIL':
#             return 60000
# class Academy(Course):
#     def courses(self):
#         print("CSE\nECE\nCIVIL")
#     def billing(self,total):
#         print(f"your total bill for the course is{total}")
#         print("adding the registration fee was RS.100")
#         print(f"your total bill for course after adding the registration fee was {total+100}")
#     def enroll(self):
#         cost=0
#         self.courses()
#         while True:
#             choose=input("enter which course you want to enroll: " )
#             cost+=self.fee(choose)
#             next=input("do you want to add another course ?y/n")
#             if next=='n':
#                 break
#         self.billing(cost)
# class Student(Academy):
#     pass
# s=Student()
# s.enroll()


# 7. Cab Booking System Using Hierarchical Inheritance
# Class 1: Cab
# • Create methods to calculate the fare for Bike, Auto, and Car rides.
# Class 2: Uber (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 10% GST and apply a 15% discount if the bill is above ₹1000.
# Class 3: Ola (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 12% GST and apply a 20% discount if the bill is above ₹1500.
# Driver Code
# • Ask the user to choose Uber or Ola and call the booking() method.
#


# class Cab:
#     def bike(self,distance):
#         return distance*50
#     def auto(self,distance):
#         return distance*70
#     def car(self,distance):
#         return distance*100
# class Uber(Cab):
#     def menu(self):
#         print("bike=50/km")
#         print("auto=70/km")
#         print("car=100/km")
#     def billing(self,amount):
#         amount+=amount*0.1
#         if amount>1000:
#             amount-=amount*0.15
#         print("your total fare is RS.",amount)
#     def booking(self):
#         self.menu()
#         vehicle=input("enter your vehicle choice.")
#         total_cost=0
#         distance=int(input("enter the distance: "))
#         if vehicle=='bike':
#             total_cost=self.bike(distance)
#         elif vehicle=='auto':
#             total_cost=self.auto(distance)
#         elif vehicle=='car':
#             total_cost=self.car(distance)
#         else:
#             print("invalid choose")
#         return self.billing(total_cost)
# class Ola(Cab):
#     def menu(self):
#         print("bike=50/km")
#         print("car=100/km")
#         print("auto=70/km")
#     def billing(self,amount):
#         amount+=amount*0.12
#         if amount>1000:
#             amount-=amount*0.2
#         print(f"your total fare for booking is{amount}")
#     def booking(self):
#         self.menu()
#         total_cost=0
#         vehicle=input("enter which service you want to take:")
#         distance=int(input("enter how many distance you want to travel"))
#         if vehicle=='bike':
#             total_cost=self.bike(distance)
#         elif vehicle=='car':
#             total_cost=self.car(distance)
#         elif vehicle=='auto':
#             total_cost=self.auto(distance)
#         return self.billing(total_cost)
# choose=input("enter which app you would like to open?")
# if choose=='uber':
#     Uber().booking()
# elif choose=='ola':
#     Ola().booking()
# else:
#     print("Invalid Choice")



# 10. ATM System Using Multiple Inheritance
# Class 1: SBI
# • Create the methods deposit(amount) and check_balance().
# Class 2: UnionBank
# • Create the methods withdraw(amount) and mini_statement().
# Class 3: ATM (inherits SBI and UnionBank)
# • Create the methods menu() and transaction().
# • Allow the user to perform banking operations.
# Driver Code
# • Create an object of the ATM class.
# • Call the transaction() method.



# class SBI:
#     def __init__(self,balance):
#         self.balance=balance
#         self.statement=[]
#     def deposite(self,amount):
#         self.balance+=amount
#         print("your account has been deposited with amount RS.",amount)
#         self.statement.append("Deposite RS."+str(amount))
#     def check_balance(self):
#         print("your balance is RS.",self.balance)
# class Union:
#     def __init__(self,balance):
#         self.balance=balance
#         self.statement=[]
#     def withdraw(self,amount):
#         self.balance-=amount
#         print("your total available balance is",amount)
#         self.statement.append("Withdrawal RS."+str(amount))
#     def ministatement(self):
#         print(self.statement)
# class Atm(SBI,Union):
#     def menu(self):
#         print("1.Withdraw\n2.Deposit\n3.checkbalance\n4.ministatement")
#     def tranction(self):
#         self.menu()
#         while True:
#             op=int(input("Enter the option: "))
#             if op==1:
#                 self.withdraw(int(input("Enter the withdraw amount.")))
#             elif op==2:
#                 self.deposite(int(input("Enter deposite amount")))
#             elif op==3:
#                 self.check_balance()
#             elif op==4:
#                 self.ministatement()
#             else:
#                 break
# user=Atm(12000)
# user.tranction()

