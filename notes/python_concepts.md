# Python Concepts Reference Guide

Quick reference for key Python concepts covered in this repository.

## 📌 BEGINNER CONCEPTS

### Variables & Data Types

```python
# Variables
name = "Python"
age = 3
version = 3.9

# Data types
str_var = "string"
int_var = 42
float_var = 3.14
bool_var = True
list_var = [1, 2, 3]
dict_var = {"key": "value"}
```

### String Methods

```python
text = "Hello World"
text.lower()        # "hello world"
text.upper()        # "HELLO WORLD"
text.replace()      # Replace substrings
text.split()        # Split into list
text.strip()        # Remove whitespace
```

### Control Flow

```python
if condition:
    # Do something
elif other_condition:
    # Do something else
else:
    # Default action

while condition:
    # Repeat until False

for item in iterable:
    # Process item
```

### Loops

```python
# For loop
for i in range(10):
    print(i)

# While loop
count = 0
while count < 10:
    print(count)
    count += 1

# Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

## 📗 FUNDAMENTALS

### Lists

```python
# Create list
my_list = [1, 2, 3, 4, 5]

# Methods
my_list.append(6)          # Add to end
my_list.insert(0, 0)       # Insert at index
my_list.remove(3)          # Remove value
my_list.pop()              # Remove and return last
my_list.sort()             # Sort in place
my_list.reverse()          # Reverse in place
my_list.extend([6, 7])     # Add multiple

# Indexing
first = my_list[0]
last = my_list[-1]
slice_part = my_list[1:3]  # my_list[1], my_list[2]
```

### Tuples

```python
# Create tuple (immutable)
my_tuple = (1, 2, 3)

# Operations
first = my_tuple[0]
length = len(my_tuple)
# Cannot modify after creation
```

### Dictionaries

```python
# Create dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Access
name = person["name"]
name = person.get("name", "Unknown")

# Add/Update
person["email"] = "john@example.com"

# Remove
del person["city"]
person.pop("city")

# Iteration
for key, value in person.items():
    print(key, value)
```

### List Comprehensions

```python
# Create list with expression
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i+j for j in range(3)] for i in range(3)]

# Dict comprehension
square_dict = {x: x**2 for x in range(5)}

# Set comprehension
unique_squares = {x**2 for x in range(10)}
```

---

## 🔧 FUNCTIONS

### Function Basics

```python
# Define function
def greet(name):
    """Docstring: Function description"""
    return f"Hello, {name}!"

# Call function
result = greet("Python")

# Default parameters
def add(a, b=0):
    return a + b

# Multiple return values
def divide_and_remainder(a, b):
    return a // b, a % b
```

### Recursion

```python
# Recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### Decorators

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello {name}"
```

### \*args and \*\*kwargs

```python
# *args: variable number of positional arguments
def sum_all(*args):
    return sum(args)

# **kwargs: variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Combined
def flexible_func(*args, **kwargs):
    pass
```

### Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello {name}"

# Complex types
from typing import List, Dict, Optional
def process_items(items: List[int]) -> Dict[str, int]:
    return {"count": len(items), "sum": sum(items)}
```

---

## 🏛️ OOP (OBJECT-ORIENTED PROGRAMMING)

### Classes

```python
class Dog:
    # Class variable
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says Woof!"

    # Static method
    @staticmethod
    def static_info():
        return "This is a static method"

    # Class method
    @classmethod
    def create_from_string(cls, data_string):
        name, age = data_string.split(',')
        return cls(name, int(age))

# Usage
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
```

### Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

# Usage
dog = Dog("Buddy")
print(dog.speak())  # Buddy barks!
```

### Dunder Methods (Magic Methods)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __len__(self):
        return self.age

    def __getitem__(self, index):
        return getattr(self, list(self.__dict__.keys())[index])
```

---

## 📁 FILE HANDLING

### Basic File Operations

