def comments():
    # This is a single line comment
    print("Hello, World!")  # This prints Hello, World!
    """
    This is a multi-line comment
    You can write multiple lines here
    """
    print("Python is fun!")
comments()


def type_conversion():
    var1="123"
    var2=3.14
    var3=10
    var4=True
    print(type(var1),type(var2),type(var3),type(var4))  #<class 'str'> <class 'float'> <class 'int'> <class 'bool'>
    print(int(var1),float(var1),str(var1),bool(var1))   #123 123.0 123 True
    print(int(var2),float(var2),str(var2),bool(var2))   #3 3.14 3.14 True
    print(int(var3),float(var3),str(var3),bool(var3))   #10 10.0 10 True
    print(int(var4),float(var4),str(var4),bool(var4))   #1 1.0 True True

#type_conversion()

def user_input():
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old.")
    print("In 5 years, you will be",age+5,"years old.")

#user_input()

def variableType():
    var1="Welcome to Python \n"     #string
    print(2*var1)
    print(type(var1))
    var2=3.14                       #float
    print(type(var2))
    var3=10                         #integer
    print(type(var3)) 
    var4=True                       #boolean  
    print(type(var4))  
    var5=None                       #NoneType  
    print(type(var5))  
    var6=3+4j                       #complex number
    print(type(var6))           
    var7=b'Hello'                      #bytes
    print(type(var7))
    var8=bytearray(5)                   #bytearray
    print(type(var8))               
    var9=range(6)                       #range
    print(type(var9))
    var10=['apple','banana','cherry']   #list
    print(type(var10))
    var11=('apple','banana','cherry')   #tuple
    print(type(var11))
    var12={'name':'John','age':30}       #dictionary
    print(type(var12))
    var13={'apple','banana','cherry'}       #set
    print(type(var13))

#variableType()

def slicing():
    str1="Hello, welcome to Python programming."
    print(str1[0:5])          #Hello
    print(str1[7:14])         #welcome
    print(str1[:5])           #Hello
    print(str1[7:])           #welcome to Python programming.
    print(str1[0:5:2])      #Hlo
    print(str1[-11:-1])       #programming
    print(str1[-11:])         #programming.
    print(str1[:-12])       #Hello, welcome to Python programming    
    print(str1[-1:-11:-1])    #gnimmargorp
    print(str1[::-1])        #.gnimmargorp nohtyP ot emoclew ,olleH                   

#slicing()

def string_methods():
    str1="Hello, welcome to Python programming."
    print(str1.upper())          #HELLO, WELCOME TO PYTHON PROGRAMMING.
    print(str1.lower())          #hello, welcome to python programming.
    print(str1.capitalize())     #Hello, welcome to python programming.
    print(str1.title())          #Hello, Welcome To Python Programming.
    print(str1.strip('.'))       #Hello, welcome to Python programming
    print(str1.replace('o','0')) #Hell0, welc0me t0 Pyth0n pr0gramming.
    print(str1.split())          #['Hello,', 'welcome', 'to', 'Python', 'programming.']
    print(str1.find('Python'))   #18
    print(str1.index('welcome')) #7
    print(str1.count('o'))       #4
    print(str1.startswith('Hello')) #True
    print(str1.endswith('programming.')) #True

#string_methods()

def list_methods():
    list1=['apple','banana','cherry']
    print(list1)
    list1.append('orange')
    print(list1)                 #['apple', 'banana', 'cherry', 'orange']
    list1.insert(1,'kiwi')
    print(list1)                 #['apple', 'kiwi', 'banana', 'cherry', 'orange']
    list1.remove('banana')
    print(list1)                 #['apple', 'kiwi', 'cherry', 'orange']
    list1.pop()
    print(list1)                 #['apple', 'kiwi', 'cherry']
    list1.sort()
    print(list1)                 #['apple', 'cherry', 'kiwi']
    list1.reverse()
    print(list1)                 #['kiwi', 'cherry', 'apple']
    print(len(list1))            #3
    list2=['grape','melon']
    list1.extend(list2)
    print(list1)                 #['kiwi', 'cherry', 'apple', 'grape', 'melon']

#list_methods()

