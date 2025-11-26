#Exception Handling: in lay man language, occurring surprising something
# iT is an event which can occur during the program execution and can lead to the abnormal execution of the program.

# What is an Exception ?
#An excecption Handling is an event that occur during execution of a program that disrupts the normal flow of program execution.
#when this event occurs, Python generates an exception that can be handled, which avoids your program to crash.

# Why use Exceptions ?
#Exceptions are convenient in many ways for handling errors ans special conditions in a program.
# when you think that you have a code which can produce an error then you can use exception handling.

#You can raise an exception in your own program by using the raise exception statement.

#Raising an exception breaks current code execution and returns the exception back until it is handling.

#Exception  propagation hmesha current Environment sa parent environmentse move krta hai...

#Exception Handler/ Error Handler:

# The runtime system reaches the call stack for a method/function that contains a block of code that can handle the  exception.
# This block of code is called an exception handler.

#The search begins with the method/function in which the exception occurred and proceeds through the cell stack in the reverse order in which the methods/function
#were called.

#When an appropriate handler is found, the runtime system passes the exception object to the handler.

#An exception handler is considered appropriate if the type of the exception object throen matches the type that can be handled by the handler.

def div():
    print("-----Start of div function ----")
    num1=int(input("Enter first num:"))
    num2=int(input("Enter second num:"))
    res=num1//num2
    print(f"Result is {res}")
    print("End of div function")

def test():
    print("Inside test function")
    div()  # error yaha ayega when passing num1=12/any no. and num2=0 #Error known as trace back and Leads to data loss
    print("End of test")


print("Inside main block")
test()
print("End of main Function")

#Appropriate handler hona chahiye: jis type ka exception hai ussi type ka exception handler hona chahiye...

#Where Exception may occur ?

#Hardware/operating system level:

#arithmetic exceptions; divide by 0, under/overflow.
#Memory access violations, stack over/underflow.

#Language level:

#Bounds violations: illegal indices.
#Value Error: invalid literal, improper casts.

#Program Level:

#User-defined exceptions.

#Exception Handling Keywords:
# 1.try
# 2. except
# 3. raise
# 4. finally
# 5. else

#try-excpt syntax: 

# try: try block is a wrapper of risky code/ line of code that may cause an error/exception. Write the risky code here.
#except: handles the exception.
#else: runs only when no exception occurs.
#finally: runs always (inportant for cleanup)
#raise: used to manually raise an exception (used in custom exception)

# Exception Hndling / exceptioncep Raised Code:

#exception is the parent of all exception / base exception
def div():
    print("-----Start of div function ----")
    num1=int(input("Enter first num:"))
    num2=int(input("Enter second num:"))
    try:
      res=num1//num2
      print(f"Result is {res}")
    except Exception as ob: #using exception class for finding the type of exception raised #ob ko reference milega aur ob se hi pta chlega type of ob
          print("Exception raised!!!")
          print(ob)
    print("End of div function")

print("Inside main block")
div()
print("End of main Function")


#
import builtins
print(dir(builtins))
help(builtins.ZeroDivisionError)

#for inputing string instead of integer: how to handle  exception ..?

def div():
    print("-----Start of div function ----")
    try:
       num1=int(input("Enter first num:"))
       num2=int(input("Enter second num:"))
       res=num1//num2
       print(f"Result is {res}")

    except ZeroDivisionError as ob:
        print("Zero Division Error:",ob)
    except ValueError as ob:
        print("Value Error:",ob)
    except Exception as ob: #using exception class for finding the type of exception raised #ob ko reference milega aur ob se hi pta chlega type of ob
          print("Exception raised!!!")
          print(ob)
    print("End of div function")

print("Inside main block")
div()
print("End of main Function")

#Error ayega: valuerror and terminates abnormally
def div():
    print("-----Start of div function ----")
    try:
       num1=int(input("Enter first num:"))
       num2=int(input("Enter second num:"))
       res=num1//num2
       print(f"Result is {res}")

    except ZeroDivisionError as ob:
        print("Zero Division Error:",ob)
    # except ValueError as ob:
    #     print("Value Error:",ob)
    # except Exception as ob: #using exception class for finding the type of exception raised #ob ko reference milega aur ob se hi pta chlega type of ob
    #       print("Exception raised!!!")
    #       print(ob)
    print("End of div function")

print("Inside main block")
div()
print("End of main Function")

#

def div():
    print("-----Start of div function ----")
    try:
       num1=int(input("Enter first num:"))
       num2=int(input("Enter second num:"))
       res=num1//num2
       print(f"Result is {res}")

    except (ZeroDivisionError, ValueError) as ob:
    
        print(ob)
    except Exception as ob: #using exception class for finding the type of exception raised #ob ko reference milega aur ob se hi pta chlega type of ob
          print("Parent class exception handler",ob)
    print("End of div function")
         

print("Inside main block")
div()
print("End of main Function")