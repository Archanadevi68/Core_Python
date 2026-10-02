# function is a reusable block of code.insted of writing multiple lines of code .once you created a function whenever you need a you can call it.
# there are different types of functions .
# example function.
# def greet():
#     print("Hello student")
# greet()
# # o/p:Hello Student
# you can also store function into a varibale.
# def squre(n):
#     return n*n
# x=squre(4)
# print(x)
# o/p:16
from random import choice

from pyexpat import error


# section 1
# def say_hello():
#     print("Welcome to python!")
# say_hello()
# o/p:Welcome to python!

# def add(a,b):
#     return a+b
# print(add(2,3))
# o/p:5

# 3Q.o/p:if no return value is given to the function then iot  will give the output as "None".

# def area(length,width):
#     return length*width
# print(area(6,4))
# o/p:24

#5Q.function is set of structure .using sturcture we can use different values to pass to get the result .
# but if you wite directly code for different valures you can wirte different code .

# Section 2
# parameters are the varibale writing inside the function parathesis.arguments ar ethe actual values  you pass when calling the function.
# SINGLE PARAMETER
# def greet(name):
#     print("hello! ",name)
# greet("Alice")
# greet("Bob")
# o/p:hello! Alice
# hello!Bob

# MULTIPLE PARAMETER
# def add(a,b):
#     return a+b
# def student_info(name,age,grade):
#     return(f"name: {name}, age: {age}, grade: {grade}")
# print(add(6,5))
# print(student_info('archana',22,'A'))

# practise Questions.
# def multiply(a,b,c):
#     return a*b*c
# print(multiply(2,3,4))

# def describe_pet(animal,name):
    # return f"My {animal} is named {name}."
# print(describe_pet('dog','puppy'))

# def greet(name,age,status):
#     print(f"this is {name} and my age is {age} and iam currently{status}")
# greet('archana')
# o/p:type error greet() mising 2 required positional arguments :age and status.


# def power(base,expo):
#     return base**expo
# print(power(2,3))
# o/p:8

# def full_name(first,last,middle):
#     return f"{first} {middle} {last}"
# print(full_name('gunji','devi','archana'))

# SECTION 3
# when you pass values into a function without specifying parameter names it will assign values from left to right.
# def describe(color,size,shape):
#     print(f"A {color} {size} {shape}")
# describe('red','small','circle')

# def divide(n,d):
#     return n/d
# print(divide(10,2))
# print(divide(2,10))

# def intro(name,city,hobby):
#     return f"{name} {city} {hobby}"
# print(intro('archana','guntur','playing hockey'))
# print(intro('plaing hockey','priya','vizag'))

# def send_email(subject,to,body):
#     return to,subject,body
# print(send_email('greeting',to='archana',body='hello'))\

# Section 5.
# key word parameters
# def greet(name,message='hello'):
#     print(f"{message},{name}!")
# greet("alise","hey! there")

# SECTION 6.ORBITARY PARAMETERS(*ARGS,**KWARGS)
# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(add(1,2,3,4,5))

# def print_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
# print_info(name='archana',age=22,city='guntur')
#

# def full(a,b,*args,option='default',**kwargs):
#     print(a,b,args,option,kwargs)
# full(1,2,5,3,4,6,7,8,option='customer',x=10,y=20)

# def multiplay(*args):
#     s=1
#     for i in args:
#         s*=i
#     return s
# print(multiplay(1,2,3,4,5,6,7,8,9,10))

# def display_tags(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
# display_tags(name='archana',age=22,status='single',location='hydarabad')


# SECTION 7 FUNCTION REFERENCE
# def greet(name):
#     return f"Hello, {name}"
# say_hello=greet
# print(say_hello('archana'))
#

# def apply(func,value):
#     return func(value)
# def double(x):
#     return x*x
# def squre(n):
#     return n*n
# print(apply(double,2))
# print(apply(squre,2))

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# operation={
#     '+':add,
#     '-':sub,
#     '*':mul
# }
# op='*'
# print(operation[op](2,3))

# l=[1,2,3,4,5,6,7,8,9]
# print(len(l))

# def run_twice(func,value):
#     return func(value)
# def double(n):
#     return n*n
# print(run_twice(double,4))

# d={
#     'upper':str.upper,
#     'lower':str.lower,
#     'title':str.title
# }
# choice=input()
# def change(name):
#     return f"hello {name} you can changed to {choice} case"
# print(d[choice](change('archana')))

# def make_multiplier(x):
#     def multiple(n):
#         return n*x
#     return multiple
# multiples_of_3=make_multiplier(3)
# print(multiples_of_3(5))

# SECTION 8 LAMBDA FUNCTIONS

# squre=lambda x:x*x
# print(squre(5))

# add=lambda a,b:a+b
# print(add(5,6))

