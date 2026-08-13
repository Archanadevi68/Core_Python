# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
# n=int(input())
# pp=n-1
# # c=0
# while True:
#     if is_prime(pp):
#         break
#     pp-=1
# np=n+1
# # c=0
# while True:
#     if is_prime(np):
#         break
#     np+=1
# dpp=n-pp
# dnp=np-n
# if dpp<dnp:
#     print("the nearest prime is :",pp)
# elif dnp<dpp:
#     print("the nearest prime is:",np)
# else:
#     print("the nearest prime is :",pp,np)
#
#
#
#
#
#
#
# n=int(input())
# n1=int(input())
# c=0
# if n<n1:
#     for i in range(n,n1+1):
#         c+=1
#         if c>1:
#             print(',',end='')
#         if i>=0:
#             print(f"5*{i}",end='')
#         else:
#             print(f"5*({i})",end='')
# else:
#     for i in range(n,n1-1,-1):
#         c+=1
#         if c>1:
#             print(',',end='')
#         if i>=0:
#             print(f"5*{i}",end='')
#         else:
#             print(f"5*({i})",end='')
from operator import truediv


# n=float(input())
# n1=float(input())
# c=0
# # i=n
# while n<=n1:
#     c+=1
#     if c>1:
#         print(',',end='')
#     print(f"{n}^2",end='')
#     n=n+0.2
#     n=round(n,1)
# print('.')



# def isprime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
# n=int(input())
# # n1=int(input())
# for i in range(1,n+1):
#      if n%i==0 and isprime(i):
#         print(i,end=' ')

# import math
# n=int(input())
# if int(math.sqrt(n)**2)==n:
#     print("perfect squre")
# else:
#     print("not")

# n=int(input())
# print("Sum of 'n' Natural Numbers is ",end='')
# c=0
# for i in range(1,n+1):
#     if i==n:
#         print(i,end='')
#     else:
#         print(i,end='+')
#     c+=i
# print(f"={c}.")


# def is_palim(n):
#     t=n
#     rev=0
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n//=10
#     if rev==t:
#         return True
#     return False
#
# n=int(input())
# n1=int(input())
# c,sum=0,0
# print(f"Sum of Alternative palindrome numbers between the {n} and {n1} is ", end='')
# for i in range(n,n1+1):
#     if is_palim(i):
#         c+=1
#         if c%2==1:
#             sum+=i
#             if c > 1:
#                 print('+', end='')
#             print(i,end='')
# if c==0:
#     print('no palimdrome values')
# else:
#     print(f"= {sum}.")




# def is_arm(n):
#     c=0
#     t=n
#     while t>0:
#         r=t%10
#         c+=1
#         t//=10
#     t=n
#     rev=0
#     while t>0:
#         r=t%10
#         rev=(r**c)+rev
#         t//=10
#     if rev==n:
#         return True
#     return False
# n=int(input())
# if is_arm(n):
#     print('armstrong number')


# n=int(input())
# if n%4==0 or n%400==0 and n%100!=0:
#     print("leap")
# else:
#     print("not")


# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
# n=int(input())
# pp=n-1
# while pp>0:
#     if is_prime(pp):
#         break
#     pp-=1
# print(pp)
# np=n+1
# while np>0:
#     if is_prime(np):
#         break
#     np+=1
# print(np)
#
# dpp=n-pp
# dnp=np-n
# if dnp>dpp:
#     print(pp)
# elif dnp<dpp:
#     print(np)
# else:
#     print(pp,np)




n=int(input())
n1=int(input())
c=0
for i in range(n-1,0,-1):
    temp=i
    while temp>0:
        if temp%10==n1:
            c+=1
            print(i)
            break
        temp//=10
    if c==1:
        break