def tuple_methods():
    tuple1=('apple','banana','mango','mango')
    print(tuple1)          #('apple', 'banana', 'mango', 'mango')
    print(tuple1.count('mango'))    #2
    print(tuple1.index('mango'))    #2
    # Tuples are immutable, so we cannot add or remove elements
    # But we can convert it to a list and then back to a tuple
    list1=list(tuple1)
    list1.append('orange')
    tuple1=tuple(list1)
    print(tuple1)                 #('apple', 'banana', 'cherry', 'orange')

#tuple_methods()

def dict_methods():
    dict1={'name':'Pravin','age':37,'city':'Pune'}
    print(dict1)        #{'name': 'Pravin', 'age': 37, 'city': 'Pune'}            
    print(dict1['name'])    #Pravin
    dict1['age']=36      #Update age
    print(dict1)            #{'name': 'Pravin', 'age': 36, 'city': 'Pune'}
    dict1['job']='RPA'  #Add new key-value pair
    print(dict1)            #{'name': 'Pravin', 'age': 36, 'city': 'Pune', 'job': 'RPA'}
    dict1.pop('city')   #Remove key 'city'
    print(dict1)            #{'name': 'Pravin', 'age': 36, 'job': 'RPA'}                   
    print(len(dict1))      #3            
    print(dict1.keys())     #dict_keys(['name', 'age', 'job'])           
    print(dict1.values())   #dict_values(['Pravin', 36, 'RPA'])             
    print(dict1.items())    #dict_items([('name', 'Pravin'), ('age', 36), ('job', 'RPA')])          
    dict2={'country':'India','language':'English'}
    dict1.update(dict2)     #Merge dict2 into dict1
    print(dict1)            #{'name': 'Pravin', 'age': 36, 'job': 'RPA', 'country': 'India', 'language': 'English'}     

#dict_methods()

def set_methods():
    set1={'apple','banana','cherry',"mango"}
    print(set1)          #{'banana', 'cherry', 'apple'}
    set1.add('orange')
    print(set1)          #{'banana', 'cherry', 'orange', 'apple'}
    set1.remove('banana')
    print(set1)          #{'cherry', 'orange', 'apple'}
    set1.discard('grape') # No error if element not found
    print(set1)          #{'cherry', 'orange', 'apple'}
    print(len(set1))     #3
    set2={'kiwi','mango','apple'}
    print(set1.union(set2))        #{'kiwi', 'cherry', 'mango', 'orange', 'apple'}
    print(set1.intersection(set2)) #{'apple'}
    print(set1.difference(set2))   #{'cherry', 'orange'}
    print(set1.issubset(set2))     #False
    print(set1.issuperset(set2))   #False
    print(set1.isdisjoint(set2))   #False

#set_methods()


