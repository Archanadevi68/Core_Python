# l=[20,19,44,50,60]
# print(list(map(lambda x:f"{(x*9/5)+32}F",l)))

# l=['Archana','Devi','gunji','arjun','Lucky']
# print(list(filter(lambda x: x==x.title() ,l)))


# from functools import reduce
# l=[1,2,3,4,5]
# res=reduce(lambda x,y:x*y,l)
# print(res)

# l=[('archana',20),('mahi',21),('arjun',23),('krishna',25)]
# print(sorted(l,key=lambda x:x[1],reverse=True))

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,map(lambda x:x if x%2==1 else x**2,l))))

# from functools import reduce
# # l=['cat','elephant','dog','rhinoceros']
# l=['cow','dog','cat','rat']
# print(reduce(lambda x,y:x if len(x)>len(y) else y,l ))

# from functools import reduce
# l=[200,500,1000,800,900,2000,10000]
# res=map(lambda x: x if x<500 else x-(x*10)/100 ,
#                filter(lambda x:x>500,l))
# res2=map(lambda x:x ,filter(lambda x: x<=500,l))
# print(reduce(lambda x,y:x+y,res)+reduce(lambda x,y:x+y,res2))

#
# from functools import reduce
# l=[1,3,5,-1,6,0,7,-9,-3,-5,1,6,-10]
# sum=((list(map(lambda x:abs(x),filter(lambda x:x<0,l))))
#      +list(map(lambda x: x,filter(lambda x:x>0,l))))
# print(reduce(lambda x,y:x+y,sum))


# from functools import reduce
# l=[20,15,30,50,60,70,10,5]
# maximum=map(lambda x:x if x>50 else x*3,
#             filter(lambda x: x < 50,l))
# print(reduce(lambda x,y:x if x>y else y,maximum))



# from functools import reduce
# l=['sowjanya','devi','cow','to','arjun','krishna']
# res=map(lambda x: x.upper() if 3<len(x) else x,
#         filter(lambda x:3<len(x),l))
# print(reduce(lambda x,y:(x+y),res))


# from functools import reduce
# emp_salary=[10000,25000,50000,13000,60000,15000]
# res=list(map(lambda x:x+(x*10)/100,filter(lambda x:x>30000,emp_salary)))+list(map(lambda x:x,filter(lambda x:x<=30000,emp_salary)))
# print(reduce(lambda x,y:(x+y),res))


# from functools import reduce
# l=[1,2,3,5,4,6,7,3,9,8]
# res=map(lambda x:x if x%2==0 else x**2,
#         filter(lambda x:x%2==1,l))
# print(reduce(lambda x,y:x+y,res))

# from functools import reduce
# l=[350,176,640,540,240,737,97]
# res=map(lambda x:x if x<500 else (x+
#                                  (x*10)/100),
#         filter(lambda x:x>500,l))
# print(reduce(lambda x,y:x+y,res))



# 25/7/2026
# Q1.
# list1=[
#     ('arjun',98),('archana',98),('devi',96),('krishna',60)
# ]
# print(sorted(list1,key=lambda x:(-x[1],x[0])))
#

# Q2.
# list2=['bhema','balaram','anjaneya','arjun','devi']
# print(sorted(list2,key=lambda x:(len(x),x)))

# Q3.
# from functools import reduce
# list3=[10,5,20,16,78,80,90,12,34,56]
# print(reduce(lambda x,y:(x+y)+5,filter(lambda x: x%2==0 and x%5==0,map(lambda x:x,list3))))

# Q4.
# from functools import reduce
# l=['malayalam','arjun','aditya','archana','devi']
# print(reduce(lambda x,y:x+" @ "+y,list(sorted(map(lambda x:x.upper(),filter(lambda x:x[0]==x[-1],l)),key=lambda x:(x[-1],len(x))))))
# Q5.
# from functools import reduce
# list5=[
#     {"Type":"credit","amount":1000},
#     {"Type":'debit','amount':500},
#     {"Type":'credit','amount':2000}
# ]
# res=filter(lambda x:x['Type']=='credit',list5)
# bonus=map(lambda x:{"Type":x['Type'],'amount':int(x['amount']+(x['amount']*5)/100)},res)
# res2=sorted(bonus,key=lambda x:x['amount'],reverse=True)
# # amount=map(lambda x:x['amount'],res2)
# # print(res2[0]['amount'])
# print(res2)
# print(reduce(lambda x,y:x['amount']+y['amount'],res2))

