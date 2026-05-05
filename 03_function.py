# def forall(to="world"):
#     print("hello", to)
     
# forall()
# name=input("what is ur name: ")
# forall(name)

import math

def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = float(input("Enter second number: "))

result = add(a, b)
rounder=math.ceil(result)
rounder2=math.floor(result)
print(f"Addition number is {rounder},{rounder2}")