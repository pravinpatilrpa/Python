#List comprehension: make lists fast in one line.
#new_list = [expression for item in iterable if condition]

fruits = ["a","apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#/ gives decimals, // gives only whole numbers
print(5//2) #/ result is a floating point number
print(5/2)  #// result is an integer

def add(x, y):
    return x + y
def apply_func(func, a, b):
    return func(a, b)
print(apply_func(add, 3, 5))


def fun(*argv):
    for arg in argv:
        print(arg)
fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

