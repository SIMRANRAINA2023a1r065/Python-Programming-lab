# Program to print natural numbers from 1 to n using while loop

# Input from user
n = int(input("Enter your limit: "))

i = 1   # initialization

while i <= n:   # condition
    print(i, end=" ")   # print current value of i
    i += 1   # increment

##2

# Program to print natural numbers from 1 to n (in reverse) using while loop

# Input from user
n = int(input("Enter your limit: "))

i = n   # initialization

while i >= 1:   # condition
    print(i, end=" ")   # print current value of i
    i -= 1   # decrement


 ##3

 ##Write a python program to print all even numbers between 1 to 100. - using while loop

print("All even no.`s b/w 1 to 100 are:")
for temp in range(2,100,2):
  print(temp,end= " ")

#4

## 4: Write a python program to find sum of all natural numbers between 1 to n.
n=int(input("Enter your limit:"))
i=1
sum=0
while(i<=n):
   sum=sum+i
   i+=1
print(sum)

##5: Write a python program to find sum of all even numbers between 1 to n.
n = int(input("Enter your limit: "))
i = 2       # even number start hota hai 2 se
sum = 0

while i <= n:
    sum = sum + i
    i += 2   # har baar agla even number add hoga
print("Sum of even numbers =", sum)

#6.	Write a python program to print multiplication table of any number.
n=int(input("Enter any number for which you want to print the table:"))
i=1
print(f"Table of {n} is as follows:")
while i<=10:
   print(f"{n}*{i} =",n*i)
   i+=1

# 7.Write a python program to count number of digits in a number.
num=(input("Enter the number:"))
print(f"Number of digits in {num} is:",len(num))

#or 

#using while loop

num = int(input("Enter a number: "))  # User se number input lo
n = abs(num)                           # Negative number ko positive bana do
count = 0                               # Count ko 0 se start karo

while n:                                # Jab tak number non-zero hai
    n //= 10                             # Last digit remove karo
    count += 1                           # Count me 1 add karo

print("Number of digits:", count)       # Total digits print karo
 #or
 #by using for loop
num = input("Enter a number: ")
count = 0

for d in num:          # Har digit ke liye loop chalega
    count += 1         # Count 1 se badhao

print("Number of digits:", count)


#8.	Write a python program to find first and last digit of a number.
num1=(input("Enter the number:"))
print(f"First and last digit of {num1} is:",num1[0],"and",num1[-1])

#or

#using while loop

num = int(input("Enter a number: "))   # User se number input lo
n = abs(num)                           # Negative number ko positive bana do

last = n % 10                           # Last digit nikal lo

while n >= 10:                          # Jab tak number >= 10 hai
    n //= 10                             # Last digit hatao taaki first digit mil jaye

first = n                               # Jo bacha wo first digit hai

print("First digit:", first)            # First digit print karo
print("Last digit:", last)              # Last digit print karo

#or
#by using for loop

num = input("Enter a number: ")

first = num[0]
last = num[-1]

for d in num:          # Loop har digit ke liye
    if first is num[0]:  # Pehli digit ko first set karo
        first = d
    last = d           # Har digit update hoti rahegi, last digit final me milegi

print("First digit:", first)
print("Last digit:", last)


#9.	Write a python program to find sum of first and last digit of a number.
num1 = input("Enter the number: ")

# Convert first and last digit to integer
first = int(num1[0])
last = int(num1[-1])

sum_digits = first + last   # Ab sum correctly calculate hoga

print(f"Sum of first and last digit i.e {num1[0]} and {num1[-1]} is:", sum_digits)

#or

#using while loop

num = int(input("Enter a number: "))   # User se number input lo
n = abs(num)                           # Negative number ko positive bana do

last = n % 10                           # Last digit nikal lo

while n >= 10:                          # Jab tak number >= 10 hai
    n //= 10                             # Last digit hatao taaki first digit mil jaye

first = n                               # Jo bacha wo first digit hai

print(f"sum of First digit-> {first} and last digit -> {last} is:", first+last)       
#or
# by using for loop
num = input("Enter a number: ")

first = num[0]
last = num[-1]

for d in num:          
    if first is num[0]:   # Pehli digit ko first set karo
        first = int(d)
    last = int(d)       # Last digit ko update karte jao

sum_digits = first + last
print("Sum of first and last digit:", sum_digits)
  
      
# 10.	Write a python program to calculate product of digits of a number.
num = input("Enter a number: ")     # Number ko string me input lo
product = 1                          # Product ko 1 se start karo

for d in num:                        # Har digit ke liye loop
    product *= int(d)                # Digit ko int me convert karke multiply karo

print("Product of digits:", product) # Final product print karo

