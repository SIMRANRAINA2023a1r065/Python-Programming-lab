#30/9/25
# Tuple properties:
# 1) It is a sequence (it allow indexing and slicing)
# 2) It is an ordered collection
# 3) It is immutable(operations like insertion,updation and deletion)
# 4) It may contains duplicate elements
# 5) It preserve the insertion order
# 6) It may contains different type of objects
t=tuple(iter)
t=(1,2,3,4)

t=tuple("james")
print(t,type(t))
t=('j','a','m','e','s')
print(t,type(t))
t=10,20,30 #packing
print(t,type(t))
t=[10],[20],[30]
print(t,type(t))
a,b,c=t#unpacking
print(f"a:{a} b:{b} c:{c}")
t=10,20,30,40,50
print(t)

t=(10,20,30)
print(t,type(t))
#or
t=10,20,30
print(t,type(t))

#tuple k andr 3 list hai
#packing tuple
t=[10],[20],[30]
print(t,type(t))

#unpacking tuple------
t=10,20,30
a,b,c=t
print(f" a:{a} b:{b} c: {c}")

a,b=t
print(f" a:{a} b:{b}")

# *->varar : 0 or more extra parameter it contains
t=10,20,30,40,50
print(t)
a,*b,c=t
print(a,b,c)

t=10,20
print(t)
a,*b,c=t
print(a,b,c)

#swap two numbers:num1,num2 are tuples here
num1,num2=int(input("Enter first number:")),int(input("Enter second number:"))
print(f"Before swap num1:{num1} num2:{num2}")
num1,num2=num2,num1
print(f"After swap num1:{num1} num2:{num2}")

#fibonacci series:
# 0 1 1 2 3 5 8 13 21 34
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(8) :
    num3=num1+num2
    print(num3,end=" ")
    num1=num2
    num2=num3

    #or

num1,num2=0,1
for i in range(10) :
    print(num1,end=" ")
    num1,num2=num2,num1+num2

##imp:for exams

num1=(10) ## it takes it as an integer , use , after that one element in a tuple
print(type(num1))

##correct way

num1=(10,) 
print(type(num1))

#or
num1=10,
print(type(num1))

#tuple m modification nhi ho skta hai
#2 methods:count, index,slicing
#tuple is immutable list

t=(10,20,30,40,50)
print(t.count(30))
print(t.index(40))
# print(t[0],t[-1],t[2:-2],t[::-1])
# t[0]=1000
# print(t[0])
# del(t[-1])
t=(12,12.4,12+5j,True,"james",[10,20,30]) #tuple m multiple values store ho skta hai , tuple m list jo hai voh mutable hai toh hm change kr skte hai uski value yah append kr skte hai
t[-1].append(1000)
print(t)

#dictionary properties
# a) It is not a sequence (indexing and slicing are not allowed)
# b) It is an un-ordered collection.
# c) It is mutable(operations like insertion updation and deletion)
# d) It may contains duplicate values but key are always unique
# f) It preserve the insertion order
# g) It may contains only immutable type of obj as keys
# but any type of obj as value

#for tight bounding b/w the values, we us ductionary
 #1)
name ={"james":3000,"simran":67890,"mahi":45900,"payal":67890,"diya":45670}
print(name[-1]) # indexing is not allwoed here

# use key here
name ={"james":3000,"simran":67890,"mahi":45900,"payal":67890,"diya":45670}
print(name["simran"])

#  2) data matter krta hai but sequence nhi
#jaha indexing ho, vaha order matter krta hai nhi tih nhi
d1={'r':'red' ,'b':'blue'}
d2={'b':'blue' ,'r':'red'}
print(d1==d2)

#3)
# for making empty dictionary #key can`t be repeated, its unique... if key is there, it overwrites it nhi toh add krdega dictionary m simply`
d=dict()
d={}
print(d,id(d))
d['r']='red'
print(d,id(d))
d['b']='blue'
print(d,id(d))
d['b']='black'
print(d,id(d))
del(d['r'])
print(d,id(d))

# 6): keys are only immutable , value kuch bhi ho skti hai
d={"int":10,"str":"james","list":[10,20,30],"tuple":(10,)}
print(d)
# hash: m immutable type of data hota hai
