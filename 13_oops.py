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