#11.Write a python program to enter a number and print its reverse.
#using string slicing
num = input("Enter the number: ")      # Number ko string me lo
rev = num[::-1]                         # String slicing: start:end:step (-1 se reverse)

print("Reverse of the number:", rev) 

#using for loop
num = input("Enter the number: ")   # User se number input lo, string me
rev = ""                             # Empty string se reverse start karte hain

for d in num:                        # Loop har character (digit) ke liye
    rev = d + rev                    # Current digit ko pehle add karo, purana reverse ke baad

print("Reverse of the number:", rev) # Final reversed number print karo

#using while loop
num = int(input("Enter the number: "))
n = num
rev = 0

while n > 0:
    last_digit = n % 10          # Last digit nikal lo
    rev = rev * 10 + last_digit  # Last digit ko reverse me add karo
    n = n // 10                  # Last digit hata do

print("Reverse of the number:", rev)

#12.	Write a python program to check whether a number is palindrome or not.
num = input("Enter a number: ")      # Number ko string me lo

# Check palindrome using string slicing
if num == num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

# using for loop

num = int(input("Enter a number: "))  # User se number input lo
n = num
rev = 0

while n > 0:
    last_digit = n % 10               # Last digit nikal lo
    rev = rev * 10 + last_digit       # Reverse me add karo
    n = n // 10                       # Last digit hata do

# Check palindrome
if rev == num:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
# using while loop
num = int(input("Enter a number: "))  # User se number input lo
n = num
rev = 0

while n > 0:
    last_digit = n % 10               # Last digit nikal lo
    rev = rev * 10 + last_digit       # Reverse me add karo
    n = n // 10                       # Last digit hata do

# Check palindrome
if rev == num:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

#13.	WAP to print the following pattern: 1	3	 5	 7	 9 …….till 100 
print("All odd numbers starting from 1 ro 100 are:")
for temp in range(1,100,2):
   print(temp,end=" ")

# 14. Write a python program to find power of a number using for loop.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(f"pow({num1},{num2}) =", pow(num1, num2))
# using for loop
num1 = int(input("Enter first number: "))   # User se base number input lo
num2 = int(input("Enter second number: "))  # User se exponent input lo

result = 1                                   # Start with 1, because anything^0 = 1

for d in range(num2):                        # Loop num2 times (exponent)
    result *= num1                            # Multiply result by base each time

print(f"{num1} ^ {num2} =", result)          # Final power print karo

# 15.Write a python program to find all factors of a number.


num = int(input("Enter a number: "))      # User se number input lo

print(f"Factors of {num} are:")

for i in range(1, num + 1):               # 1 se num tak loop chalega
    if num % i == 0:                       # Agar i perfectly divide kare num ko
        print(i, end=" ")                  # Factor ko print karo

 # 16.	Write a python program to calculate factorial of a number.
import math

n = int(input("Enter a number: "))
result = n * math.factorial(n-1)   # n! = n * (n-1)!
print(f"{n}! = {result}")

#using for loop
n = int(input("Enter a number: "))  # User se number input lo
fact = 1                             # Factorial start karenge 1 se

for i in range(1, n + 1):            # 1 se n tak loop chalega
    fact *= i                         # fact = fact * i (multiply each number)

print(f"{n}! = {fact}")              # Final factorial print karo

# 17.	Write a python program to check whether a number is Prime number or not.
n = int(input("Enter the number:"))

if n <= 1:  # 0 aur 1 prime nahi hote
    print(f"{n} is not a prime number")
else:
    for i in range(2, n):           # 2 se n-1 tak check karenge
        if n % i == 0:              # Agar divisible hai
            print(f"{n} is not a prime number")
            break
    else:                             # Loop complete hua aur break nahi hua
        print(f"{n} is a prime number")

# 18.	Write a python program to print all Prime numbers between 1 to n.
n = int(input("Enter the number:"))
print(f"Prime numbers from 2 to {n} are:")

for num in range(2, n+1):            # 2 se n tak har number check karo
    for i in range(2, num):          # 2 se num-1 tak check karo
        if num % i == 0:             # divisible hua → not prime
            break
    else:                             # break nahi hua → prime hai
        print(num, end=" ")
# 19. Write a python program to find sum of all prime numbers between 1 to n.
n = int(input("Enter the number:"))
prime_sum = 0                        # sum store karne ke liye variable

for num in range(2, n+1):            # 2 se n tak har number check karo
    for i in range(2, num):          # 2 se num-1 tak check karo
        if num % i == 0:             # divisible hua → not prime
            break
    else:                             # break nahi hua → prime hai
        prime_sum += num              # prime number ko sum me add karo

print(f"Sum of all prime numbers from 1 to {n} is: {prime_sum}")
