import numpy as np
def Addition_array():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    print("Numpy array addition result:", c)
    return c
Addition_array()

list = [1, 2, 3, 4, 5]
for x in list:
    print(x)
def Addition_list():
    result = [x + 10 for x in list]
    print("List addition result:", result)
    return result
Addition_list()

dic = {'name':'pravin','age':37}
for key in dic:
    print('Key:',key)
for d in dic.values():
    print('Values:',d)
for k,v in dic.items():
    print('key:',k,'values:',v)

distances =[100,200,300]
times = [5,10,12]
speed = []
for i in range(len(distances)):
    speed.append(distances[i]/times[i])
print(speed)

#Vectorized Operations: Offers fast operations over entire arrays, avoiding slow Python loops
s = [d/t for d,t in zip(distances,times)]
print(s)
print(sum(d/t for d,t in zip(distances,times)))

