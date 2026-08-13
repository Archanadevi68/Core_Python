cube = lambda x : x ** 3
# print(cube(10))

bigger = lambda x , y : x if x > y else y
# print(bigger(100,30))

def even(n):
    return n % 2 == 0
even1 = lambda n : n % 2 == 0
# print(even(10))
# print(even1(10))

fruits = [(100, "Banana"), (20, "Cherry"), (130, "Apple")]
fruits.sort(key = lambda x : x[0], reverse=True)
# print(fruits)
