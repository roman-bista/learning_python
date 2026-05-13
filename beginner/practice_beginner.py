# i=1
# while i<=100:
#     print(i)
#     i+=1
# i=100
# while i>=1:
#     print(i)
# #     i-=1
# i=1
# n=int(input("enter  n :"))
# while i<=10:
#     mul=n*i
#     print(f" {n}*{i}={mul}")
#     i+=1
# list=[2,3,5,6,4,3,2,34,545,3,35,54,3,5,566,34]
# n=int(input("enter  n  to search :"))

# while n in list:
#     if(n==list):
#         print(f"{n}is in list")
#     else:
#         print("not found")
#     n+=12


# for i in range(3):
#     pass
    

# n=int(input("enter n"))
# i=0
# sum=0
# while i<=n:
#     sum+=i
#     i+=1

# print(sum)

# sum=0
# n=int(input("enter n"))

# for i in range(1,n+1):
#     sum+=i
#     i+=1


# print(sum)

# 5!=5*4*3*2*1
# 5*(n-1)!
# n=int(input("enter n:"))
# fact=1
# for i in range(n,0,-1): 
#     fact = fact * i

# print(fact)

# fibonaci 0,1,1,2,3,5,8

# n=int(input("enter n:"))
# a=0
# b=1

# for i in range(n):
#    print(a)
#    c=a+b
#    a=b
#    b=c

# palindrome
# 121,racecar,madam


# text=(input("en†er string: "))
# text2=text[::-1]
# if text==text2:
#     print("palindrome")
# else:
#     print("not palindrome")
    

# 1 2 1
n = input("Enter: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# wap to ask the user to enter the name of 3 fav movie and store them in list

# list=[]
# movies1=input("enter the 1st fav movie: ")
# movies2=input("enter the 2nd fav movie: ")
# movies3=input("enter the 3rd fav movie: ")
# list.append(movies1)
# list.append(movies3)
# list.append(movies2)

# print(list)


# via looping

# list=[]
# for i in range(1,4):
#     movie=input(f"enter {i}st movies:")
#     list.append(movie)
# for movie in list:
#    print(movie)


# wap to check if a list conatin a plaindrome of elements:

# list=[1,2,3,2,1]
# copied_list=list.copy()
# list.reverse()
# if(copied_list==list):
#     print("palindrome")
# else:
#     print("not palindrome")

# wap to count the number of student with the A grade in the following tupple

# tup=("c","d","a","a","b","b","a")
# print(tup.count("a"))

