# Basic Syntax
# variable: type
# name: str = "Roman"
# age: int = 19
def greet(name:str)->str:
    return f"hello {name}"
print(greet("roman"))
# /////// ////////

# List Type Hint
# Modern Python:

# numbers: list[int] = [1,2,3]
# String list:
# names: list[str] = ["a", "b"]

# //////  ////////

# Dictionary Type Hint
# student: dict[str, int] = {
#     "math": 90
# }
# //////  //////  ////

# def add(a: int, b: int) -> int:
#     return a + b

# means:
# a should be int
# b should be int
# returns int
