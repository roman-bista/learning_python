# CREATE STUDENT CLASS THAT TAKES NAME AND MARKS OF 4 STUDENT AS ARGUMENT IN CONSTRUSTOR AND CREATE METHOD TO PRINT THEIR AVG
# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def cal_avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i

#         print("hi",self.name,"your marks is :",sum/3)


# sub1=Student("phy",[0,2,3])
# sub2=Student("chem",[60,3,4])
# sub3=Student("sci",[2,4,34])
# sub1.cal_avg()

# ////////    ////    /////// /////
# class Account:

#     def __init__(self,balance,acc_num):
#         self.balance=balance
#         self.acc_num=acc_num

#     def debit(self,amount):
#         self.balance=-amount
#         print("rs",amount,"was debited")
#         print("total balance is",self.get_balance)

        
#     def credit(self,amount):
#         self.balance+=amount
#         print("rs",amount,"credited")
#         print("total balance is",self.get_balance)
#     def get_balance(self):
#         return self.balance

# acc1 = Account(100,12345)
# acc1.debit(1000)
# acc1.credit(200)


# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def perimeter(self):
#         return 2*3.14*self.radius



# c1 = Circle(4)

# print(c1.area())
# print(c1.perimeter())

class Employee:
    def __init__(self,role,salary):
        self.role=role
        self.salary=salary

    def show(self):
        print(self.role,self.salary)
# e=Employee("top",12345)
# e.show()

class Engineer(Employee):
    def __init__(self, role, salary,age,name):
        super().__init__(role, salary)
        self.age=age
        self.name=name

    def showdetails(self):
        self.show()
        print(self.age,self.name)

eg=Engineer("enginner", 333333, 33, "roman")
eg.showdetails()