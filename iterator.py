# class A:
#     def __init__(self):
#         self.value=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value<=5:
#             n=self.value
#             self.value+=1
#             return n
#         else:
#             raise "stop Iterator"
# obj=A()
# for i in obj:
#     print(i)



class Fibinocci:
    def __init__(self):
        self.count=0
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<=10:
            x=self.a
            self.count += 1
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
            return x
        else:
            raise StopIteration

obj=Fibinocci()
for i in obj:
    print(i)


# class EvenNumbers:
#     def __init__(self):
#         self.start=0
#         self.count=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count<=10:
#             n = self.start
#             if n%2==0:
#                 self.x=n
#             self.start+=1
#             self.count+=1
#             return self.x
#         else:
#             raise StopIteration
# obj=EvenNumbers()
# for i in obj:
#       print(i)
#



