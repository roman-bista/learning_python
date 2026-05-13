# with open("practice.txt","w") as file:
#     file.write(" hi everyone \n we are learnig file io\n using python \n i like programming")
    
# with open("practice.txt","r") as file:
#  data=file.read()
#  if "learning" in data:
#   print("exist")
#  else:
#   print("not exist")

# new_data=data.replace("python","java")
# print(new_data)

# with open("practice.txt","w") as file:
#  data=file.write(new_data)
# def find():
#     word="learning"
#     with open("practice.txt","r") as file:
#         data=file.read()
#         if data.find(word)!=-1:
#             print("found")
#             print(data.index(word))
            
#         else:
#             print("not found")
# find()
# def checkforline():
#     word="learning"
#     data=True
#     line_num=1
#     with open("practice.txt","r") as file:
#         while data:
#             data=file.readline()
#             if(word in data):
#                 print(line_num)
#                 return
#             line_num+=1

#     return -1
# checkforline()
count=0
with open("practice.txt","r") as file:
    data=file.read()
    num=data.split(",")
    for i in num:
        if (int(i)%2==0):
            count+=1 #for counting even in file
print(count)