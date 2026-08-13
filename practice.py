# print("this is python 21")
# print("we are learning how to write functions in python")
# def greet():
#     print("hiee")
# greet()
# def say_hi(name):
#     print("hi",name)
# say_hi("Shiva")
# say_hi("Nikith")
#
# def hello(a,b):
#     print("welcome to the hello function")
#     print(a+b)
#     print(a-b)
#     return a,b
#
# x, y = hello(10,20)
# print(x,y)
# # print(hello(10,20))
import code
from http.cookiejar import uppercase_escaped_char

# def send_email(to,subject,body):
#     print(f"TO:{to}\nsubject: {subject}\nBody:{body}\nis used for the whole concept of the mail")
# send_email(body='working on the key word arguments',to='archanagunji043@gmail.com',subject='asking for leave')

# def create_profile(username,email,age):
#     print(username,email,age)
# create_profile(username='archana\n',email='archanagunji043@gmail.com\n',age=20)

# def create_profile(username,email,age):
#     print(username,email,age)
# create_profile('archana','archana@gmail',22,username='jimi',email='',age=20)
#
# o/p:typeError(got multiple values for arguments)
#

# def book_ticket(name,start,to,stops):
#     print('book ticket:',name,start,to,stops)
# book_ticket('Alice','Delhi','mumbai',2)


# def intro(name,city,hobby):
#     print(f"his name is {name}.he is from {city}.his hobbys are {hobby} ")
# intro('cricket','arjun','sidney')
# intro(name='arjun',city='sidney',hobby='hockey')

# def subtract(a,b):
#     return a-b
# print(subtract(10,3))
# print(subtract(3,10))

# def bio(first_name,last_name,age):
#     print(first_name,last_name,age)
# bio('archana','devi',20)
# bio(20,'devi','archana')


#8/7/2026
# def power(base,exponent=2):
#     return base**exponent
# print(power(2))
# print(power(2,3))

# def connect(host,port=3306,protocol='TCP'):
#     print(host,port,protocol)
#     print(protocol,host,port)
#     print(port,protocol,host)
# connect("local")
# connect("localhost")

# def func(name='guest',age):
#     print(name,age)
# func(20)
# func(21) --SyntaxError: parameter without a default follows parameter with a default

# def discount_price(price,discount=10):
#     return price-discount
# print(discount_price(100))
# print(discount_price(100,10))



# def food_delivary_app(name,order_type='regular',*items,**info):
#     print(name)
#     print(order_type)
#     for i in items:
#         print(i)
#     for key,value in info.items():
#         print(key,value)
#     return food_delivary_app
# print(food_delivary_app(input('enter your name: '),'veg',))


#14/7/2026
#1.code
# l=[1,2,3,4,'archana','devi']
# count=len
# print(count(l))


#2.code
# def squre(number):
#     return number * number
# def run_twice(squre,value):
#     return squre(squre(value))
# print(run_twice(squre,2))

#3.code
# string_type={'upper':str.upper,'lower':str.lower,'title':str.title}
# string=input()
# print("string_type avalilable:'upper','lower','title'")
# choice=input()
# if choice in string_type:
#     chosen_function=string_type[choice]
#     result=chosen_function(string)
#     print(result)

#4.code
# def make_multiplier(n):
#     def mutiplier(x):
#         return n*x
#     return mutiplier
# print(make_multiplier(3))
# res=make_multiplier(3)
# print(res(3))

#5.code
def greet():
    return "Hello World"

func={
    'say_hello':greet,
    'greet':greet,
    'welcome':greet
}
print(func['say_hello']())
print(func['greet']())
