# l=[1,5,6,8,7,1,2,5,3,7]
# l.sort(key=lambda x:x)
# print(l)

# student=[
#     ('alice',85),
#     ('Bob',92),
#     ('Carol',78)
# ]
# student.sort(key=lambda x:x[1])
# print(student)


# a=lambda x:x**3
# print(a(3))

# a=lambda x,y:x if x>y else y
# print(a(9,20))

# a=lambda x:'even' if x%2==0 else 'odd'
# print(a(5))

# l=[
#     (1,'banana'),
#     (2,'apple'),
#     (3,'cherry')
# ]
# l.sort(key=lambda x:x[1])
# print(l)

# SECTION 9 HIGHER ORDER FUNCTIONS
# 1.MAP
# l=[1,2,3,4,5]
# print(list(map(lambda x:x*2,l)))
#
# a=[1,2,3]
# b=[10,20,30]
# print(list(map(lambda x,y:x+y,a,b)))

# # 2.filter
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,numbers)))

# 3.reduce
# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x+y,l))

# 4.SORTED
# l=[
#     {'name':'Alice','score':85},
#     {'name': 'Bob', 'score': 92},
#     {'name': 'Carol', 'score': 78},
# ]
# a=sorted(l,key=lambda x:x['score'],reverse=True)
# print(a)

#
# l=[1,4,5,2,6]
# print(list(map(lambda x:x*(9/5)+32,l)))

# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x*y,l))
#
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x*2,filter(lambda x:x%2==1,l))))

# l=['cat','elephant','dog','rhinoceros']
# print(reduce(lambda x,y:x if len(x)>len(y) else y,l))


#
# def my_map(func,lst):
#     l=[]
#     for i in lst:
#         l.append(func(i))
#     return l
# def squre(n):
#     return n*n
# print(my_map(squre,[1,2,3,4,5,6]))

# def mystery(*args,**kwargs):
#     print(sum(args),list(kwargs.values()))
# mystery(1,2,3,a=4,b=5)

# def f(n):
#     if n==0:
#         return 0
#     return n+f(n-1)
# print(f(4))

# from functools import reduce
# data=[2,3,4]
# res=reduce(lambda x,y:x+y,list(map(lambda x:x+1,data)))
# print(res)
#
# def apply(a,b,op):
#     return op(a,b)
#
# print(apply(3,4,lambda x,y:x+y))
# print(apply(5,4,lambda x,y:x-y))
# print(apply(3,4,lambda x,y:x*y))
#
# def make_greet(name,prefix='Hello',formatter=lambda x:x):
#     res=prefix+" "+name
#     return formatter(res)
# print(make_greet('archana',formatter=str.upper))


# def double(n):
#     return n*n
# def triple(n):
#     return n**3
# def qua(n):
#     return n**4
# def apply(func,value):
#     for i in func:
#         print(i(value))
# l=[double,triple,qua]
# apply(l,2)

#
# from functools import reduce
# def weight(**scores):
#     for key,value in scores.items():
#         print(key,value)
#     res=reduce(lambda x,y:x+y,scores.values())
#     return res/len(scores)
# print(weight(t=90,h=80,m=70,e=100))

# student=[
#     {'name':'archana','score':90},
# {'name':'priya','score':80},
# {'name':'arjun','score':88},
# {'name':'sidhu','score':60}
# ]
# res=filter(lambda x:x['score']>60,student)
# res1=map(lambda x:{**x,'grade':'pass'},res)
# res2=sorted(res1,key=lambda x:x['score'],reverse=True)
# print(res2)

# d={
#     'by_name':lambda x:x[0],
#     'by_score':lambda x:x[1],
#     'by_length':lambda x:len(x[0])
# }
# l=[('archana',90),('arjun',96),('priya',96),('trisha',95)]
# choice=input()
# print(sorted(l,key=d[choice]))

# op={
#     'add':lambda x,y:x+y,
#     'mul':lambda x,y:x*y,
#     'min':lambda x,y:x if x<y else y,
#     'max':lambda x,y:x if x>y else y
# }
# def calculator(*args,operation='add',**options):
#     func=op[operation]
#     res=args[0]
#     for i in args:
#         if options.get("show_steps"):
#             print(res,i,operation,func(res,i))
#         res=func(res,i)
#     print(res)
# calculator(1,2,3,4,5,opration='add',show_steps='True')


# DECORATORS
# def greet():
#     print("hello")
# say=greet
# say()

# def greet():
#     print("this is outer function")
#     def inner():
#         print("hello")
#     return inner
# say=greet()
# say()

# BUILDING A  REAL DECORATOR
# def my_decorator(func):
#     def wrapper():
#         print("before the function start")
#     func()
#     print("after function start")
#     return wrapper
# def greet():
#     print("hello world")
# say=my_decorator(greet)
# say()


