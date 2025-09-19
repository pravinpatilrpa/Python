def classes_objects():
    class Dog:
        def __init__(self,name,age):
            self.Name=name
            self.age=age
        
        def bark(self):
            return f"{self.name} says Woof!"
        
        def get_age(self):
            return self.age

    dog1=Dog("Buddy",3)
    print(dog1.bark())          #Buddy says Woof!
    print(f"{dog1.name} is {dog1.get_age()} years old.")  #Buddy is 3 years old.

classes_objects()

# def inheritance():
#     class Animal:
#         def __init__(self,name):
#             self.name=name
        
#         def speak(self):
#             return f"{self.name} makes a sound."

#     class Dog(Animal):
#         def speak(self):
#             return f"{self.name} says Woof!"

#     class Cat(Animal):
#         def speak(self):
#             return f"{self.name} says Meow!"

#     dog1=Dog("Buddy")
#     cat1=Cat("Whiskers")
#     print(dog1.speak())  #Buddy says Woof!
#     print(cat1.speak())  #Whiskers says Meow!
# inheritance()

# def polymorphism():
#     class Bird:
#         def speak(self):
#             return "Chirp Chirp!"

#     class Dog:
#         def speak(self):
#             return "Woof Woof!"

#     class Cat:
#         def speak(self):
#             return "Meow Meow!"

#     def animal_sound(animal):
#         print(animal.speak())

#     bird1=Bird()
#     dog1=Dog()
#     cat1=Cat()
#     animal_sound(bird1)  #Chirp Chirp!
#     animal_sound(dog1)   #Woof Woof!
#     animal_sound(cat1)   #Meow Meow! 
# polymorphism()

# def encapsulation():
#     class Person:
#         def __init__(self,name,age):
#             self.__name=name      #Private attribute
#             self.__age=age        #Private attribute
        
#         def get_name(self):
#             return self.__name
        
#         def set_name(self,name):
#             self.__name=name
        
#         def get_age(self):
#             return self.__age
        
#         def set_age(self,age):
#             if age>0:
#                 self.__age=age
#             else:
#                 print("Invalid age!")

#     person1=Person("Pravin",37)
#     print(person1.get_name())  #Pravin
#     print(person1.get_age())   #37
#     person1.set_age(38)
#     print(person1.get_age())   #38
#     person1.set_age(-5)        #Invalid age!
#     print(person1.get_age())   #38

# encapsulation()