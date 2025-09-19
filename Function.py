def greet(name):
    return f"Hello, {name}!"
print(greet("Pravin"))  #Hello, Pravin!

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))  #120


def outer_function():
    x=2
    def inner_function():
        x=3
        print("Inner x:",x)  #3
    inner_function()
    print("Outer x:",x)      #2

outer_function()

def global_variable():
    global x
    x=5
    def modify_global():
        global x
        x=10
        print("Inside function, x:",x)  #10
    modify_global()
    print("Outside function, x:",x)     #10
global_variable()

def lambda_functions():
    add=lambda a,b:a+b
    print(add(5,3))  #8
    square=lambda x:x**2
    print(square(4))  #16
    even_numbers=list(filter(lambda x:x%2==0,range(10)))
    print(even_numbers)  #[0, 2, 4, 6, 8]
lambda_functions()


def file_handling():
    # Writing to a file
    with open('example.txt','w') as file:
        file.write("Hello, World!\n")
        file.write("Welcome to Python file handling.\n")
    
    # Reading from a file
    with open('example.txt','r') as file:
        content=file.read()
        print(content)
    
    # Appending to a file
    with open('example.txt','a') as file:
        file.write("This is an appended line.\n")
    
    # Reading line by line
    with open('example.txt','r') as file:
        for line in file:
            print(line.strip())
file_handling()

def modules_imports():
    import math
    print("Square root of 16 is",math.sqrt(16))  #4.0
    print("Value of pi is",math.pi)               #3.141592653589793

    from random import randint
    print("Random integer between 1 and 10 is",randint(1,10))

    import datetime
    now=datetime.datetime.now()
    print("Current date and time is",now)

    import os
    print("Current working directory is",os.getcwd())

modules_imports()

def list_vs_tuple():
    my_list=[1,2,3]
    my_tuple=(1,2,3)
    print("Original list:",my_list)      #[1, 2, 3]
    my_list[0]=10
    print("Modified list:",my_list)      #[10, 2, 3]
    print("Original tuple:",my_tuple)     #(1, 2, 3)
    try:
        my_tuple[0]=10
    except Exception as e:
        print("Error:",e)  #Error: 'tuple' object does not support item assignment  
list_vs_tuple()

def shallow_vs_deep_copy():
    import copy
    original_list=[[1,2,3],[4,5,6]]
    shallow_copied_list=copy.copy(original_list)
    deep_copied_list=copy.deepcopy(original_list)

    original_list[0][0]=10
    print("Original list:",original_list)            #[[10, 2, 3], [4, 5, 6]]
    print("Shallow copied list:",shallow_copied_list) #[[10, 2, 3], [4, 5, 6]]
    print("Deep copied list:",deep_copied_list)       #[[1, 2, 3], [4, 5, 6]]
shallow_vs_deep_copy()

def args_kwargs():
    def display_info(*args,**kwargs):
        print("Positional arguments:",args)
        print("Keyword arguments:",kwargs)

    display_info(1,2,3,name="Pravin",age=37)
    #Positional arguments: (1, 2, 3)
    #Keyword arguments: {'name': 'Pravin', 'age': 37}
args_kwargs()

def zip_enumerate():
    list1=['a','b','c','d']
    list2=[1,2,3,4]
    zipped=zip(list1,list2)
    print("Zipped list:",list(zipped))  #[('a', 1), ('b', 2), ('c', 3)]

    for index,value in enumerate(list1):
        print(f"Index: {index}, Value: {value}")
    #Index: 0, Value: a
    #Index: 1, Value: b
    #Index: 2, Value: c
zip_enumerate()