# def decorator(func):
#     print("brfore the function start")
#     def wrapper(*args,**kwargs):
#         print("this is inside the outer function and its is a wrapper function")
#         res=func(*args,**kwargs)
#         print("this is function is outside")
#         return res
#     return wrapper
# def add(a,b):
#     return a+b
# say=decorator(add)
# print(say(4,5))

# USING DECORATOR
# def shout(func):
#     def wrapper(*args,**kwargs):
#         print("this is inner function")
#         res=func(*args,**kwargs)
#         return str(res).upper()
#     return wrapper
#
# @shout
# def greet(name):
#     return (f"hello {name}")
# print(greet('archana'))
#
# import functools
# def my(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper
# @my
# def greet():
#     pass
# print(greet.__name__)


#
# import functools
# def repeat(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#                 return result
#             return wrapper
#     return decorator
# @repeat(3)
# def say_hello():
#     print("Hello!")
# say_hello()



# import functools
# def prefix_log(prefix,seprator=' ! '):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             res=func(*args,**kwargs)
#             print(f"{prefix}{seprator}{res}")
#             return res
#         return wrapper
#     return decorator
# @prefix_log('INFO')
# def status():
#     return  "server is running"
#
# @prefix_log('ERROR')
# def error():
#     return "404 Not Found"
# status()
# error()


# _username='Archana'
# _password='1234'
# successful_attempts=0
# unsuccessful_attempts_u=0
# unsuccessful_attempts_p=0
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("please enter your details to login")
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def login(username,password):
#     global successful_attempts,unsuccessful_attempts_u,unsuccessful_attempts_p
#     if _username==username and _password==password:
#         print("you are succesfully login")
#         successful_attempts+=1
#         return
#     elif _username!=username:
#         unsuccessful_attempts_u+=1
#         if unsuccessful_attempts_u<=3:
#             username=input("the user name does not exit please enter username: ")
#             login(username,password)
#         else:
#             print("you are not able to login ")
#             return
#     elif password!=_password:
#         unsuccessful_attempts_p+=1
#         if unsuccessful_attempts_p<3:
#             password=input("you enter the wrong passwor dplase enter correct password: ")
#             login(username,password)
#         else:
#             print("you loged out pleaase try again later")
#             return
# login(input("enter user name:"),input("enter password: "))
# print("unsuccessful_attempts_u",unsuccessful_attempts_u)
# print("unsuccesssful_attempts_p",unsuccessful_attempts_p)

# CLASS
# class student:
#     def __init__(self,age):
#         if age>18:
#             self.age=age
#         else:
#             raise ValueError('Age is below 18')
# s1=student(21)
# print(s1.__dict__)

# class Bank:
#     def __init__(self,account_holder,account_number,balance):
#         if balance>0:
#             self.balance=balance
#         else:
#             self.balance=0
#         self.account_holder = account_holder
#         self.account_number = account_number
# e1=Bank('archana',9392702947,200000)
# e2=Bank('arjun',8834528031,-500000)
# print(e1.__dict__)
# print(e2.__dict__)


# class Employee:
#     company='TechCorp'
#     employee_count=0
#     def __init__(self,name,department,salary,experience):
#         if salary>0 and experience>0:
#             if experience>5:
#                 self.bonus=(salary*15)//100
#             elif experience>=3:
#                 self.bonus=(salary*10)//100
#             else:
#                 self.bonus=(salary*5)//100
#             self.name=name
#             self.department=department
#             self.salary=salary
#             self.experience=experience
#             Employee.employee_count+=1
#             employee_id=Employee.employee_count
#             final_salary=self.bonus+salary
#             self.pay_details={
#                 "name":name,
#                 "salary":salary,
#                 "experience":experience,
#                 "bonus":self.bonus,
#                 "final_salary":final_salary,
#                 "employee_id":employee_id
#             }
# e1=Employee('archana','CSE',200000,5)
# print(e1.__dict__)


# class Student:
#     college_name="ABC COLLEGE"
#     count=0
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         if marks>=0 and marks<=100:
#             self.marks=marks
#         else:
#             self.marks=0
#         Student.count+=1
# s1=Student('Abhilash',75457,99)
# s2=Student("yesmitha",1,100)
# print(s1.__dict__)
# print(s2.__dict__)

# product=[]
# class Product:
#     store_name='ABC STORE'
#     def __init__(self,name,price,quality):
#         self.name=name
#         if price>0 and quality>0:
#             self.price=price
#             self.quality=quality
#         else:
#             raise ValueError("invalid quality or price")
#         product.append(name)
# p1=Product('mars Lip Liner',79,5)
# p2=Product("ps5",50000,1)
# p3=Product('kay beauty lip oil',799,1)
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)
#
# print(product)