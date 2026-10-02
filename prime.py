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




# n=int(input())
# n1=int(input())
# c=0
# for i in range(n-1,0,-1):
#     temp=i
#     while temp>0:
#         if temp%10==n1:
#             c+=1
#             print(i)
#             break
#         temp//=10
#     if c==1:
#         break




# r=int(input())
# c=int(input())
# s=1
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print(s,end=' ')
#     s+=1
#     print()




# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
# def n_prime(n):
#     x=2
#     c=0
#     while True:
#         if is_prime(x):
#             c+=1
#             if c==n:
#                 return x
#         x+=1
# n=int(input())
# for i in range(1,n+1):
#     d=i
#     for j in range(1,i+1):
#         print(n_prime(d),end=' ')
#         d=d+(n-1)
#     print()
#


# def is_check(list,c):
#     for i in range(0,len(list)):
#         if list[i]==c:
#             return True
#     return False
# def find_min(list):
#     for i in range(0,len(list)):
#         if i==0:
#             a=l[i]
#         if a>l[i]:
#             a=l[i]
#     return a
#
# l=list(map(int,input().split()))
# min=find_min(l)
# x=min+1
# k=0
# while k<4:
#     if not is_check(l,x):
#         print(x,end=' ')
#         k+=1
#     x+=1



# def mini(l):
#     a = l[0]
#     for i in range(1, len(l)):
#         if a > l[i]:
#             a = l[i]
#     return a
#
#
# l = list(map(int, input().split()))
#
# x = mini(l)
# s = len(l)
#
# while s > 0:
#     for i in range(len(l)):
#         if l[i] == x:
#             print(x, end=' ')
#             s -= 1
#     x += 1



# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if n%2==1:
#             if i==n-i+1 or j==n-j+1:
#                 print("*",end=' ')
#             else:
#                 print(" ",end=' ')
#         else:
#             if i==n-i or i==n-i+2 or j==n-j or j==n-j+2:
#                 print("*",end=' ')
#             else:
#                 print(" ",end=' ')
#     print()


# a=int(input())
# d=int(input())
# n=int(input())
# c=0
# for i in range(1,n+1):
#     c+=1
#     if c>1:
#         print(',',end='')
#     print(a,end='')
#     a+=d

# f=int(input())
# s=int(input())
# t=int(input())
# if f<s and f<t:
#     min=f
# elif s<f and s<t:
#     min=s
# else:
#     min=t
# i=min
# while i>=1:
#     if f%i==0 and s%i==0 and t%i==0:
#         print(i)
#         break
#     i-=1


# a=int(input())
# d=int(input())
# n=int(input())
# for i in range(n):
#     ap=a+(i*d)
#     hp=1/ap
#     print(f"{hp:.2f}")

# n=int(input())
# n1=int(input())
# max=n if n>n1 else n1
# i=max
# while True:
#     if i%n==0 and i%n1==0:
#         print(i)
#         break
#     i+=max

# n=int(input())
# n1=int(input())
# n3=int(input())
# for i in range(n3):
#     print(n,end=' ')
#     n=n*n1


# n=int(input())
# a=0
# b=1
# d=0
# for i in range(1,n*2):
#     d+=1
#     if d%2==1:
#         print(a,end=' ')
#     c=a+b
#     a=b
#     b=c


# n=int(input())
# s=1
# sum=0
# for i in range(1,n+1):
#     s=s*i
#     sum+=s
#     print(s,end=' ')



# n=int(input())
# def is_arm(n):
#     t=n
#     c=0
#     while t>0:
#         r=t%10
#         c+=1
#         t//=10
#     t=n
#     res=0
#     while t>0:
#         r=t%10
#         res+=r**c
#         t//=10
#     if res==n:
#         return True
#     return False
# if is_arm(n):
#     print("armstron number")
# else:
#     print("not")

#
# t=n
# rev=0
# while t>0:
#     r=t%10
#     rev=rev*10+r
#     t//=10
# if rev==n:
#     print("palindrome")
# else:
#     print("not")




# n=int(input())
# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
# # def reverse(n):
# #     rev=0
# #     t=n
# #     while t>0:
# #         r=t%10
# #         rev=rev*10+r
# #         t//=10
# #     return rev
# # if is_prime(n) and is_prime(reverse(n)):
# #     print("its circular prime")
# # else:
# #     print("not")
# #
# # t=n
# # count=0
# # while t>0:
# #     count+=1
# #     t//=10
# # pc=0
# # for i in range(count):
# #     if is_prime(n):
# #         pc+=1
# #     r=n%10
# #     n=r*(10**(count-1))+n//10
# t=n
# count=0
# while t>0:
#     count+=1
#     t//=10
# pc=0
# for i in range(count):
#     if is_prime(n):
#         pc+=1
#         r=n%10
#         n=r*(10**(count-1))+n//10
#
# if pc==count:
#     print("circular")
# else:
#     print("not")

# count=0
# t=n
# while t<0:
#     count+=1
#     t//=10
# pc=0
# for i in range(1,count):
#     if is_prime(n):
#         pc+=1
#         r=n%10
#         n=r*(10**(count-1))+n//10
#
# if pc==count:
#     print("circular")
# else:
#     print("not")
# # def is_prime(n):
# #     fc=0
# #     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
# def n_prime(n):
#     x=2
#     c=0
#     while True:
#         if is_prime(x):
#             c+=1
#             if c==n:
#                 return x
#         x+=1
# n=int(input())
# for i in range(1,n+1):
#     d=i
#     for j in range(1,i+1):
#         print(n_prime(d),end=' ')
#         d=d+(n-1)
#     print()

# def n_prime(n):
#     c=2
#     x=0
#     while True:
#         if is_prime(c):
#             x+=1
#             if x==n:
#                 return c
#         c+=1
# n=int(input())
# for i in range(1,n+1):
#     d=i
#     for j in range(1,i+1):
#         print(n_prime(d),end=' ')
#         d=d+(n-1)
#     print()



# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     p=2
#     a=0
#     b=1
#     c=0
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             if c%2==0:
#                 while True:
#                     fc=0
#                     for k in range(1,p+1):
#                         if p%k==0:
#                             fc+=1
#                     if fc==2:
#                         print(p,end=' ')
#                         p+=1
#                         break
#                     p+=1
#             else:
#                 print(a,end=' ')
#                 d=a+b
#                 a=b
#                 b=d
#             c+=1
#         print()