```python
# Read file
with open("file.txt", "r") as f:
    content = f.read()

# Write file
with open("file.txt", "w") as f:
    f.write("Hello World")

# Append to file
with open("file.txt", "a") as f:
    f.write("\nNew line")

# Read lines
with open("file.txt", "r") as f:
    lines = f.readlines()
```

### JSON Handling

```python
import json

# Parse JSON
data = json.loads('{"name": "John", "age": 30}')

# Serialize to JSON
json_string = json.dumps({"name": "John", "age": 30})

# Read from file
with open("data.json", "r") as f:
    data = json.load(f)

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f)
```

### CSV Handling

```python
import csv

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Write CSV
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["John", 30])
```

---

## ⚡ ADVANCED CONCEPTS

### Iterators

```python
# Create iterator
iterator = iter([1, 2, 3])
print(next(iterator))  # 1
print(next(iterator))  # 2

# Custom iterator
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration
```

### Generators

```python
# Generator function
def count_up(max):
    count = 0
    while count < max:
        yield count
        count += 1

# Usage
for num in count_up(5):
    print(num)  # 0, 1, 2, 3, 4

# Generator expression
gen = (x**2 for x in range(5))
```

### Context Managers

```python
# Using context manager
with open("file.txt") as f:
    content = f.read()

# Create custom context manager
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False

# Usage
with MyContext() as ctx:
    print("Inside context")
```

### Exception Handling

```python
try:
    # Code that might raise exception
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exception occurred")
finally:
    print("Cleanup code")

# Raise exception
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## ⚙️ ASYNC PYTHON

### Async/Await

```python
import asyncio

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(1)
    print("Done!")
    return "Data"

# Run async function
asyncio.run(fetch_data())

# Multiple async operations
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())
    results = await asyncio.gather(task1, task2)
    return results
```

---

## 🔗 MODULES & PACKAGES

### Module Basics

```python
# In calculator.py
def add(a, b):
    return a + b

# In main.py
import calculator
result = calculator.add(5, 3)

# From import
from calculator import add
result = add(5, 3)

# Alias
import calculator as calc
from calculator import add as addition
```

### Package Structure

```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py

# Import from package
from mypackage import module1
from mypackage.subpackage import module3
```

---

## 🎯 Quick Reference Table

| Concept       | Usage                       | Example                  |
| ------------- | --------------------------- | ------------------------ |
| List          | Ordered, mutable sequence   | `[1, 2, 3]`              |
| Tuple         | Ordered, immutable sequence | `(1, 2, 3)`              |
| Dict          | Key-value pairs             | `{"a": 1, "b": 2}`       |
| Set           | Unordered, unique items     | `{1, 2, 3}`              |
| Function      | Reusable code block         | `def func(): pass`       |
| Class         | Object template             | `class MyClass: pass`    |
| Decorator     | Function wrapper            | `@decorator`             |
| Generator     | Lazy iteration              | `yield`                  |
| Lambda        | Anonymous function          | `lambda x: x**2`         |
| Comprehension | Compact list creation       | `[x for x in range(10)]` |

---

## 🔗 Important Built-in Functions

| Function      | Purpose           | Example              |
| ------------- | ----------------- | -------------------- |
| `print()`     | Output            | `print("Hello")`     |
| `len()`       | Length            | `len([1, 2, 3])`     |
| `range()`     | Number sequence   | `range(10)`          |
| `enumerate()` | Index + value     | `enumerate(list)`    |
| `zip()`       | Combine iterables | `zip(list1, list2)`  |
| `map()`       | Transform items   | `map(func, list)`    |
| `filter()`    | Select items      | `filter(func, list)` |
| `sorted()`    | Sort items        | `sorted(list)`       |
| `sum()`       | Add items         | `sum([1, 2, 3])`     |
| `max()/min()` | Maximum/minimum   | `max([1, 2, 3])`     |

---

## 📚 External Learning Resources

- **Official Docs**: https://docs.python.org/3/
- **Real Python**: https://realpython.com/
- **Python Enhancement Proposals**: https://www.python.org/dev/peps/
- **Hitchhiker's Guide**: https://docs.python-guide.org/

