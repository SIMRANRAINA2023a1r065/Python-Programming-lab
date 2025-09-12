##arr=[10,20,30,40]
##print(arr[0])
##print(arr[1])
##print(arr[2])
##print(arr[3])
##print(arr[4])

##using while loop 
##arr=[10,20,30,40,50,60,70,80,90]
##index=0
##while(index<len(arr)):
##    print(arr[index])
##    index+=1
##    
##
##using for loop

##for i in [10,20,30,40,50]
##print(i)

##using separator

##arr=[10,20,30,40,50]
##for i in arr:
##   print(i,i**2,sep="->")

##using end

##arr=[10,20,30,40,50]
##for i in arr:
##    print(i,end="")

##for i in 12345:
##    print(i,end=" ")
##

##for i in "123.34":
##    print(i,end= " ")

##for i in [1,1,1,1,1,0,9,8,7,6]:
##    print("Hello")

##range function

##print(range(20))
##
##for temp in range(8):
##    print(temp)

##for temp in range(5,11):
##    print("Hello")
##    
## for odd numbers
    
##for temp in range(1,11,2):
##    print(temp,end=" ")

## for even numbers

##for temp in range(2,11,2):
##    print(temp,end=" ")

##
##for temp in range(5,101,5):
##    print(temp,end=" ")
##
##for i in range(100,4,-5):
##    print(i)
##
##ele=[1,2,7,9,15,14]
##num=int(input("Enter a number to search"))
##flag=0
##for i in ele:
##    if num==i:
##        flag=1
##        print("Element Found !")
##        break
##
##if(flag==0):
##       print("Element not found !")
#### for else statements
##for i in ele:
##    if num==i:
##        flag=1
##        print("Element Found !")
##        break
##
##else:
##       print("Element not found !")
##1

##limit=int(input("Enter your limit:"))
##for i in range(limit+1):
##            print(i)

##2
##limit=int(input("Enter your limit:"))
##n=1
##while (n<=limit):
##     print(limit)
##     n-=1
 ##3

##for temp in range(2,100,2):
##   print(temp,end= " ")
##4

## 4: sum od all natural numbers
##n=int(input("Enter your limit:"))
##i=1
##sum=0
##while(i<=n):
##   sum=sum+i
##   i+=2
##print(sum)

##5: sum  of all even natural numbers
n=int(input("Enter your limit:"))
i=1
sum=0
while(i<=n):
   sum=sum+i
   i+=1
print(sum)
