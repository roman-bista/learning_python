# Original Function
#         ↓
# Decorator adds extra behavior
#         ↓
# Modified Function


# def greet():       #original fn
#     print("Hello Roman")

# def decorator(func):

#     def wrapper():
#         print("Before")
#         func()
#         print("After")

#     return wrapper

# obj = decorator(greet)

# obj()
# # or.      ///////
# @decorator
# def greet():       #original fn
#     print("Hello Roman")

# greet()

# def decorator(func):

#     def wrapper():
#         print("=== Start ===")

#         func()

#         print("=== End ===")

#     return wrapper


# @decorator
# def hello():
#     print("Welcome")

# hello()