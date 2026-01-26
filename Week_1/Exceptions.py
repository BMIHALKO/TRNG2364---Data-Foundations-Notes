#Errors and Exceptions
#All exceptions are errors, but not all errors are exceptions

#Errors - problems that prevent our application from running correctly
#EX: syntax error; there is no handling, we just have to fix it
#most errros come with error messages to help diagnose the issue
#Syntax, Indentation, Name, Value, Type 0 division, etc...

#Exceptions - problems that are raised during runtime and can be detected and handled using try-except (try-catch in Java)

# try:
#     x = int("5")
#     print(x)

# except ValueError:
#     print("Conversion has failed")

# #try-except-else-finally

# try:
#     number = int(input("Please enter a number: "))
#     result = 10 / number
# except ValueError:
#     print("Invalid Input. Please enter a valid integer")
# except ZeroDivisionError:
#     print("You cannot divide by 0.")

# #its a good idea to have a generic catch-all exception block to handle anything we have not thought of
# except Exception:
#     print("I have no idea how you got here.")

# else:
#     #runs only if NO exception occurs
#     print(f"Your result: {result:.3f}")

# finally:
#     #runs no matter what, whether or not an exception is thrown
#     print("Execution Complete . . .")


# #We can manually raise(throw) an exception using the 'raise' keyword
# y = -5

# if y < 0:
#     raise Exception("Sorry no negative numbers allowed")


#We can create custom exceptions by creating our own custom exception class
class myCustomException(Exception):
    def __init__(self, message = "This is not the exception you are looking for"):
        super().__init__(message)

userNumber = input("Please enter your favorite integer: ")

if not type(userNumber) is int:
    raise myCustomException()
print(userNumber)