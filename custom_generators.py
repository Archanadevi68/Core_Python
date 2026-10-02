def m1():
    val = 2
    while True:
        yield val
        val += 2
x = m1()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

def fib():
    a, b = 0, 1
    while True:
        yield a
        a , b = b , a + b

# obj = fib()
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

# l = [x*x for x in range(1, 11)]
# print(l)
# print(type(l))
# s = {x*x for x in range(1, 11)}
# print(s)
# print(type(s))
# d = {x : x*x for x in range(1, 11)}
# print(d)
# print(type(d))
# t = tuple(x for x in range(1, 11))
# print(t)
# print(type(t))
# g = (x for x in range(1, 11) if x % 2 == 0)
# for i in g:
#     print(i)
# print(max((x for x in range(1, 11) if x % 2 == 0)))
# print(min((x for x in range(1, 11) if x % 2 == 0)))
# print(sum((x for x in range(1, 11) if x % 2 == 0)))
import sys
l = [x for x in range(10000000)]
g = (x for x in range(10000000))
# print(sys.getsizeof(l))
# print(sys.getsizeof(g))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


l = [1,2,3,4]
g1 = (x for x in range(1, 3) for x in l if x % 2 == 0)
# for i in g1:
#     print(i)
g2 = (x if x % 2 == 0 else 0 for x in l)
for i in g2:
    print(i)