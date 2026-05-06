# def countdown(n):
#     print(n)
#     if n==1:
#         return 
#     countdown(n-1)
# countdown(5)

# n=int(input("enter n"))
# def fact(n):
#     if(n==0):
#         return 1
#     return n*fact(n-1)
# print(fact(n))

# 1+2+3+4+5

# def sum(n):
#     if n==0:
#         return 0
#     return n+ sum(n-1)
# print(sum(5))

# 01123,5,8

# def fib(n):
#     if n==0 or n==1:
#         return 1
#     return fib(n-1)+fib(n-2)
# print(fib(3))

# palindroem
# def fn(n):
#     original=n
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     if rev==original:
#         print("palindrome")
#     else:
#         print("no palindrome")
# fn(121)

def fn(text):
    original=text
    rev=text[::-1]
    if rev==original:
        print("palindrome")
    else:
        print("not palindrome")
fn("racecar")