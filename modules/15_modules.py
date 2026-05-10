# a module is a file
# # math_utils.py
# def add(a,b):
#     return a+b
# #  main.py
# import math_utils
# print(math_utils.add(3,4))

# import math
# print(math.sqrt(9))
# from math import sqrt

# print(sqrt(16))
# ////////    /////// ////////
# import with alias/nickname
# import math as m
# print(m.pi)

# import random

# print(random.randint(1, 10))
# User-Defined Modules

# Any .py file you create can become a module.

# Example project:

# project/
# │
# ├── main.py
# ├── calculator.py
# calculator.py
# def multiply(a, b):
#     return a * b
# main.py
# import calculator

# print(calculator.multiply(4, 5)


 # alised module
# import datetime as dt
# print(dt.date.today())

# //////////  //////  /////// ///////
# using third party modules
# pip install requests
# import requests
# response=requests.get("link")
# print(requests.status_codes)