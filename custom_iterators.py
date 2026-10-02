# class A:
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= 5:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration
# obj = A()
# print(type(obj))
# for i in obj:
#     print(i)


# class Py21:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         val = self.current
#         self.current += 1
#         return val
# ten = Py21(1, 10)
# # for i in ten:
# #     print(i)
# #
# fifty = Py21(30 , 50)
# for i in fifty:
#     print(i)

# class Evens:
#     def __init__(self, end):
#         self.start = 2
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#         val = self.start
#         self.start += 2
#         return val
#
# ten = Evens(50)
# for i in ten:
#     print(i)


class Fibonacci:
    def __init__(self, n):
        self.count = 1
        self.a , self. b = 0, 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            val = self.a
            self.a , self.b = self.b , self.a + self.b
            self.count += 1
            return val
        else:
            raise StopIteration
five = Fibonacci(5)
for i in five:
    print(i)