# def m1():
#     def m2():
#         print('hi')
#     return m2
# func=m1()
# func()

# def m1():
#     print('hi')
#     x=20
#     return x
# value=m1()
# print(value)


# def m1(func):
#     print('hi')
#     def wrapper():
#         func()
#         print('this is python -21 batch')
#         print('hello')
#     return wrapper
#     # return 10
# def greet():
#     print('archan')
# my_func=m1(greet)
# # my_func()
# # x = m1(greet)
# # x = wrapper
# # x()
# # print(m1(greet()))
#
#
#
#

# def my_decorator(func):
#     def wrapper():
#         print('System Starting')
#         func()
#     return wrapper
# def start_system():
#     print('system started successfully')
# start_system=my_decorator(start_system)
# start_system()

# def my_decorator(func):
#     print('archana')
#     def wrapper():
#         print('System Starting')
#         func()
#         print('successful')
#     return wrapper
#
# # @my_decorator
# def start_system():
#     # print('system started successfully')
#     # pass
# x=my_decorator(start_system)
# x()
#
#



import functools
def dec1(func):
    @functools.wraps(func)
    def wrap1(*args,**kwargs):
        print("function starting")
        func(*args,**kwargs)
        print("function ending")
    return wrap1
def dec2(func):
    @functools.wraps(func)
    def wrap2(*args,**kwargs):
        print("this is second function starting")
        func(*args,**kwargs)
        print("this is second function ending")
    return wrap2
@dec2
@dec1
def greet(name):
    print("hii!",name)
greet=dec2(greet)
greet('archana')
# print(greet.__name__)













