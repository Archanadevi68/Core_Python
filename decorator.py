# def greet():
#     print("hello")
# say_hello=greet
# say_hello()

# def outer():
#     message="iam the outer function"
#     def inner():
#         print(message)
#     inner()
# outer()

# def make_greeter():
#     def say_hi():
#         print("hi there")
#     return say_hi
# x=make_greeter()
# x()


# def my_decorator(func):
#     def wrapper():
#         print("__Before the function runs__")
#         func()
#         print("__after the function runs__")
#     return wrapper
# def hello():
#     print("This is my own function")
# x=my_decorator(hello)
# x()



# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Function staring...")
#         res=func(*args,**kwargs)
#         print("after execution...")
#         return res
#     return wrapper
# def add(a,b):
#     return a+b
# x=my_decorator(add)
# print(x(10,20))


# def shout(func):
#     def wrapper(*args,**kwargs):
#         print("function berfore..")
#         res=func(*args,**kwargs)
#         print("after execution..")
#         return res
#     return wrapper
# @shout
# def hello(name):
#     return f"my name is {name}"
# print(hello('archana'))




# def shout(func):
#     def wrapper(*args,**kwargs):
#         print("this is function starting..")
#         res=func(*args,**kwargs)
#         print("this is function ending..")
#         return str(res).upper()
#     return wrapper
# @shout
# def hello(name):
#     return f"my name is {name}"
# print(hello('archana'))



# def bold(func):
#     def wrapper(*args,**kwargs):
#         print("this is bold function")
#         return func(*args,**kwargs)
#     return wrapper
# def italic(func):
#     def wrapper1(*args,**kwargs):
#         print("this is italic function")
#         return func(*args,**kwargs)
#     return wrapper1
# @bold
# @italic
# def message():
#     return "Hello"
# # print(message())
# mes=italic(message)
# mes()



# import functools
# def my_decor(func):
#     @functools.wraps(func)
#     def wrap(*args,**kwargs):
#         print("this is starting")
#         func(*args,**kwargs)
#     return wrap
# @my_decor
# def greet():
#     print("Hello")
# print(greet.__name__)


# def dec2(x):
#     def dec1(func):
#         def wrapper1(*args,**kwargs):
#             for i in range(x):
#                 res=func(*args,**kwargs)
#             return res
#         return wrapper1
#     return dec1
# @dec2(3)
# def say_hello():
#     print("hello")
# say_hello()



# def m1():
#     x=20
#     print(x)
# m1()

# x=5
# def m1():
#     x=50
#     return x
# m1()
# # print(x)

# x=5
# def m1():
#     global x
#     x=15
# m1()
# print(x)


# _username="archana"
# _password='123@'
# successful_attempts=0
# unsuccessful_attempts_u=0
# unsuccesssful_attempts_p=0
# def dec1(func):
#     def wrap1(*args,**kwargs):
#         print("welcome to our application!please login to continue")
#         func(*args,**kwargs)
#     return wrap1
# @dec1
# def login(username,password):
#     global successful_attempts,unsuccessful_attempts_u,unsuccesssful_attempts_p
#     if _username==username and _password==password:
#         print("login successful")
#         successful_attempts+=1
#         return
#     elif _username!=username:
#         unsuccessful_attempts_u+=1
#         if unsuccessful_attempts_u<=3:
#             print("this user name does not exit. reenter user name: ")
#             login(username,password)
#         else:
#             print("your not able o login")
#             return
#     elif _password!=password:
#         unsuccesssful_attempts_p+=1
#         if unsuccesssful_attempts_p<=3:
#             print("re_enter password: ")
#             login(username,password)
#         else:
#             print("out of time")
#             return
# login(input("enter user name:"),input("enter password: "))
# print("unsuccessful_attempts_u",unsuccessful_attempts_u)
# print("unsuccesssful_attempts_p",unsuccesssful_attempts_p)

_username = "mohana"
_password = "1234"

successful_attempts = 0
unsuccessful_attempts_u = 0
unsuccessful_attempts_p = 0
def dec1(func):
    def wrap1(*args, **kwargs):
        print("Welcome to our application! Please login to continue.")
        func(*args, **kwargs)
    return wrap1
@dec1
def login(username, password):
    global successful_attempts, unsuccessful_attempts_u, unsuccessful_attempts_p
    if _username == username and _password == password:
        print("Login Successful")
        successful_attempts += 1
        return
    elif _username != username :
        unsuccessful_attempts_u += 1
        if unsuccessful_attempts_u <= 3:
            username = input("This username does not exist. Re-enter the username: ")
            login(username, password)
        else:
            print("You're out of attempts. Try again later.")
            return

    else:
        unsuccessful_attempts_p += 1
        if unsuccessful_attempts_p <= 3:
            password = input("You've entered the wrong password. Re-enter the password: ")
            login(username, password)
        else:
            print("You're out of attempts. Try again later.")
            return
login(input("Enter Username"), input("Enter Password"))
print("Unsuccessful Password attempts : ", unsuccessful_attempts_p)
print("Unsuccessful Username attempts : ", unsuccessful_attempts_u)
print("Successful Attempts : ", successful_attempts)



