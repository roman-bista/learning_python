# # class Student:
# #     def __init__(self, name):
# #         self.name = name

# # s = Student("Roman")
# print(s.name)
 
# #  here python automatically call s.__init__("Roman")

# ////////    //////////
# 2.using str
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# s = Student("Roman", 19)

# print(s)
# ////////    ///////
# 3.repr=Used for developers/debugging.

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Student('{self.name}')"

# s = Student("Roman")

# print(s)
# 4. len=Allows object to work with:len(obj)
# class Book:
#     def __init__(self, pages):
#         self.pages = pages

#     def __len__(self):
#         return self.pages

# b = Book(300)

# print(len(b))
# ////////    /////////
# 5. add
# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# a = Number(10)
# b = Number(20)

# print(a + b)
# ///////////   /////// //////////
# 7.sub
# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __sub__(self, other):
#         return self.value - other.value

# a = Number(20)
# b = Number(5)

# print(a - b)
# /////   ////////    ////////

# 8.getitem: support indexing
# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __getitem__(self, index):
#         return self.items[index]

# m = MyList([10,20,30])
# print(m[1])
# /////// /////// /////////
# class roman:
#     def __call__(self):
#         print("hey i m roman")
# r=roman()
# r()
