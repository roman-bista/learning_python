# JSON means:
# JavaScript Object Notation

# Used everywhere in:

# APIs
# databases
# backend systems
# import json

# data = {
#     "name": "Roman",
#     "age": 19
# }

# result = json.dumps(data)

# print(result)


# output={"name": "Roman", "age": 19}
# import json

# data = '{"name":"Roman","age":19}'

# result = json.loads(data)

# print(result)
# print(type(result))

# Function	Purpose
# dumps()	dict → JSON string
# loads()	JSON string → dict


# Writing JSON File
# import json

# data = {
#     "name": "Roman",
#     "age": 19
# }

# with open("data.json", "w") as f:
#     json.dump(data, f)

# Reading JSON File
# import json

# with open("data.json", "r") as f:
#     data = json.load(f)

# print(data)