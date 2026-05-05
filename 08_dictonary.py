# key:value for dictonary unordered mutable and not allowed duplicate keys,noindexing

info={
    "name":"ran",
    "age":20,
    "class":3,
    "subjects":{
        "phy":3,
        "math":3
    }
}
# print(info["age"])
# print(info["subjects"]["phy"])
# print(list(info.keys()))
# print(list(info.values()))
# print(info.items())
print(info.get("subject"))