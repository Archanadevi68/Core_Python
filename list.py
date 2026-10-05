# l = [10,20,30,60,50,10,20,50,30,40]
# d = {}
# for i in l:
#     d[i] = d.get(i,0)+1
# for i,j in d.items():
#     print(i,j)



# first question.
# l=[20,30,40,50,60]
# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         sum=0
#         sl=l[i:j+1]
#         for k in range(0,len(sl)):
#             sum+=sl[k]
#         print(sl,sum)

# second question
# l=[10,20,30,40,50,60]
# target=int(input())
# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         sum=0
#         sl=l[i:j+1]
#         for k in range(0,len(sl)):
#             sum+=sl[k]
#         if target==sum:
#             print(sl)


# third question.
# def ispalim(n):
#     rev=0
#     t=n
#     while t>0:
#         r=t%10
#         rev=rev*10+r
#         t//=10
#     if rev==n:
#         return True
#     return False
# l=[10,35,34,45,64,89,90]
# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         sum=0
#         sl=l[i:j+1]
#         for k in range(0,len(sl)):
#             sum+=sl[k]
#         if ispalim(sum):
#             print(sl,sum)
#


# fourth question.
# def ispalim(n):
#     rev=0
#     t=n
#     while t>0:
#         r=t%10
#         rev=rev*10+r
#         t//=10
#     if rev==n:
#         return True
#     return False
#
# l=[1,2,3,2,4,5,6,7,99,88,3,31,45]
# d=0
# c=1
# m=0
# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         sum=0
#         sl=l[i:j+1]
#         for k in range(0,len(sl)):
#             sum+=sl[k]
#             c+=1
#             if ispalim(sum) and d<c:
#                     d = c
#                     m = sl
# print(m,"->",sum)
#

# fifth question.
# target=int(input())
# l=[10,20,30,40,50,60,70,80,90]
# c=3
# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         r=0
#         sum=0
#         sl=l[i:j+1]
#         for k in range(0,len(sl)):
#             r+=1
#             sum+=sl[k]
#         if r==c and target==sum:
#             print(sl)




# l=list(map(int,input().split()))
# max1=float('-inf')
# max2=float('-inf')
# max3=float('-inf')
# max4=float('-inf')
# for i in range(0,len(l)):
#     if l[i]>max1:
#         max4=max3
#         max3=max2
#         max2=max1
#         max1=l[i]
#     elif l[i]>max4 and l[i]!=max2 and l[i]!=max1 and l[i]!=max3:
#         max4=l[i]
# print(max4,max3,max2,max1)


# def mini(l):
#     a=float("inf")
#     for i in range(0,len(l)):
#         if l[i]<a:
#             a=l[i]
#     return a
# def maxi(l):
#     a=float('-inf')
#     for i in range(0,len(l)):
#         if l[i]>a:
#             a=l[i]
#     return a
# def check(l,n):
#     for i in range(0,len(l)):
#         if n==l[i]:
#            return True
#     return False
# l=list(map(int,input().split()))
# m=mini(l)
# ma=maxi(l)
# x=m+1
# s=0
# while s<ma:
#     if not check(l,x):
#         print(x,end=' ')
#         s+=1
#     x+=1



# l=list(map(int,input().split()))
# n=int(input())
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==n:
#             print(l[i],l[j])

# def mini(l):
#     a=float('inf')
#     for i in range(0,len(l)):
#         if l[i]<a:
#             a=l[i]
#     return a
#
# def check(l,n):
#     for i in range(0,len(l)):
#         if n in l:
#             return True
#     return False
# m=mini(l)
# x=m
# c=0
# while c<len(l):
#     if check(l,x):
#         print(x,end=' ')
#         c+=1
#     x+=1


# def isprime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
#
# for i in range(0,len(l)):
#     a=l[i]
#     a=abs(a)
#     np=a+1
#     while True:
#         if isprime(np):
#             break
#         np+=1
#     print(np,end=' ')

# for i in range(0,len(l)):
#     oc=0
#     bc=0
#     for j in range(0,len(l)):
#         if l[i]==l[j]:
#             oc+=1
#     for j in range(0,i+1):
#         if l[i]==l[j]:
#             bc+=1
#     if bc==1:
#         print(l[i],"->",oc)

# l=list(map(int,input().split()))
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.append(i)
# l1.reverse()
# j=0
# for i in range(0,len(l)):
#     if l[i]%2==0:
#         l[i]=l1[j]
#         j+=1
# print(l)
#



# n=int(input())
# t=n
# l=[]
# while t>0:
#     r=t%10
#     l.append(r)
#     t//=10
# l.reverse()
# while l[-1]<n:
#     s=0
#     for i in l[-len(str(n)):]:
#         s+=i
#     l.append(s)

# while l[-1]
# if l[-1]==n:
#     print("Keith NUmber")
# else:
#     print("not")

# l=list(map(int,input().split()))
#
# s=set()
#
# for i in l:
#     c=0
#     for j in l:
#         if i==j:
#             c+=1
#
#     if i==c and i not in s:
#         print(i,"lucky")
#         s.add(i)


# l=list(map(int,input().split()))
# s=set()
# for i in l:
#     c=0
#     for j in l:
#         if i==j:
#             c+=1
#     if i==c:
#         if i not in s:
#             print(i,"lucky number")
#         s.add(i)


# l=list(map(int,input().split()))
# n=int(input())
# d=0
# for i in range(0,len(l)):
#     for j in range(i,len(l)):
#         c=0
#         s=l[i:j+1]
#         for k in s:
#             c+=k
#         if c==n:
#             d+=1
#             for x in s:
#                 print(x,end=' ')
#             print()
#
# if d==0:
#     print("No Sub Arrays Found")

