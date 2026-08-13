import numbers

count = len
list1 = [1,2,3,4,5,6,7]
# print(count(list1))

def run_twice(func, value):
    return func(func(value))
def square(value):
    return value ** 2
def cube(value):
    return value ** 3

# print(run_twice(square, 3))
# print(run_twice(cube, 3))
operate = {'U': str.upper,
           'L': str.lower,
           'T': str.title
           }
text = "hEllOHiE"
# print(operate['T'](text))
def hello(name):
    print("This is the hello function")
    print("Hi !", name)
    print("Trying functional referencing")
# hello("Nithi")
# x = 10
# y = x
# hii = hello
# hii("Harshi")




# def multiply_with_three(num):
#     return num * 3
# def multiplier(num):
#     return multiply_with_three(num)
# print(multiplier(4))
# # print(multiplier(5))



#15/7/2026
# 1.assign built fun  sum to a variable and used it to calculate the total of list of numbers.Number
# 2.store function min,max,sum in a dictonary allow the user to choose which operation allow to perform.
# 3.write a function repeat with parameters(func, n, value).

# 1.code
# l=[10,20,30,40,50]
# s=sum(l)
# print(s)

# 2.code
# def store(*args):
#     d={'min':min,'max':max,'sum':sum}
#     print(d['sum'](args))
# store(1,2,3,4,5,6,7)

# def store(list):
#     list=[10,20,30,40,50]
#     d = {'min': min, 'max': max, 'sum': sum}
#     return(d['min'](list))
# print(store(list))


#3.code
def squre(value):
    return value ** 2
def repeat(func,n,value):
    for i in range(n):
        value=func(value)
    return value
print(repeat(squre,3,2))
































