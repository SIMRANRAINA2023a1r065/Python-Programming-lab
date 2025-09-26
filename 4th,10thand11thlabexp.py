# EXP 4: write a program to perform searching activity using linear seach and binary search
#linear search
lst=[]
n=int(input("no of elements in list:"))
for i in range(n):
    lst.append(int(input("enter the elements:")))

print(lst)
#lst.sort()
#print(lst)

num=int(input("Enter the number to search:"))
print("Linear search of list of numbers is as:")
for i in range(len(lst)):
    if(lst[i]==num):
        print(f"Number is found at index  {i} !")
        break
else:
    print("Number is not found !")

#or: for not using for loop for printing the list simply
# n=int(input("Enter your limit:"))
# lst=list(map(int,input(f"Enter {n} number separated by space").split(" "))) 
# print(lst)

# binary search
n=int(input("No of elements in list:"))
lst=list(map(int,input(f"Enter {n} numbers separated by space:").split(" ")))
print(lst)
lst.sort() # bineary search m sort krna pdta hai
print(f"After sorting list is: {lst}")
min=0
max=len(lst)-1
num=int(input("Enter the number to search:"))
print("Binary search of list of numbers is as:")
while(min<=max):
     mid=(min+max)//2 #float error will come without //
     if(num==lst[mid]):
       print(f"Number is found at index {mid} !")
       break
     elif(lst[mid]<num): 
       min=mid+1
     else:
        max=mid-1
else:
   print("Number is not found !")
    

# EXP 10: simple calculator program : using switchcase and functions
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the choice(case number):"))
match c:
    case 1: print(f"Addition of {a} and {b} is:",a+b)
    case 2: print(f"Subtraction of {a} and {b} is:",a-b)
    case 3: print(f"Multiplication of {a} and {b} is:",a*b )
    case 4: print(f"Division of {a} and {b} is:",a/b)
    case _: print("Invalid")
def add_numbers(d,e):
    print(f"Addition of {d} and {e} is:",d+e)
def sub_numbers(d,e):
    print(f"Subtraction of {d} and {e} is:",d-e)
def mult_numbers(d,e):
    print(f"Multiplication of {d} and {e} is:",d*e)
def div_numbers(d,e):
    print(f"Division of {d} and {e} is:",d/e)
d=int(input("Enter the first number:"))
e=int(input("Enter the second number:"))
add_numbers(d,e)
sub_numbers(d,e)
mult_numbers(d,e)
div_numbers(d,e)
#EXP 11: Write a python program that accepts the length of three sides of a triangle as inputs. 
# The program should indicate whether or not the triangle is right-angled triangle. (use Pythagorean theorem). 
# Also find out its area using Herons formula.
# Input sides of the triangle
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

# Check if it's a right-angled triangle
# Sort sides to easily compare the largest side
sides = [a, b, c]
sides.sort()
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("It is a Right-Angled Triangle")
else:
    print("It is NOT a Right-Angled Triangle")

# Find the area using Heron's formula
s = (a + b + c) / 2
area = ((s - a) * (s - b) * (s - c)) ** 0.5
print(f"Area of the triangle = {area:.2f}")
