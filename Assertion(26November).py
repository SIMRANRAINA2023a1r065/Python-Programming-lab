#  15 Lab Experiment
''' 
----MORSE CODE PROGRAM-----
'''























# Assertion is a debugging tool in python used to check if a condition is True while the program is running. If the condition is False, Python raises an:Assertion Error
#assertions are mainly used by developers to catch logical errors early.

#where to use Assertionns in Python ?
#1.Input Validation inside Functions (Especially internal Code):
#use assertions to check if inputs are correct for developers, not users.
# def divide(a,b):
   #assert b!=0, "b should not be zero"
#use when you expect the condition to never be wrong in correct code.

#2.Checking Function Output:
# Ensuring your function returns valid or expected results.

#3.Checking Invariants in Loops: (>=): use when certain conditions must always remain true in a loop.
#4.class invariant checks: Make sure object attributes remain valid.
#5.Debugging complex algorithms:Great for testing assumptioms in algorithms.


#voting Application:

def ageveri(age:int)->None:
   assert  age>18,"You are below age"
   print("You are allowed to cast your vote !")


ageveri(int(input("Enter your age:")))