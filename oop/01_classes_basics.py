# class Student:
#     name="roman"
# s1=Student()
# print(s1.name)



# class Car:
#     brand="BMW"
#     color="blue"
# car1=Car()
# print(car1.color)
# print(car1.brand)


#/////////////////////////////
#constructor=__init__ fn execute when obj is created.  

# class Student:

#     def __init__(self):
#         print("Constructor called")


# s1 = Student()

# class Student:
#     def __init__(self,name,umer):
#         self.name=name
#         self.age=umer

#         print(self.name)
#         print(self.age)

# s1=Student("roman",19)
# s2=Student("karan",22)
# mportant Difference
# Local Variable
# name
# temporary
# exists only inside function
# deleted after function ends
# Instance Variable
# self.name
# stored in object
# accessible everywhere through object
# survives after constructor ends
# Think of a constructor like setting up a new phone.

# When you buy a phone:

# language is set
# date/time configured
# apps initialized

# Same with objects:

# Constructor prepares object before use.
# Constructor = automatic setup function for objects.

#method are nothing but a function on classes

# class Student:
#     college_name="swastik"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print("welcome", self.name )

#     def showage(self):
#         print(self.age)

# s=Student("roman",22)
# s1=Student("bipsan",24)
# s2=Student("salan",25)

# s.show()
# s.showage()
# s1.show()

    # /////////////   /////////   ////////    /////// //////

#     # @staticmethod
# class Student():
#     @staticmethod
#     def hello():
#       print("hello")

# Student.hello()

# /////// ////    /// ///
# Simple meaning of static method:

# We can call a function directly using the class name without creating an object.

# Example:

# class Student:

#     @staticmethod
#     def hello():
#         print("hello")

# Student.hello()


# ////////    //////  /////   /////   //////
# abstraction= hiding implementation details of class and showing ony essential feature to  eg : car engine unnecesasary hiding showing only necesary

# ////////    /// //  /   /   /   /   /   /   /   /
# encapsulation= wrapping data into a single unit called class

# # //////  /// /   /   /   //  //  /   /   /   /   /
# class Student:
#     def __init__(self,name):
#         self.name=name

# s= Student("roman")
# # del s
# print(s.name)

# //////  //////  /////// //////  //////

# private method __ used for hiding under class ie acc passwords÷

# class Account:
#     def __init__(self, acc_name ,acc_pwd):

#         self.acc_name=acc_name 
#         self.__acc_pwd=acc_pwd

#     def showpw(self):
#         return(self.__acc_pwd)


# acc1=Account("roman",232343)
# print(acc1.showpw())
# print(acc1.acc_name)

# //////  //////  /////// ////////    ////////

# class Car:
#     car_color="red"
#     @staticmethod
#     def start():
#         print("car has been started")
#     @staticmethod
#     def stop():
#         print("stoped")


# class Toyato(Car):
#     @staticmethod
#     def show(name):
#         print("car model is ",name)
        
# Toyato.show("harry")
# Toyato.start()

# ////////    //////  ////    /////   /////
# self.name = name
# current_object.name = passed_value
# /////// ////////    /////// ///////
# single inheritance
# class Car:
#     car_color="red"

    
#     def start(self):
#         print("car has been started")
#         print(self.name)

#     @staticmethod
#     def stop():
#         print("stoped")

# class toyato(Car):
#     def __init__(self,name):
#         self.name=name

# s1=toyato("sx")
# s2=toyato("ex")
# s1.start()
# ////////    ////////    /   ////    //  /   /   /   /   /   /   /   /   /   /
# multilevel=Grandparent → Parent → Child
# class Animal:

#     def eat(self):
#         print("Animal can eat")


# class Dog(Animal):

#     def bark(self):
#         print("Dog barks")


# class Puppy(Dog):

#     def weep(self):
#         print("Puppy weeps")
# p1 = Puppy()

# p1.eat()
# p1.bark()
# p1.weep()
# class Car:

#     def start(self):
#         print("Car started")


# class Toyota(Car):

#     def model(self):
#         print("Toyota Supra")


# class Supra(Toyota):

#     def speed(self):
#         print("300 km/h")


# s1 = Supra()

# s1.start()
# s1.model()
# s1.speed()

# ////////    /////   //////  /////   /// ///
# multiple inheritance=Parent1 + Parent2 → Child


# class Father:

#     def skills1(self):
#         print("Driving")


# class Mother:

#     def skills2(self):
#         print("Cooking")


# class Child(Father, Mother):

#     def skills3(self):
#         print("Coding")


# c1 = Child()

# c1.skills1()
# c1.skills2()
# c1.skills3()


# class Camera:

#     def photo(self):
#         print("Take photo")


# class Phone:

#     def call(self):
#         print("Make call")


# class SmartPhone(Camera, Phone):

#     def internet(self):
#         print("Use internet")

# s1 = SmartPhone()

# s1.photo()
# s1.call()
# s1.internet()


# >>>>>><<<<<<<>>>>>><<<<<
# Father      Mother
#     \        /
#       Child
# ///////////////////////////

# super() is a built-in Python function used to access the parent class method or anything .super().__init__()
# class Parent:

#     def show(self):
#         print("Parent method")


# class Child(Parent):

#     def display(self):
#         super().show()


# c1 = Child()
# c1.display()

# class Car:

#     def __init__(self):
#         print("Car constructor")


# class Toyota(Car):

#     def __init__(self):

#         super().__init__()

#         print("Toyota constructor")


# t1 = Toyota()

# class Animal:

#     def sound(self):
#         print("Animal sound")


# class Dog(Animal):

#     def sound(self):

#         super().sound()

#         print("Dog barks")


# d1 = Dog()
# d1.sound()
# ////////    /   //  /   //////  //////  ///

# @classmethod is a method which is basically used to change the attribut of a class 
# It is commonly used to:

# modify class attributes
# access class variables
# create alternative constructors
# class person:
#     name="shyam"

#     @classmethod
#     def changename(cls,name):
#         cls.name=name
#         print(name)

# p1=person()
# p1.changename("roman")
# print(p1.name)

# ///////     ////////    //////  /////// /////// /////

# SUMMARY:

# # 1. Static Methods

# ```python id="jlwmy8"
# @staticmethod
# ```

# * No `self`
# * No `cls`
# * Does not depend on object or class state
# * Used for utility/helper functions

# Example:

# ```python id="jlwmy9"
# class Math:

#     @staticmethod
#     def add(a, b):
#         return a + b
# ```

# Use:

# ```python id="jlwmz0"
# Math.add(2, 3)
# ```

# ---

# # 2. Class Methods (`cls`)

# ```python id="jlwmz1"
# @classmethod
# ```

# * Uses `cls`
# * Works with class variables
# * Can modify class attributes

# Example:

# ```python id="jlwmz2"
# class Student:

#     school = "ABC"

#     @classmethod
#     def change_school(cls, name):
#         cls.school = name
# ```

# ---

# # 3. Instance Methods (`self`)

# Normal methods.

# * Uses `self`
# * Works with object data
# * Most common type of method

# Example:

# ```python id="jlwmz3"
# class Student:

#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(self.name)
# ```

# ---

# # Best Quick Memory Trick

# | Method Type              | Uses              |
# | ------------------------ | ----------------- |
# | Static method            | Utility logic     |
# | Class method (`cls`)     | Class-level data  |
# | Instance method (`self`) | Object-level data |

# ---

# # Real Meaning

# | Keyword | Refers To      |
# | ------- | -------------- |
# | `self`  | Current object |
# | `cls`   | Current class  |

# ---

# # One-Line Definitions

# * Static method → independent helper function inside class
# * Class method → method that works with class itself
# * Instance method → method that works with object data

# ////////    /////////   ////////    //////////  /////////// ////////
# @property method: Access method like variable
# Why Use @property?

# It gives:

# cleaner syntax
# encapsulation
# validation control
# safer attribute management
# You can calculate values dynamically.

# Example:

# percentage
# age
# BMI
# salary after tax

# without storing them separately.

# class Student:
#     def __init__(self,phy, chem ,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math

#     @property #getter
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"

# s1=Student(90,33,44)
# print(s1.percentage)
# s1.chem=90
# print(s1.percentage)


# class Student:

#     def __init__(self):
#         self._age = 0


#     # Getter
#     @property
#     def age(self):
#         return self._age


#     # Setter
#     @age.setter
#     def age(self, value):

#         if value < 0:
#             print("Invalid age")

#         else:
#             self._age = value

# s1 = Student()
# s1.age = 19
# print(s1.age)
# s1.age=20
# print(s1.age)

# /////// //////  /////////
  