# mixed concept
# Q1.
def mixed(a,b,op):
    op={
        'add':lambda x,y:x+y,
        'sub':lambda x
    }
    return op(a,b)
print("add",mixed(10,5,lambda x,y:x+y))
print("sub",mixed(20,10,lambda x,y:x-y))
print("multiply",mixed(5,5,lambda x,y:x*y))

# Q3.

# def greeting(name,prefix='hello',formatter=lambda x:x):
#     gret=prefix+" "+name
#     return formatter(gret)
# print(greeting('archana'))
# print(greeting('archana',formatter=str.upper))

# Q4.
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# res=filter(lambda x:x%3==0,map(lambda x:x,l))
# print(list(res))
#

# Q10.
# def calculator(*args,operation='add',**options):
#     op={'add':lambda x,y:x+y,
#         'sub':lambda x,y:x-y,
#         'mul':lambda x,y:x*y,
#         'max':lambda x,y:(x,y),
#         'min':lambda x,y:(x,y)
#     }
#     func = op[operation]
#     res=args[0]
#     for i in args:
#         if options.get('show_steps'):
#             print(res,i,operation,func(res,i))
#         res=func(res,i)
#     return res
# print(calculator(1,2,3,4,5,6,operation='mul',show_steps=True))
#
#Q5.
# def double(x):
#     return x ** 2
# def triple(x):
#     return x ** 3
# def quadruple:
#     return x ** 4

# double = lambda x : x ** 2
# triple = lambda x : f" {double(x)} ,    {x ** 3}"
#
# quadruple = lambda x  : x ** 4
#
# operations = [double, triple, quadruple]
#
# def apply_all(funcs, value):
#     for func in funcs:
#        print(func(value))
# apply_all(operations, 10)

# Q7.
from functools import reduce
# def weighted_average(**scores):
#     for key,value in scores.items():
#         print(key,value)
#     total=reduce(lambda x,y:x+y,scores.values())
#     return total/len(scores)
# print(weighted_average(telugu=98,hindi=99,maths=95,science=90))
# print(reduce(weighted_average,lambda x,y:x[1]+y))

# Q8.
# list1=[
#     {'name':'archana','score':95},
#     {'name':'arjun','score':88},
#     {'name':'archana','score':50},
#     {'name':'archana','score':45}
# ]
# res=filter(lambda x:x['score']>=60,list1)
# grade=map(lambda x:{**x,'grade':'pass'},res)
# res1=sorted(grade,key=lambda x:x['score'],reverse=True)
# print(res1)

# Q9.
# res=[
#     ('archana',99),('arjun',90),('akhila',90),('raju',89),('shiva',70)
# ]
# d={
#     'by_name':lambda x:x[0],
#     'by_score':lambda x:x[1],
#     'by_length':lambda x:len(x[0])
# }
# print("available choices are: by_name,by_score,by_length")
# choice=input()
# if choice in d:
#     res1=sorted(res,key=d[choice])
#     print(res1)
#
#
# from functools import reduce
# def calculator(*args,operation,**option):
#     op={
#         'add':lambda x,y:x+y,
#         'mul':lambda x,y:x*y,
#         'min':lambda x,y:x if x<y else y,
#         'max':lambda x,y:x if x>y else y
#     }
#     func=op[operation]
#     res=args[0]
#     for i in args:
#         if option.get('show_steps'):
#             print(res,i,operation,func(res,i))
#         res=func(res,i)
#     print(res)
# print(calculator(1,2,3,4,5,operation='mul',show_steps=True))




