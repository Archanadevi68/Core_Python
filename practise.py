# 1.l=[('archana',95),('arjun',95),('priya',80),('trisha',70)]
# print(list(sorted(l,key=lambda x:(-x[1],x[0]))))

# 2.l=['archana','arjun','anand devara','pooja','rajuwilloms']
# print(sorted(l,key=lambda x:(len(x),x)))

# 3.from functools import reduce
# l=[2,4,5,10,4,2,8,9,10]
# res=map(lambda x:x+5,filter(lambda x:x%2==0 and x%5==0,l))
# print(reduce(lambda x,y:x+y,res))

# 4.from functools import reduce
# l=[2,3,4,5,6,7,8,9,10]
# res=sorted(map(lambda x:x+3,filter(lambda x:x%2==0 and x%4!=0,l)),reverse=True)
# print(res)
# print(reduce(lambda x,y:x*y,res))

# 5.from functools import reduce
# l=['monkey','buffalo','pig','honey','malayalam','rever','eagle']
# res=sorted(map(lambda x:x.lower(),filter(lambda x:x[0].lower()==x[-1].lower(),l)),key=lambda x:(x[-1],len(x)))
# print(reduce(lambda x,y:x+' '+y,res))

# 6.from functools import reduce
# l=[
#     {'type':'credit','amount':1000},
#     {'type':'debit','amount':500},
#     {'type':'credit','amount':2000}
#     ]
# res=filter(lambda x:x['type']=='credit',l)
# bonus=map(lambda x:{'type':x['type'],'amount':int(x['amount']+(x['amount']*5)/100)},res)
# res2=sorted(bonus,key=lambda x:x['amount'],reverse=True)
# print(res2)
# print(reduce(lambda x,y:x['amount']+y['amount'],res2))

# 7.def apply(a,b,op):
#     return op(a,b)
# print(apply(10,20,lambda x,y:x+y))
# print(apply(50,20,lambda x,y:x-y))
# print(apply(2,5,lambda x,y:x*y))

# 8.def greeting(name,prefix='Hello',formatter=lambda x:x):
#     greet=prefix+' '+name
#     return formatter(greet)
# print(greeting('Archana',formatter=str.upper))
#

# 9.l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(list(map(lambda x:x**2,filter(lambda x:x%3==0,l))))

# 10.double=lambda x:x**2
# triple=lambda x:x**3
# quadruple=lambda x:x**4
# l=[double,triple,quadruple]
# def apply(funcs,value):
#     for func in funcs:
#         print(func(value))
# apply(l,2)

#11. from functools import reduce
# def average(**scores):
#     for key,value in scores.items():
#         print(key,value)
#     total=reduce(lambda x,y:x+y,scores.values())
#     return total/len(scores)
# print(average(m=90,e=80,s=30,h=60,so=50))
#

# 12.l=[
#     {'name':'archana','score':90},
#     {'name':'teju','score':80},
#     {'name':'arjun','score':90},
#     {'name':'krishna','score':88}]
# res=filter(lambda x:x['score']>=60,l)
# res2=map(lambda x:{**x,'grade':'pass'},res)
# print(sorted(res2,
#              key=lambda x:x['score'],
#              reverse=True))

# 13.l=[('archana',90),('arjun',88),('teju',95),('krishna',77)]
# d={
#     'name':lambda x:x[0],
#     'score':lambda x:x[1],
#     'length':lambda x:len(x[0])}
# c=input()
# if c in d:
#     res=sorted(l,key=d[c])
#     print(res)


# def calculator(*args,operation='add',**options):
#     op={
#         'add':lambda x,y:x+y,
#         'sub':lambda x,y:x-y,
#         'mul':lambda x,y:x*y,
#         'min':lambda x,y:x if x<y else y,
#         'max':lambda x,y:x if x>y else y
# }
#     func=op[operation]
#     res=args[0]
#     for i in args:
#         if options.get('show_steps'):
#             print(res,i,operation,func(res,i))
#         res=func(res,i)
#     print(res)
# calculator(1,2,3,4,5,show_steps=True)

l=[1,2,3,4,5,6,7,8,9,10]
r=map(lambda x)



















