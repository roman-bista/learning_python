# Python Generators - Learning Guide

# 1. Basic Generator Function
def simple_generator():
    """A simple generator that yields values one at a time"""
    yield 1
    yield 2
    yield 3

print("1. Basic Generator:")
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


# 2. Generator with Loop
def count_up_to(n):
    """Generator that counts from 1 to n"""
    i = 1
    while i <= n:
        yield i
        i += 1

print("\n2. Generator with Loop:")
for num in count_up_to(5):
    print(num, end=" ")  # Output: 1 2 3 4 5
print()


# 3. Generator Expression (similar to list comprehension)
print("\n3. Generator Expression:")
gen_expr = (x * 2 for x in range(5))
print(next(gen_expr))  # Output: 0
print(next(gen_expr))  # Output: 2
print(next(gen_expr))  # Output: 4

# Or iterate through all values
gen_expr2 = (x ** 2 for x in range(4))
for value in gen_expr2:
    print(value, end=" ")  # Output: 0 1 4 9
print()


# 4. Generator with send() method
def echo_generator():
    """Generator that receives values via send()"""
    value = None
    while True:
        value = yield value
        if value is not None:
            value = f"Echo: {value}"

print("\n4. Generator with send():")
gen4 = echo_generator()
next(gen4)  # Prime the generator
print(gen4.send("Hello"))  # Output: Echo: Hello
print(gen4.send("World"))  # Output: Echo: World


# 5. Generator with State
def fibonacci(limit):
    """Generator that yields Fibonacci numbers up to limit"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("\n5. Fibonacci Generator:")
for fib in fibonacci(20):
    print(fib, end=" ")  # Output: 0 1 1 2 3 5 8 13
print()


# 6. Key Differences: Generator vs List
print("\n6. Memory Efficiency - Generator vs List:")
import sys

# List approach (stores all values in memory)
list_comp = [x * x for x in range(1000)]
print(f"List size: {sys.getsizeof(list_comp)} bytes")

# Generator approach (generates values on demand)
gen_comp = (x * x for x in range(1000))
print(f"Generator size: {sys.getsizeof(gen_comp)} bytes")


# 7. Chaining Generators
def first_gen():
    """First generator"""
    yield 1
    yield 2

def second_gen():
    """Second generator"""
    yield 3
    yield 4

def chain_generators(*generators):
    """Chain multiple generators"""
    for gen in generators:
        yield from gen

print("\n7. Chaining Generators:")
for val in chain_generators(first_gen(), second_gen()):
    print(val, end=" ")  # Output: 1 2 3 4
print()
