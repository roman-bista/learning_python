# # def add(*args):
# #     print(args)
# #     return sum(args)


# # print(add(1,2,3,4))

# # so args is a positional arguments as tuple
# # here (1,2,3,4) are postional arguments
# #  args le chsai variable nabhako arrgumetns linxa

# # /////////   /////////   ////////////
# # **kwargs are variable keywrod arguments collect named argumetns into a dictonary

# # def info(**kwargs):
# #     print(kwargs)
# # info(name="roman",age=20)

# # using both together
# # def demo(*args, **kwargs):
# #     print("ARGS:", args)
# #     print("KWARGS:", kwargs)

# # demo(1, 2, 3, name="Roman", skill="Python")
# # Function parameters should usually follow this order:

# # def func(normal, *args, **kwargs):
# #     pass


# # nums = [1, 2, 3]

# # print(*nums)

# data={
#     "age":3,
#     "name":"fdffd"
# }
# def studnet(name,age):
#     print(name,age)

# studnet(**data)




# def test(*numbers, **details):
#     pass

# we can use this for agrs*
# and for kwargs ** any name 

def wrapper(*args, **kwargs):
    print("Before function")

    result = calculate(*args, **kwargs)

    print("After function")
    return result


def calculate(a, b):
    return a + b

print(wrapper(5, 10))