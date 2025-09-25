#list data structure
# it may contain different types of objects
#sum is a fn that do sum of all the list and len is a fn that gives the length of a string
lst=[12,12.5,12+5j,"james",True,[10,20,30],sum,len]
for i in lst:
    print(i,type(i)) # it can hold mutable and immutable type of objects
print(lst[-1]("simran"))
print(lst[-2][1,3,4,5])

#list can grow and shrink at runtime
lst=[]
print(lst,id(lst)) # ek hi object hai ... same list badal raha hai , mutable hai list
lst.append(10)
print(lst,id(lst))
lst.append(20)
print(lst,id(lst))
lst.append(30)
print(lst,id(lst))
lst.append(40)
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))

##list of a list
lst=[[1,2,3],[4,5,6],[7,8,9]]
for i in lst:
    print(i)

#even k liye star print kro aur odd k liye space hona chahiye
# use of nested list
lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:
    for ele in cl:
        if(ele%2==0):
            print("*",end=" ")
    print()
        
else:
    print(" ",end=" ")
print()

lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:
    for ele in cl:
        print(ele**2,end=" ")
    print()

## now replacing the above list numbers to its square
## using indexing(range)# for index
lst=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j]=lst[i][j]**2
    print(lst,end=" ")
    print()

# square of every number in list having elements as lsit and integers in it
lst=[[1,2,3],4,5,6,[7,8,9]]
for i in lst:
    for j in i: 
        print(j**2,end=" ") ## integer object is iterable

# for non- collection # numbers(integers) pe nested loop nhi chlega
lst=[[1,2,3],4,5,6,[7,8,9]]
for i in lst:
    if type(i)==list:
     for j in i: 
        print(j**2,end=" ")
    else:
        print(i**2,end=" ")

lst=[]
n=int(input("no of objects:"))
for i in range(n):
    num=int(input("Enter the number:"))
    lst.append(num)

print(lst)
# for different types of value at runtime: eval
lst=[]
n=int(input("no of objects:"))
for i in range(n):
    
    lst.append(eval(input("enter the obj")))

print(lst)
# string functions
lst=list()
lst.append("simran")
lst.append("payal")
lst.append("mahi")
print(lst)
#insert: for putting a new value at the middle or at a specific position
lst=list()
lst.append("simran")
lst.append("payal")
lst.append("mahi")
print(lst)
lst.insert(1,"diya")
print(lst)
lst.insert(1,"diya") ## it can insert or can have duplicate value as well
print(lst)
print(lst.count("diya"))
# for seeing index
print(lst.index("payal",1,4))
#string, list , tuple m index, count use hota hai

lst1=["red","green","blue"]
lst2=["violet","cyan"]
for i in lst2:
    lst1.append(i)

print(lst1)
 # using extend
lst1=["red","green","blue"]
lst2=["violet","cyan"]
print(lst1,id(lst1))
lst1.extend(lst2)
print(lst1,id(lst1)) # same id

# list pf even numbers
lst=list(range(2,11,2))
print(lst)
#pop:last inserted element remove krega 
lst=list(range(2,11,2))
res=lst.pop() # by default last value ko pop krega
print(f"Popped element is {res}")
print(lst)

lst=list(range(2,11,2))
res=lst.pop(1) # index 1 ki value remove krega
print(f"Popped element is {res}")
print(lst)
 # pop pe lgega index, remove value se httata hai
lst=["james","neena","blake","neena","simran"]
lst.remove("neena")
del(lst[0]) # 3rd way to remove
print(lst)
## saara kuch hatana ho toh ,puri list htani ho toh
lst=["james","neena","blake","neena","simran"]
lst.remove("neena")
del(lst[0]) # 3rd way to remove
print(lst)
lst.clear()
print(lst)
# sorting list
# aur sorting same type of object m hoti hai
lst=["james","neena","blake","neena","simran"]
print(f"Before sort: {lst}")
lst.sort()
print(f"after sort: {lst}")
# sort in descending order , bada se chota
lst=["james","neena","blake","neena","simran"]
print(f"Before sort: {lst}")
lst.sort(reverse=True)
print(f"after sort: {lst}")
 # for not modifying or changing the original list
lst=["james","neena","blake","neena","simran"]
print(f"Before sort: {lst}")
#lst.sort(reverse=True)
res=sorted(lst)
print(f"after sort: {res}")
print(f"Original list: {lst}")
