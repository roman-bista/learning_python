# An iterator is an object that lets you traverse through data one item at a time.
# __iter__()
# __next__()

# A generator is an easier way to create iterators.
# Instead of writing __iter__() and __next__(),
# you use: yield
# def my_gen():
#     yield 1
#     yield 2
#     yield 3

# g = my_gen()

# print(next(g))
# print(next(g))
# # print(next(g))
# Difference Between return and yield
# return
# def test():
#     return 5
# Function ends immediately
# yield
# def test():
#     yield 5
# Saves function state
# Pauses function
# Continues later
# def demo():
#     print("Start")
#     yield 1

#     print("Middle")
#     yield 2

#     print("End")
#     yield 3

# g = demo()

# print(next(g))
# print(next(g))
# print(next(g))

# Memory Comparison
# Normal List
# nums = [x for x in range(1000000)]

# Stores all million values in memory.
# nums = (x for x in range(1000000))

def creater():
    i=1
    while i<=20:
        yield i
        i+=1
print(creater())
x=creater()
print(next(x)) #1
print(next(x))
print(list(x))