def arithmetic_operations():
    a=10
    b=3
    print("Addition:",a+b)            #13
    print("Subtraction:",a-b)         #7
    print("Multiplication:",a*b)      #30
    print("Division:",a/b)            #3.3333
    print("Floor Division:",a//b)     #3
    print("Modulus:",a%b)             #1
    print("Exponentiation:",a**b)     #1000
#arithmetic_operations()

def comparison_operations():
    a=10
    b=3
    print("Equal:",a==b)              #False
    print("Not Equal:",a!=b)          #True
    print("Greater than:",a>b)        #True
    print("Less than:",a<b)           #False
    print("Greater than or equal to:",a>=b) #True
    print("Less than or equal to:",a<=b)    #False

#comparison_operations()

def logical_operations():
    a=True
    b=False
    print("AND:",a and b)             #False
    print("OR:",a or b)               #True
    print("NOT a:",not a)             #False
    print("NOT b:",not b)             #True

#logical_operations()

def membership_operations():
    str1="Hello, welcome to Python programming."
    list1=['apple','banana','cherry']
    dict1={'name':'Pravin','age':37,'city':'Pune'}
    print('welcome' in str1)          #True
    print('kiwi' not in str1)         #True
    print('banana' in list1)          #True
    print('grape' not in list1)       #True
    print('name' in dict1)            #True
    print('country' not in dict1)     #True
#membership_operations()

def identity_operations():
    a=10
    b=10
    c=5
    print(a is b)                     #True
    print(a is not c)                 #True
    print(id(a),id(b),id(c))          #Same id for a and b, different for c
#identity_operations()

def operator_precedence():
    a=10
    b=5
    c=2
    result=a+b*c
    print("Result of a + b * c:",result)  #20
    result=(a+b)*c
    print("Result of (a + b) * c:",result) #30
    result=a**b+c
    print("Result of a ** b + c:",result)  #100002
    result=a**(b+c)
    print("Result of a ** (b + c):",result) #1000000000
#operator_precedence()

def formatted_strings():
    name="Pravin"
    age=37
    city="Pune"
    print("Hello, my name is {}. I am {} years old and I live in {}.".format(name,age,city))
    print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")
    print("Hello, my name is %s. I am %d years old and I live in %s." % (name,age,city))
#formatted_strings()

def escape_sequences():
    print("Hello,\nWelcome to Python programming.")   #New line
    print("Hello,\tWelcome to Python programming.")   #Tab space
    print("Hello,\\Welcome to Python programming.")   #Backslash
    print("He said, \"Python is awesome!\"")          #Double quote
    print('It\'s a beautiful day!')                    #Single quote
    print("C:\\Users\\Pravin\\Documents")             #File path
#escape_sequences()

def arithmetic_quiz():
    import random
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    answer=num1+num2
    user_answer=int(input(f"What is {num1} + {num2}? "))
    if user_answer==answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}.")

#arithmetic_quiz()

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))  #120

def fibonacci(n):
    a,b=0,1
    fib_sequence=[]
    for _ in range(n):
        fib_sequence.append(a)
        a,b=b,a+b
    return fib_sequence
print(fibonacci(10))  #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(29))  #True

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
print(gcd(56,98))  #14
def lcm(a,b):
    return abs(a*b)//gcd(a,b)  

print(lcm(4,5))    #20

def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))  #olleH

def count_vowels(s):
    vowels='aeiouAEIOU'
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
print(count_vowels("Hello World"))  #3

def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
print(is_palindrome("AA"))  #True

def sum_of_digits(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total
print(sum_of_digits(12345))  #15

def divide(a,b):
    if b==0:
        return "Error! Division by zero."
    return a/b
print(divide(10,2))  #5.0

def power(a,b):
    return a**b
print(power(2,3))  #8

def modulus(a,b):
    return a%b
print(modulus(10,3))  #1

def floor_division(a,b):
    if b==0:
        return "Error! Division by zero."
    return a//b
print(floor_division(10,3))  #3

def square(a):
    return a*a
print(square(4))  #16

def cube(a):
    return a*a*a
print(cube(3))  #27

def sqrt(a):
    if a<0:
        return "Error! Square root of negative number."
    return a**0.5
print(sqrt(16))  #4.0

def absolute(a):
    return abs(a)
print(absolute(-5))  #5

def average(a,b):
    return (a+b)/2
print(average(10,20))  #15.0

def percentage(part,total):
    if total==0:
        return "Error! Total cannot be zero."
    return (part/total)*100
print(percentage(50,200))  #25.0

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))  #120


def conditional_statements():
    age=int(input("Enter your age: "))
    if age<18:
        print("You are a minor.")
    elif 18<=age<65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
#conditional_statements()

def loops():
    print("Using for loop:")
    for i in range(5):
        print(i)  #0 1 2 3 4
    print("Using while loop:")
    count=0
    while count<5:
        print(count)  #0 1 2 3 4
        count+=1
#loops()

def nested_loops():
    for i in range(1,4):
        for j in range(1,4):
            print(f"i={i}, j={j}")
nested_loops()

def break_continue():
    print("Using break:")
    for i in range(10):
        if i==5:
            break
        print(i)  #0 1 2 3 4
    print("Using continue:")
    for i in range(10):
        if i%2==0:
            continue
        print(i)  #1 3 5 7 9
break_continue()

def list_comprehensions():
    squares=[x**2 for x in range(10)]
    print(squares)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    even_squares=[x**2 for x in range(10) if x%2==0]
    print(even_squares)  #[0, 4, 16, 36, 64]
list_comprehensions()