# l=list(map(int,input().split()))
# for i in range(0,len(l)):
#     c=0
#     for j in range(0,len(l)):
#         if l[i]==l[j]:
#             c+=1
#     if c==1:
#         print(l[i])

#

# write a program to print the even numbers in the given list.
# r=int(input())
# n1=[]
# for i in range(0,r):
#     n1.append(list(map(int,input().split())))
# c=len(n1[0])
# for i in range(0,r):
#     for j in range(0,c):
#         s=n1[i][j]
#         if s%2==0:
#             print(n1[i][j],end=' ')
#     print()



# write a program to print the prime number values in the nested list.
# def isprime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
#
# r=int(input())
# l1=[]
# for i in range(0,r):
#     l1.append(list(map(int,input().split())))
# c=len(l1[0])
# for i in range(0,r):
#     for j in range(0,c):
#         s=l1[i][j]
#         if isprime(s):
#             print(l1[i][j],end=' ')
#     print()
#
#


# write a programe to print the sum of all elements in the nested list.
# r=int(input())
# l1=[]
# s=0
# for i in range(0,r):
#     l1.append(list(map(int,input().split())))
# c=len(l1[0])
# for i in range(0,r):
#     for j in range(0,c):
#        s+=l1[i][j]
# print(s)
#


# write a programe to print the first and second maximum elements in the given nested list.
# r=int(input())
# l1=[]
# for i in range(0,r):
#     l1.append(list(map(int,input().split())))
# c=len(l1[0])
# f=float('-inf')
# s=float('-inf')
# for i in range(0,r):
#     for j in range(0,c):
#         if l1[i][j]>f:
#             s=f
#             f=l1[i][j]
#         elif l1[i][j]>s and l1[i][j]<f:
#             s=l1[i][j]
# print(f,s)
#


# write a programe to prite the sum of each inner list separetly.
# r=int(input())
# l1=[]
# for i in range(0,r):
#     l1.append(list(map(int,input().split())))
# c=len(l1[0])
# for i in range(0,r):
#     s=0
#     for j in range(0,c):
#         print(l1[i][j],end=' ')
#         s+=l1[i][j]
#     print("->",s,end=' ')
#     print()

# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# m=float("-inf")
# for i in range(0,len(l)):
#     if l[i][i]>m:
#         m=l[i][i]
# print(m)


# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# sp=0
# ss=0
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#         if i==j:
#             sp+=l[i][j]
#         if i==r-1:
#             ss+=l[i][j]
#
# print(sp,ss)



# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=int(input())
#
# for
#



# def isprime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
#     return False
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# for i in range(0,len(l)):
#     for j in range(0,c):
#         s=l[i][j]
#         if isprime(s):
#             print(s,end='')
#         print()



# sum of all elements in the nested list.
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# s=0
# for i in range(0,len(l)):
#     for j in range(0,c):
#         s+=l[i][j]
# print(s)


# first and secod maximum elements in the given nested list.
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# f=float("-inf")
# s=float("-inf")
# for i in range(0,len(l)):
#     for j in range(0,c):
#         a=l[i][j]
#         if a>f:
#             s=f
#             f=a
#         elif s<a and f>a:
#             s=a
# # print(f,s)



# write a programe to print the sum of each inner list in the separetly.
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# d=0
# for i in range(0,len(l)):
#     for j in range(0,c):
#         s=l[i][j]
#         d+=s
#     print(d)


# column wise printing the sum of nested list in the given list.
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# for i in range(0,c):
#     d = 0
#     for j in range(0,len(l)):
#         s=l[j][i]
#         d+=s
#     print(d)


# sum of primary and seccondary diagonal elements in the nested list.

# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# f=0
# s=0
# for i in range(0,len(l)):
#     for j in range(0,c):
#         if i==j:
#             f+=l[i][j]
#         if i+j==c-1:
#             s+=l[i][j]
# print(f,s)


# match question.
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# print("Total Score of each match")
# for i in range(0,len(l)):
#     d = 0
#     for j in range(0,c):
#         s=l[i][j]
#         d+=s
#     print(f"m{i+1} Total ={d}")
#
# print("man of the match")
# for i in range(0,len(l)):
#     x =0
#     m=0
#     for j in range(0,c):
#         s=l[i][j]
#         if x<s:
#             x=s
#             m=j
#     print(f"mm {i+1} is p{m+1}")


# neighbor elements.
# r=int(input())
# l=[]
# for i in range(0,r):
#     l.append(list(map(int,input().split())))
# c=len(l[0])
# for i in range(0,len(l)):
#     for j in range(0,c):
#         print(l[i][j],end='-->')
#         if i!=0:
#             print(l[i-1][j],end=' ')
#         if j!=c-1:
#             print(l[i-1][j+1],end=' ')
#         if i!=len(l)-1:
#             print(l[i+1][j],end=' ')
#         if j!=0:
#             print(l[i][j-1],end=' ')
#         print()



# bubble sort.
# l=list(map(int,input().split()))
# for i in range(0,len(l)):
#     c=0
#     for j in range(0,len(l)-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#             c+=1
#     if c==0:
#         break
# print(l)

# insection sort.
# l=list(map(int,input().split(',')))
# for i in range(1,len(l)):
#     for j in range(i,0,-1):
#         if l[j-1]>l[j]:
#             l[j-1],l[j]=l[j],l[j-1]
#         else:
#             break
# print(l)

# selection sort.
l=list(map(int,input().split(',')))
for i in range(0,len(l)-1):
    k=0
    for j in range(1,len(l)-i):
        if l[j]>l[k]:
            k=j
            print(l)
    l[k],l[len(l)-i-1]=l[len(l)-i-1],l[k]
