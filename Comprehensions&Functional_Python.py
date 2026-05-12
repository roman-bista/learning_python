# List Comprehension

# marks=[1,2,3,4]
# new_marks=[]
# for i in marks:
#     new_marks.append(i*i)

# print(new_marks)

# list comprehension:

#here 5 lines
# marks=[1,2,3,4]
# new_marks=[i*i for i in marks]
# print(new_marks)

# cube=[]
# for i in range(1,10):
#     if i%2==0:
#         cube.append(i**3)
# print(cube)

# # by list comprehesion
# cube=[]
# new=[i**3 for i in range(1,10) if i%2==0]
# print(new)

# [expression for item in iterable]

# /////////////   /////////// ////////////

# 2. Dictionary Comprehension
# num=[2,22,222]
# d={}
# for i in num:
#     d[i]=i*i
# print(d)

# # by comprehension
# num=[2,22,222]
# d={i: i*i for i in num}
# print(d)
# //////////  /////////
# 3. Set Comprehension
# num=[2,3,4,55,6,67]
# s={ x for x in num}
# print(s)

# //////////////  /   ///

# lambda=lambda arguments: expression

# add=lambda a,b: a+b
# print(add(2,3))

# 4.map == each element ma operation=

# map(function, iterable)
# num=[1,2,3,4]
# result=map(lambda x: x*x,num)  #map(function, iterable)
# print(list(result))

# /////// /////// //  /   /   //  /   /   /   //  /   //

# filter: values based upon condition

# num=[1,2,3,4,5]
# even=filter(lambda i: i%2==0, num)
# print(list(even))

# filter(function, iterable)
# //////////  ////////    ////////
# from functools import reduce
# from functools import reduce

# nums = [1,2,3,4]

# result = reduce(lambda a,b: a+b, nums)

# print(result)

# /////// //////////  //////////names = ["Roman", "Hari"]
# zip()
# marks = [90, 80]
# names=["roman","harry"]

# result = list(zip(names, marks))

# print(result)

# names = ["Roman", "Hari"]
# marks = [90, 80]

# for name, mark in zip(names, marks):
#     print(name, mark)

# /////////   ////////////

# enumerate()

# Adds index while looping.

# Without enumerate:

# names = ["a", "b", "c"]

# index = 0

# for name in names:
#     print(index, name)
#     index += 1

# better way by enumerate:

# names = ["a", "b", "c"]

# for index, value in enumerate(names):
#     print(index, value)

# //////////////    /////// //////////  //////
# 10. Packing & Unpacking
# *args

# Accepts multiple positional arguments.

# def total(*nums):
#     print(nums)

# total(1,2,3,4)

# Output:

# (1,2,3,4)

# Tuple is created automatically.

# Sum Example
# def total(*nums):
#     return sum(nums)

# print(total(1,2,3))
# **kwargs

# Accepts keyword arguments.

# def info(**data):
#     print(data)

# info(name="Roman", age=19)

# Output:

# {'name':'Roman', 'age':19}
# Unpacking
# nums = [1,2,3]

# print(*nums)

# Output:

# 1 2 3
# Dictionary Unpacking
# data = {
#     "name": "Roman",
#     "age": 19
# }

# def info(name, age):
#     print(name, age)

# info(**data)