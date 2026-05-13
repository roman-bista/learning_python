# file=open("11_file.txt","r")
# # contents=file.readline()
# contents=file.readlines()
# print(contents)
# file.close()


# file=open("11_file.txt","a")
# contents=file.write("hello world hi \n").  w and write(): overwrite
# print(contents)
# file.close()

# with open("11_file.txt", "r") as file:
#     print(file.tell())

#     print(file.read(5))

#     print(file.tell())

#     file.seek(0)

#     print(file.read(5))

# file=open("11_file.txt","r+")

# content=file.write("my name is roman")  #r+ write le chai k write garne file ma tara existing file ko aagadi matra write garxa remaing dekhauxa tya dekhi katera

# print(content)

# file=open("11_file.txt","w+")
# content=file.read()  #khali gardinxa file nai if we use w+ and read()
# file.close()


# file=open("11_file.txt","w+")
# content=file.write("hlohlffddo")  
# file.close()