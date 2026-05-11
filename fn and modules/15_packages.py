# In Python, a package is a way to organize related modules into folders.

from packages.string_ops import add_str
from packages.math_ops import add_num


# from folder_name.module_name import fn
#   . show current folder

# ////

print(add_str("hello","worl!d"))
print(add_num(10,20))

# fn and modules/
# │
# ├── 15_packages.py
# │
# ├── packages/
# │   ├── __init__.py
# │   ├── math_ops.py
# │   └── string_ops.py

# Thing	Meaning

# Module	single .py file
# Package	folder of modules
# Library	collection of packages/modules


# Example
# Module
# math_ops.py
# Package
# packages/
# Library

# NumPy

# Contains many packages/modules internally.


# Common Beginner Mistakes
# Mistake 1

# Missing __init__.py

# Causes:

# ModuleNotFoundError

# Absolute Import
# from packages.math_ops import add_num

# /////// //////  /////// ////////
# Relative Import
# from .math_ops import add_num