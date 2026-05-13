# print(10 / 0)= zero division error
# try:
#     print(10 / 0)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# ////////    /////////// ////////    /////// ///////
# try:
#     num = int(input("Enter number: "))
#     print(num)

# except:
#     print("Invalid input")


# except ValueError:
# except FileNotFoundError:
# except ZeroDivisionError:


# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print(result)

# except Exception as e:        #means: catch almost all exceptions.
#     print(e)

# except ValueError:
#     print("Please enter valid integer")

# except ZeroDivisionError:
#     print("Cannot divide by zero")


# try:
#     num = int(input("Enter number: "))
#     div=int(100/num)

# except Exception as e:
#     print(e)

# else:
#     print("Success:", div)

# ////////    //////  ////////    ////////
# try:
#     print(10 / 0)

# except ZeroDivisionError:
#     print("Error")

# finally:
#     print("Program ended")
# Why finally Matters

# Used for cleanup:

# closing files
# closing DB connections
# releasing resources

# Very important in backend systems

# raise 

# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")


# try:
#     num=int(input("enter a integer: "))
#     div=100/num
# except ZeroDivisionError:
#     print("cannot divide by zero")
# else:
#     print("division of number is ",div)


# nums = [10, 20, 30]

# try:
#     print(nums[5])

# except IndexError:
#     print("Invalid index")

# nums = [10, 20, 30]

# try:
#     index = int(input("Enter index: "))

#     print(nums[index])

# except IndexError:
#     print("Index does not exist")

# except ValueError:
#     print("Please enter integer only")


# # /////////   /////////   ////////////
# try:

#     with open("data.txt", "r") as file:

#         print(file.read())

# except FileNotFoundError:
#     print("File not found")
# class ATM:

#     def __init__(self, balance):
#         self.balance = balance
        
#     def deposit(self):

#         try:
#             amount = int(input("Enter deposit amount: "))

#             if amount <= 0:
#                 raise ValueError("Amount must be positive")

#             self.balance += amount

#             print("Deposit successful")

#         except ValueError as e:
#             print(e)


#     def withdraw(self):

#         try:
#             amount = int(input("Enter withdraw amount: "))

#             if amount <= 0:
#                 raise ValueError("Amount must be positive")

#             if amount > self.balance:
#                 raise ValueError("Insufficient balance")

#             self.balance -= amount

#             print("Withdrawal successful")

#         except ValueError as e:
#             print(e)


#     def show_balance(self):
#         print("Current balance:", self.balance)


# a = ATM(5000)

# a.deposit()

# a.withdraw()

# a.show_balance()


# class InvalidAmountError(Exception):
#     pass


# class InsufficientBalanceError(Exception):
#     pass


# class InvalidPinError(Exception):
#     pass


# class ATM:

#     def __init__(self, pin, balance):

#         self.pin = pin
#         self.balance = balance
#         self.history = []

#     # ---------------- PIN CHECK ----------------

#     def check_pin(self):

#         entered_pin = int(input("Enter PIN: "))

#         if entered_pin != self.pin:
#             raise InvalidPinError("Wrong PIN")

#     # ---------------- DEPOSIT ----------------

#     def deposit(self):

#         try:

#             self.check_pin()

#             amount = int(input("Enter deposit amount: "))

#             if amount <= 0:
#                 raise InvalidAmountError(
#                     "Amount must be greater than 0"
#                 )

#             self.balance += amount

#             self.history.append(
#                 f"Deposited Rs {amount}"
#             )

#             print("Deposit successful")

#         except Exception as e:
#             print(e)

#     # ---------------- WITHDRAW ----------------

#     def withdraw(self):

#         try:

#             self.check_pin()

#             amount = int(input("Enter withdraw amount: "))

#             if amount <= 0:
#                 raise InvalidAmountError(
#                     "Amount must be greater than 0"
#                 )

#             if amount > self.balance:
#                 raise InsufficientBalanceError(
#                     "Insufficient balance"
#                 )

#             self.balance -= amount

#             self.history.append(
#                 f"Withdrawn Rs {amount}"
#             )

#             print("Withdrawal successful")

#         except Exception as e:
#             print(e)

#     # ---------------- TRANSFER ----------------

#     def transfer(self):

#         try:

#             self.check_pin()

#             amount = int(input("Enter transfer amount: "))

#             if amount <= 0:
#                 raise InvalidAmountError(
#                     "Amount must be greater than 0"
#                 )

#             if amount > self.balance:
#                 raise InsufficientBalanceError(
#                     "Insufficient balance"
#                 )

#             receiver = input("Enter receiver name: ")

#             self.balance -= amount

#             self.history.append(
#                 f"Transferred Rs {amount} to {receiver}"
#             )

#             print("Transfer successful")

#         except Exception as e:
#             print(e)

#     # ---------------- BALANCE ----------------

#     def show_balance(self):

#         try:

#             self.check_pin()

#             print(f"Current Balance: Rs {self.balance}")

#         except Exception as e:
#             print(e)

#     # ---------------- HISTORY ----------------

#     def show_history(self):

#         try:

#             self.check_pin()

#             if len(self.history) == 0:
#                 print("No transactions found")

#             else:

#                 print("\nTransaction History")

#                 for item in self.history:
#                     print(item)

#         except Exception as e:
#             print(e)


# # ---------------- MAIN PROGRAM ----------------

# atm = ATM(1234, 5000)

# while True:

#     print("\n------ ATM MENU ------")

#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Transfer")
#     print("4. Show Balance")
#     print("5. Transaction History")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         atm.deposit()

#     elif choice == "2":
#         atm.withdraw()

#     elif choice == "3":
#         atm.transfer()

#     elif choice == "4":
#         atm.show_balance()

#     elif choice == "5":
#         atm.show_history()

#     elif choice == "6":

#         print("Thank you for using ATM")
#         break

#     else:
#         print("Invalid choice")